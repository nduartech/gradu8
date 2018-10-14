(function($) {

  $('#meal_preference').parent().append('<ul class="list-item" id="newmeal_preference" name="meal_preference"></ul>');
  $('#meal_preference option').each(function(){
      $('#newmeal_preference').append('<li value="' + $(this).val() + '">'+$(this).text()+'</li>');
  });
  $('#meal_preference').remove();
  $('#newmeal_preference').attr('id', 'meal_preference');
  $('#meal_preference li').first().addClass('init');
  $("#meal_preference").on("click", ".init", function() {
      $(this).closest("#meal_preference").children('li:not(.init)').toggle();
  });
  
  var allOptions = $("#meal_preference").children('li:not(.init)');
  $("#meal_preference").on("click", "li:not(.init)", function() {
      allOptions.removeClass('selected');
      $(this).addClass('selected');
      $("#meal_preference").children('.init').html($(this).html());
      allOptions.toggle();
  });


   

  var marginSlider = document.getElementById('slider-margin');
  if (marginSlider != undefined) {
      noUiSlider.create(marginSlider, {
            start: [15],
            step: 1,
            connect: [true, false],
            tooltips: [true],
            range: {
                'min': 12,
                'max': 19
            },
            format: wNumb({
                decimals: 0,
                thousand: ',',
                prefix: ' ',
            })
    });
  }
  $('#reset').on('click', function(){
      $('#register-form').reset();
  });


  $('#register-form').validate({
    rules : {
        first_name : {
            required: false,
        },
        last_name : {
            required: false,
        },
        company : {
            required: false
        },
        email : {
            required: false,
            email : flase
        },
        phone_number : {
            required: false,
        }
    },
    onfocusout: function(element) {
        $(element).valid();
    },
});

    jQuery.extend(jQuery.validator.messages, {
        required: "",
        remote: "",
        email: "",
        url: "",
        date: "",
        dateISO: "",
        number: "",
        digits: "",
        creditcard: "",
        equalTo: ""
    });
})(jQuery);