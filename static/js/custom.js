const modalContactenos = () => {
    const modal = document.getElementById('modal-contactenos')
    const body = document.querySelector('body').style.backgroundColor = '#fff'
    // modal.classList.toggle("show");
    modal.classList.toggle("hidden");
} 


const contactenos = document.getElementById('nav-contactenos').addEventListener("click", modalContactenos);
const contactenosClose = document.querySelector('.modal-close').addEventListener("click", modalContactenos);