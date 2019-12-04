


const toastsContainer = document.createElement("div");
document.body.appendChild(toastsContainer)
const toastButtons = document.querySelectorAll(".button");
Object.assign(toastsContainer.style,
    {
        position: "absolute",
        bottom: 0,
        right: 0
    })

for (const toastButton of toastButtons) {
    toastButton.addEventListener("click", function () {
        createToast(toastButton.textContent, 5000);
    })
}

function createToast(message, duration) {
    const toast = document.createElement("div");
    toast.classList.add("toast")
    toast.textContent = message;
    console.log(message)
    toastsContainer.appendChild(toast);
    setTimeout(function () {
        toastsContainer.removeChild(toast);
    }, duration);

}