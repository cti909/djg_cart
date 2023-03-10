// function tem() {
    $( ".left_button" ).click(function() {
        $(".right_button").removeClass('not-allowed');
        let id = $(".quantity").val();
        id = parseInt(id)
        id <= 1 ? id=1 : id --;
        id == 1 ? $(".left_button").addClass("not-allowed") : 0;
        console.log(id)
        $(".quantity").val(id);
    });

    $( ".right_button" ).click(function() {
        $(".left_button").removeClass("not-allowed");
        let number = $(".number").attr("value");
        let id = $(".quantity").val();
        id = parseInt(id)
        id>=number ? id=number : id++
        id == number ? $(".right_button").addClass("not-allowed") : 0;
        console.log(id)
        $(".quantity").val(id);
    });

    $(".quantity").change(function(){
        let number = $(".number").attr("value");
        let id = $(".quantity").val();
        id = parseInt(id)
        if (id <= 1 ) {
            $(".left_button").removeClass('not-allowed');
        } else {
            $(".right_button").addClass('not-allowed');
        }
        if (id >= number ) {
            $(".left_button").removeClass('not-allowed');
        } else {
            $(".right_button").addClass('not-allowed');
        }
        parseInt(id) >= parseInt(number) ? id = number : 0;
        parseInt(id) <= 1 ? id = 1 : 0;
        $(".quantity").val(id);
    })
// }
// export {tem};