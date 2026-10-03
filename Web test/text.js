const add_num = () => {
    const pElement = document.querySelector('#result');
    let currentTotal = parseInt(pElement.innerText) || 0;

    const inputElement = document.querySelector('#number');
    let inputValue = parseInt(inputElement.value) || 0;

    let newTotal = currentTotal + inputValue;

    pElement.innerText = newTotal;

    inputElement.value = '';
}

document.querySelector('.button').addEventListener('click', add_num);
