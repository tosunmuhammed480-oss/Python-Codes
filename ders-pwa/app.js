let data = JSON.parse(localStorage.getItem("schedule") || "{}");

const DAYS = [
    "Pazartesi","Salı","Çarşamba","Perşembe",
    "Cuma","Cumartesi","Pazar"
];

DAYS.forEach(d => {
    if (!data[d]) data[d] = [];
});

function save() {
    localStorage.setItem("schedule", JSON.stringify(data));
}

function addItem() {
    const day = document.getElementById("day").value;
    const title = document.getElementById("title").value;
    const duration = document.getElementById("duration").value;
    const start = document.getElementById("start").value;

    if (!title || !duration) {
        alert("Başlık ve süre zorunlu.");
        return;
    }

    data[day].push({
        title,
        duration,
        start: start || null
    });

    save();
    render();
}

function render() {
    const list = document.getElementById("list");
    list.innerHTML = "";

    DAYS.forEach(day => {
        list.innerHTML += `<div class="day-title">--- ${day} ---</div>`;

        if (data[day].length === 0) {
            list.innerHTML += `<div>(Etkinlik yok)</div>`;
        }

        data[day].forEach((item, i) => {
            list.innerHTML += `
                <div>${i+1}. ${item.title} — ${item.duration} dk 
                ${item.start ? "(Başlangıç: " + item.start + ")" : ""}
                </div>
            `;
        });
    });
}

render();
