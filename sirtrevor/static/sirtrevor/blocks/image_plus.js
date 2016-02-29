/*
  Imageplus Block

  Notice: radio button name is prefixed with editorID_blockId for grouping radio buttons, stripped off when serializing
*/
(function($){
  window.SirTrevor.Blocks.Imageplus = SirTrevor.Blocks.Image.extend({
    type: "Imageplus",
    title: "Image",

    toolbarEnabled: true,
    droppable: false,
    uploadable: true,
    pastable: false,

    upload_options: {
      html: [
        '<div class="st-block__upload-container">',
        '<button class="st-upload-btn">Choose a image</button>',
        '<input type="hidden" class="input_filer_image">',
        '<img class="thumbnail" style="display: none">',
        '<span class="image_description"></span>',
        '<img class="filerClearer" style="visibility: hidden" width="10" height="10" alt="Clear" title="Clear">',
      ].join('\n')

    },

    _serializeData: function() {
      var data = {};
      if(this.$(':input').not('.st-paste-block').length > 0) {
        this.$(':input').not('[type="radio"]').each(function(index, input) {
          if (input.getAttribute('name')) {
            data[input.getAttribute('name')] = input.value;
          }
        });
        this.$(':input[type="radio"]').each(function(index, input) {
          if(input.checked) {
            data[input.getAttribute('name').split('_').pop()] = input.value;
          }
        });
      }
      return data;
    },

    loadData: function(data) {

      if(data.float == null || data.float == '') {
        data.float = 'none';
      }

      var container = this;

      var img = $('<img>', {
          src: (function () {
            if (!data.file)
              return '';
            if (data.file[0])
              return data.file[0].url;

            return data.file.url;
          })(),
          style: 'width: 33%',
        });
      var div = $('<div>', { 'style': 'text-align:' + (data.float == 'none' ? 'center' : data.float) }).append(img);

      var div_label = $('<div>', { style: 'width: 100%; clear: both;'});
      $.each(['left', 'none', 'right'], function(index, value) {
        div_label.append(
          $('<label style="padding: 12px 0; width: 33%; display: inline-block; text-align: center">').append(
            $('<input>', {
              style: 'margin-right: 5px; vertical-align: baseline',
              type: 'radio', name: container.instanceID + '_' + container.el.id + '_float', value: value,
              class: 'st-img-float-' + value,
              checked: (data.float == value ? true : false)
            }).click(function(event){
              div.css('text-align', value == 'none' ? 'center' : value);
            }),
            value
          )
        );
      });

      div.append(div_label);
      div.append($('<input>', {
          type: 'text', 
          name: 'caption', 
          style: 'width: 95%;', value: data.caption,
          placeholder: 'Caption'
        })
      );

      this.$editor.html(div).show();
    },


    onBlockRender: function(){
      /* Setup the upload button */
      me = this;
      
      this.$inputs.find('.st-upload-btn').bind('click', function(ev){ ev.preventDefault();
        /* mimic filer popup_handling behavior */  
        var input_field = $(this).siblings('input.input_filer_image')
        var thumbnail = $(this).siblings('img.thumbnail')
        var description = $(this).siblings('span.image_description')
        var clearer = $(this).siblings('img.filerClearer')
        /* popup will trigger change event, use that to fill image block */
        $(input_field[0]).on('change', function(evt){
          me.$inputs.hide();
          me.loading();
          var chosenId = this.value;
          $.get('/beheer/sirtrevor/filer/' + chosenId, function(data) {
            me.setData({'file': data});
            me.loadData({'file': data});
            me.ready();
          });
        });
        var elem_id = me.blockID + '_' + me.instanceID + "_image";
        input_field[0].id = elem_id;
        thumbnail[0].id = elem_id + '_thumbnail_img';
        description[0].id = elem_id + '_description_txt';
        clearer[0].id = elem_id + '_clear';

        win = window.open('/beheer/filer/folder/last/?_to_field=file_ptr&_popup=1', elem_id, 'height=500,width=800,resizable=yes,scrollbars=yes'); 
        win.focus(); 
        return false;
      });
    },

    onUploadSuccess : function(data) {
      this.setData(data);
      this.ready();
    },

    onUploadError : function(jqXHR, status, errorThrown){
      this.addMessage('Upload Error');
      this.ready();
    },
  });
})(django.jQuery);