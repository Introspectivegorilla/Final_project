

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