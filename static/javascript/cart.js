console.log('hello');
var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++ ){
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:',productId , 'action:',action)
 
        console.log('USER:',user)
        if(user === 'AnonymousUser' ){
            alert('Please Login To continue');
            window.location.href="/login"
        }
        else{
            updateUserOrder(productId,action)
        }
    })
}

function updateUserOrder(productId,action){
    console.log('user is logged in  ,sending data.. ' )
    var url = '/updateItem/'
    fetch(url , {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId , 'action' : action})
    }) 

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:' ,data)
        location.reload()
    })
}