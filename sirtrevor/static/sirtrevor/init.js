$(function() {
    $('.js-st-instance').each(function(i,el) {
        var $el = $(el),
            conf = $el.data('sirtrevor-conf'),
            defaults = $el.data('sirtrevor-defaults'),
            st,
            options;

        options = _.extend({}, conf, {el: $el});
        st = new SirTrevor.Editor(options);
        
        SirTrevor.setDefaults(defaults);
    });
});
