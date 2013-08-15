	App.Collections.Contacts = Backbone.Collection.extend({
		model: App.Models.Contact,
		url: '/contacts', 
		parse: function(res) {
			return _.map(res, function(contact){
				contact._id = contact._id.$oid;
				return contact;
			})
		}
	});