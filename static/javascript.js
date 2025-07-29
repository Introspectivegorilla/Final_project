

function to_new_set() {
    console.log("in to new set")
    location.href = "new"

}

function to_my_cards() {
    location.href = "library"

}

function create_new() {

    const container = document.getElementsByClassName("box3 r-corner")[0]
    const new_card = document.createElement('input')
    const button = document.getElementsByClassName('btn3')[0]

    const new_card_answer = document.createElement('input')
    new_card_answer.name="response"
    new_card_answer.className="answer"
    new_card_answer.type='text'

    new_card.name = "prompt"
    new_card.className = "question"
    new_card.type="text"


    container.appendChild(new_card)
    container.appendChild(new_card_answer)
    button.after(new_card_answer)
    button.after(new_card)
}

 let card_index = 0;
 let showing_prompt = false;

function flip_card() {

   
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

        console.log("no cards left")
    }

//function next_card():


}