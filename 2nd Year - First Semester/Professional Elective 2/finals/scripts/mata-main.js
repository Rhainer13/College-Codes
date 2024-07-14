const theSelect = document.getElementById("theSelect")

const ctu_main = document.getElementById("ctu-main") 
const cnu_main = document.getElementById("cnu-main") 
const up_cebu = document.getElementById("up-cebu")

const usc_main = document.getElementById("usc-main")
const usjr = document.getElementById("usjr")
const citu = document.getElementById("citu")


theSelect.addEventListener("change", function (event){
    if(event.target.value == "Public"){
        ctu_main.style.display = "block"
        cnu_main.style.display = "block"
        up_cebu.style.display = "block"

        usc_main.style.display = "none"
        usjr.style.display = "none"
        citu.style.display = "none"
    }
    else if(event.target.value == "Private"){
        ctu_main.style.display = "none"
        cnu_main.style.display = "none"
        up_cebu.style.display = "none"

        usc_main.style.display = "block"
        usjr.style.display = "block"
        citu.style.display = "block"
    }
    else{
        ctu_main.style.display = "block"
        cnu_main.style.display = "block"
        up_cebu.style.display = "block"

        usc_main.style.display = "block"
        usjr.style.display = "block"
        citu.style.display = "block"
    }
})