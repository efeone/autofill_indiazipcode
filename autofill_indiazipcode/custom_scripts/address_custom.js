frappe.ui.form.on("Address", {
	postal_code: function (frm, cdt, cdn) {
		let pincode = cint(frm.doc.postal_code); // 680741 , 670106, 1
		if(pincode!=0){
			frappe.call({
				"method": "autofill_indiazipcode.api.get_by_pincode",
				args: {
					pincode: pincode,
				},
				callback: function (r) {
					if(r.message){
						let result = JSON.parse(r.message)
						let arr_pincode = Object.keys(result["pincode"]);

						if (arr_pincode.length>1){
							frappe.prompt(
								{
									label: "Post Office",
									fieldtype: "Select",
									reqd: 1,
									fieldname:'post_office',
									options: arr_pincode,
									default: arr_pincode[0]								
								},
								function(data) {
									let post_office = data.post_office;
									set_value_by_post_office(frm, result, post_office);
									
								}
							)
						}else if(arr_pincode.length==1){
							let post_office = arr_pincode[0];
							set_value_by_post_office(frm, result, post_office);
						}else{
							frappe.msgprint(__("This Postal Code does not match."));
							frm.set_value("pincode", pincode);
							frm.set_value("post_office", "");
							frm.set_value("state", "");
							frm.set_value("county", "");
							frm.set_value("taluk", "");
						}			
					}	
				}
			})
		}
	},
});

var set_value_by_post_office = function (frm, result, post_office){
	frm.set_value("pincode", result["pincode"][post_office]);
	frm.set_value("post_office", post_office);
	frm.set_value("country", "India");
	frm.set_value("state", result["statename"][post_office]);
	frm.set_value("county", result["Districtname"][post_office]);
	frm.set_value("taluk", result["Taluk"][post_office]);	
}
