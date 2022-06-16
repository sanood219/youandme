jQuery('#form').validate({
    rules:{
      fullname:"required",
      phone:"required"
    },messages:{
      fullname:"please enter your full name"
    }
  })