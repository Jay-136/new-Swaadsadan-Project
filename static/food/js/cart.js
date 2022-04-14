

$(function () {

    var cartd = JSON.parse(cartdata);
    cartc = cartd
    console.log(cartd["items"][0]);
    var row = '';
    for (let index = 0; index < cartd["items"].length; index++) {
        const element = cartd["items"][index];
        console.log(element);
         row += `<div class="row">
<div class="row main align-items-center">
    <div class="col-2"><img class="img-fluid" src="`+element["img-link"]+`"></div>
    <div class="col">
        <div class="row text-muted">`+element["item-name"]+`</div>
        <div class="row">`+element["description"]+`</div>
    </div>
    <div class="col"> <button class="qtybtn" onclick=qtym(`+index.toString()+`)>-</button><span class="border qty"  id="qty-`+index.toString()+`" >`+element["quantity"]+`</span><button class="qtybtn" onclick=qtyp(`+index.toString()+`)>+</button></div>
    <div class="col">&#8377; <span id="price-`+index.toString()+`">`+element["price"]+`</span> <button class="close" onclick="deleteitem(this)" id="rm-`+index.toString()+`">&#10005;</button></div>
</div>
</div>`;
}
$(".item-column").html(row);
$("#subtotal-amount").html(cartc["total-amount"]);
$("#delivery-amount").html(cartc["delivery-amount"]);
$("#total-amount").html(cartc["total-amount"]+cartc["delivery-amount"]);
})
function qtym(btnid) {
    console.log(btnid);
    var quantity =  cartc["items"][parseInt(btnid)]["quantity"];
    const unitprice = cartc["items"][parseInt(btnid)]["price"];
    if (quantity<=1) {}
    else {
        
        quantity-=1;
        cartc["items"][parseInt(btnid)]["quantity"]-=1;
        const price = quantity*unitprice;
        $("#price-"+btnid).html(price);
        $("#qty-"+btnid).html(quantity);
        totalamount();
    }
}
function qtyp(btnid) {
    console.log(btnid);
    var quantity =  cartc["items"][parseInt(btnid)]["quantity"];
    const unitprice = cartc["items"][parseInt(btnid)]["price"];
    quantity+=1;
    cartc["items"][parseInt(btnid)]["quantity"]+=1;
    const price = quantity*unitprice;
    console.log("quantity");
    $("#price-"+btnid).html(price);
    $("#qty-"+btnid).html(quantity);
    totalamount();
    



}

function deleteitem(e){
    const id=e.id;
    var intid=id.split("-")[1];
    e.parentElement.parentElement.parentElement.remove();
    cartc["items"].splice(intid,1);
    console.log(cartc); 
}
function totalamount(){
    var stotalamount = 0;
    for (let index = 0; index < cartc["items"].length; index++) {
        stotalamount += cartc["items"][index]["price"]*cartc["items"][index]["quantity"];
        console.log(cartc["items"][index]["price"]);
    }
    console.log(stotalamount);
        $('#subtotal-amount').html(stotalamount);
        $('#total-amount').html(stotalamount+cartc["delivery-amount"]);
    
}
