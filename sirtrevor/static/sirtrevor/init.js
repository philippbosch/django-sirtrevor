$(function() {
    $('.js-st-instance').each(function(i,el) {
        var $el = $(el),
            defaults = $el.data('sirtrevor-defaults'),
            conf = $el.data('sirtrevor-conf'),
            st,
            options;

        SirTrevor.setDefaults(defaults);
        options = _.extend({}, conf, {el: $el});
        st = new SirTrevor.Editor(options);
    });
});
