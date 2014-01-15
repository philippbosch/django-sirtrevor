$(function() {
    $('.js-st-instance').each(function(i,el) {
        var $el = $(el),
            conf = $el.data('sirtrevor'),
            st,
            options;

        options = _.extend({}, conf, {el: $el});
        st = new SirTrevor.Editor(options);
    });
});
