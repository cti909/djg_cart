function add_cart(id, url_image, name, number, price, describe, producer, url_action) {
    var csrftoken = '{{ csrf_token() }}';
    // function add_cart() {
    // name = models.CharField(max_length = 100)
    // number = models.IntegerField()
    // price = models.IntegerField()
    // describe = models.CharField(max_length = 100, null=True)
    // producer = models.CharField(max_length = 100, null=True)
    // image
    // Create a form dynamically
    // $('#product{{id}}').click(function(){
        url_success = "'" + id  + "','" + url_action + "'";
        console.log(url_success)
        str = 
        "<div class='position-absolute zindex-offcanvas w-100 top-0 opacity-25' style='z-index: 1;'>"
        +"<div class='mask d-flex align-items-center gradient-custom-3 vh-100'>"
        +"    <div class='container'>"
        +"    <div class='row d-flex justify-content-center align-items-center h-100'>"
        +"       <div class='col-12 col-md-9 col-lg-7 col-xl-6'>"
        +"        <div class='card bg-secondary' style='border-radius: 15px;'>"
        +"            <div class='card-body p-3'>"
        +"            <h2 class='text-uppercase text-center mb-2'>Detail</h2>"     
        // +"           <form method='POST' action="+ url_action +">"
        // +"                {% csrf_token %}"
        +"               <div class='row'>"
        +"                    <div class='col-6'>"
        +"                      <img class='img-fluid' src='/media/"+ url_image +"' alt=''>"
        +"                  </div>"
        +"                  <div class='col-6'>"
        +"                      <h5 class='card-text' name='name'>Name: "+ name +"</h5>"
        +"                      <h5 class='card-text'>Total product: "+ number +"</h5>"
        +"                      <h5 class='card-text'>Price: "+ price +"$</h5>"
        +"                      <h5 class='card-text'>Producer: "+ producer +"</h5>"
        +"                        <div class='d-flex'>"
        // +"                          <h5 class='card-text' style='width: 80%;'>Enter the quantity: </h5>"
        // +"                          <input class='quantity' style='width: 20%;' type='text' name='number_buy'>"
        +"                        <button class='left_button btn btn-light number not-allowed' value="+number+" onClick='leftButton()'>"
        +"                             <i class='fa-solid fa-minus'></i>"
        +"                         </button>"
        +"                      <input type='text' class='quantity form-control input_num mx-2' value='1' onChange='changeInput()'>"
        +"                      <button class='right_button btn btn-light' onClick='rightButton()'>"
        +"                          <i class='fa-solid fa-plus'></i>"
        +"                      </button>"
        +"                      </div>"
        +"                  </div>"
        +"              </div>"
        +"              <div class='d-flex justify-content-center m-2'>"
        // +"                   <a href='"+ url_action +"'>"
        +"                  <button type='submit' class='btn btn-success btn-block btn-lg gradient-custom-4 text-body me-3' onClick=" + "success_buy("+ url_success +")>Add to cart</button>"
        // +"                  </a>"
        // +"                  <button type='submit' class='btn btn-success btn-block btn-lg gradient-custom-4 text-body me-3' onClick=" + "success_buy("+ 
        //                                                                         "'" + name + "','" + url_image + "','" + number + "','" + price + "','" + url_action + "'"
        //                                                                         +")>Add to cart</button>"
        +"                  <button class='btn btn-danger btn-block btn-lg gradient-custom-4 text-body' onClick='cancel_buy()' >Cancel</button>"
        +"              </div>"
        // +"          </form>"
        +"          </div>"
        +"      </div>"
        +"      </div>"
        +"  </div>"
        +"  </div>"
        +"    </div>"
        +"</div>";
        $('.showform').append(str);
}


function success_buy(id, url_action) {
    var quantity = document.getElementsByClassName('quantity')[0].value;
    console.log(url_action)
    var payload = JSON.stringify({
        product_id: id,
        number: quantity
      });
    $.ajax({
        url : url_action,
        type: "POST",
        // headers: {'X-CSRFToken': '{{ csrf_token }}'},
        data : payload,
        dataType : "json",
        // success: function( data ){
        //     console.log("success");
        // },
        // error: function(data) {
        //     console.log(data)
        // }
    }).done(function(data){
        console.log("done");
    }).fail(function(data){
        console.log("fail");
        console.log(data);
        // window.location.reload();
        document.location.href ="/cart/cart_home"
    });
}
function cancel_buy() {
    $('.showform').empty();
    // window.history.back()
}
function leftButton() {
    $(".right_button").removeClass('not-allowed');
    let id = $(".quantity").val();
    id = parseInt(id)
    id <= 1 ? id=1 : id --;
    id == 1 ? $(".left_button").addClass("not-allowed") : 0;
    console.log(id)
    $(".quantity").val(id);
}

function rightButton() {
    $(".left_button").removeClass("not-allowed");
    let number = $(".number").attr("value");
    let id = $(".quantity").val();
    id = parseInt(id)
    id>=number ? id=number : id++
    id == number ? $(".right_button").addClass("not-allowed") : 0;
    console.log(id)
    $(".quantity").val(id);
}

function changeInput(){
    
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
}