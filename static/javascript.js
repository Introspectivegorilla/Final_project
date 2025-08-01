

function to_new_set() {
    console.log("in to new set")
    location.href = "new"

}

function to_my_cards() {
    location.href = "library"

}

function to_register() {
    location.href="register"
}

function create_new() {

    const container = document.getElementsByClassName("box3 r-corner")[0]
    const new_card = document.createElement('input')
    const button = document.getElementsByClassName('btn3')[0]

    const new_card_answer = document.createElement('input')
    new_card_answer.name="response"
    new_card_answer.className="answer"
    new_card_answer.type='text'
    new_card_answer.classList.add("link_font")

    new_card.name = "prompt"
    new_card.className = "question"
    new_card.type="text"
    new_card.classList.add("link_font")


    container.appendChild(new_card)
    container.appendChild(new_card_answer)
    button.after(new_card_answer)
    button.after(new_card)
}

 let card_index = 0;
 let showing_prompt = true;

function flip_card() {

    console.log(card_index)
    const card_box = document.getElementsByClassName('box1')[0]
    const grab_data = document.getElementById("data-box")
    const card_set = JSON.parse(grab_data.dataset.info);
    const prompt_box = document.getElementById("prompt-response")
    
    if ((card_index < card_set.length) && (showing_prompt===false)) {
        prompt_box.textContent = card_set[card_index]['prompt']
        showing_prompt = true;
        return;
    }
    else if (card_index < card_set.length) {
        prompt_box.textContent = card_set[card_index]['response']
        showing_prompt = false;
        return;
    }

    else {

        next_card();
    }
}

function next_card() {

    const grab_data = document.getElementById("data-box")
    const card_set = JSON.parse(grab_data.dataset.info);


    if (card_index < card_set.length) {
        card_index++
        showing_prompt = false;
        flip_card();
    }
    else {

        card_index = 0;
        console.log("this has been triggered")
        showing_prompt = false;
        flip_card();
    }


    }

function to_log_out() {
    fetch('/logout', {method: 'POST',credentials:'same-origin'}).then(function(response) { if (response.redirected) { window.location.href = response.url;}});
}