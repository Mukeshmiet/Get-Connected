// {% load static %}
console.log('Hello from scripts.js');
// navigation bar
const accountOptEl = document.querySelector('.--account-options');
const accountEl = document.querySelector('.account-btn');
const mainTagEl = document.querySelector('.base-main');

const mouserhoverEl= function(){
    accountOptEl.style.display = 'inline-block';
    accountOptEl.style.position = 'absolute';
    accountOptEl.style.top = '70px';
    accountOptEl.style.right = '0';
}

accountEl.addEventListener('mouseover', mouserhoverEl);
mainTagEl.addEventListener('mouseover', function(){
    accountOptEl.style.display = 'none';
});