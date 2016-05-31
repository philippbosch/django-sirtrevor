/*
 Heading Block
 */
(function($){
    SirTrevor.Blocks.HeadingExtended = (function() {

        function setLevel(block, lev) {
            block.heading_level = lev;
            //console.log( 'setLevel( ' + lev + ' ) -> ' +lev+'+'+block.level_modifier );
            lev = parseInt(lev) + parseInt(block.level_modifier);
            $('#'+block.heading_id).replaceWith(function() {
                return '<h' + lev + ' id="' + block.heading_id + '" contenteditable="true">' +
                    $(this).text() +
                    '</h' + lev + '>';
            })
            $(block.$control_ui).children().each((function(_this) {
                return function(index, element) {
                    //console.log('element:', element);
                    if ($(element).attr("data-icon") === 'h'+block.heading_level) {
                        $(element).removeClass("heading_level_not_selected");
                        return $(element).addClass("heading_level_selected");
                    } else {
                        $(element).removeClass("heading_level_selected");
                        return $(element).addClass("heading_level_not_selected");
                    }
                };
            })(this));
        }

        function setLevel_1(ev) {
            ev.preventDefault();
            //console.log( 'setLevel_1' );
            setLevel(this, 1);
    //        $('#'+this.heading_id).replaceWith(function() {
    //            return '<h1>' + $(this).text() + '</h1>';
    //        })
        }

        function setLevel_2(ev) {
            ev.preventDefault();
            //console.log( 'setLevel_2' );
            setLevel(this, 2);
        }

        function setLevel_3(ev) {
            ev.preventDefault();
            //console.log( 'setLevel_3' );
            setLevel(this, 3);
        }

        function setLevel_4(ev) {
            ev.preventDefault();
            //console.log( 'setLevel_4' );
            setLevel(this, 4);
        }

        return SirTrevor.Block.extend({

        level_modifier: 1, // all level output is one level higher, e. g. h1 -> h2

        type: 'heading_extended',

        //title: function(){ return i18n.t('blocks:heading:title'); },
        title: function(){ return 'Heading'; },

        editorHTML: function() {
            this.heading_id = _.uniqueId('js-heading-');
            this.heading_level = 1;
            this.heading_text = 'text';
            //console.log('heading_id: ' + this.heading_id);
            return '<div class="st-text-block--heading" >' + //st-required st-text-block
                '<h1 id="' + this.heading_id + '" contenteditable="true">Heading' +
                '</h1></div>';
        },

        controllable: true,
        controls: {
            'h1': setLevel_1,
            'h2': setLevel_2,
            'h3': setLevel_3,
            'h4': setLevel_4
        },

        icon_name: 'heading',

        loadData: function(data){
            //console.log('HeadingExtended - loadData');
            //console.log( 'HeadingExtended - loadData level=' + data.level );
            //console.log( 'HeadingExtended - loadData text=' + data.text );
            this.heading_level = data.level;
            this.heading_text = data.text;
            //this.getTextBlock().html(SirTrevor.toHTML(data.text, this.type));
            $('#'+this.heading_id).text(this.heading_text);
            setLevel(this, this.heading_level);
            //console.log('HeadingExtended - loadData -> ' + $('#'+this.heading_id).html());
        },

        beforeBlockRender: function() {
            //console.log('beforeBlockRender');
            //console.log('HeadingExtended - beforeBlockRender -> ' + $('#'+this.heading_id).html());
        },

        onBlockRender: function() {
            //console.log('onBlockRender');
            $('#'+this.heading_id).text(this.heading_text);
            setLevel(this, this.heading_level);
            //console.log('HeadingExtended - onBlockRender -> ' + $('#'+this.heading_id).html());
        },

        _serializeData: function(){
            //console.log('HeadingExtended - toData');
            var dataObj = {};

            dataObj.level = this.heading_level;
            dataObj.text = $('#'+this.heading_id).text();

            //console.log( 'obj level=' + dataObj.level );
            //console.log( 'obj text=' + dataObj.text );

            //console.log('toData - setData');
            return dataObj;
        }

        });
    })();
})(django.jQuery);