function addRedClassToHeader() {
    const header = document.querySelector('header');
    header.classList.add('red')
}
const redHeader = document.getElementById('red_header');
redHeader.addEventListener('click', addRedClassToHeader);
