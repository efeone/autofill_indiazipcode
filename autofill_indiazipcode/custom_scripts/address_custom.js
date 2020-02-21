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
						let result = r.message;

						if (Object.keys(result).length>1){
							let arr_post_office = Object.keys(result)
							frappe.prompt(
								{
									label: "Post Office",
									fieldtype: "Select",
									reqd: 1,
									fieldname:'post_office',
									options: arr_post_office,
									default: arr_post_office[0]								
								},
								function(data) {
									let post_office = data.post_office;
									set_value_by_post_office(frm, result[post_office]);									
								}
							)
						}else if(Object.keys(result).length==1){
							let post_office = result[Object.keys(result)[0]]["officename"];
							set_value_by_post_office(frm, result[post_office]);
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

var set_value_by_post_office = function (frm, result){
	frm.set_value("pincode", result["pincode"]);
	frm.set_value("post_office", result["officename"]);
	frm.set_value("country", "India");
	frm.set_value("state", result["statename"]);
	frm.set_value("county", result["districtname"]);
	frm.set_value("taluk", result["taluk"]);	
}