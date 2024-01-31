document.addEventListener('DOMContentLoaded', function(){
    const characterElement = document.getElementById('character');

    fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then((Response) => {
        if (!Response.ok) {
            throw new Error('Network response was ok');
        }
        return Response.json();
    })
    .then((data) => {
        const characterName = data.name;

        characterElement.textContent = characterName;
    })
    .catch((error) => {
        console.error('Error:', error);
    })
})
