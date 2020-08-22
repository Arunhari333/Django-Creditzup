function Activate(x){
    var nav_links = document.querySelectorAll('.bttn');
    console.log(nav_links.length);
    for(var i = 0; i < nav_links.length; ++i){
        nav_links[i].classList.remove('active');
    }
    nav_links[x].classList.add('active');
}
