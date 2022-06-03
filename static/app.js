const form = document.querySelector("form")

form.addEventListener("change", function(e){
    e.target.value = e.target.value.toLowerCase()
})