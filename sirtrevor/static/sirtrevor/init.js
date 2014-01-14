$(function() {
    $('.js-st-instance').each(function(i,el) {
        new SirTrevor.Editor({ el: $(el) });
    });
});
