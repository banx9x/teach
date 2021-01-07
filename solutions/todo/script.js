// list todo ban đầu
let todos = [
    { id: 1, title: "Đòi nợ Thảo 10$", completed: false },
    { id: 2, title: "Code demo todo list", completed: true },
];

// Mảng chứa các element todo
// 2 mảng riêng biệt cho 2 loại doing và completed
let doingList = [];
let completedList = [];

// Khởi tạo ban đầu, duyệt qua mảng todos, tạo node với từng mục, thêm vào danh sách doing hoặc completed tùy thuộc vào thuộc tính completed true hay false
for (let i = 0; i < todos.length; i++) {
    if (todos[i].completed) {
        completedList.push(createItems(todos[i]));
    } else {
        doingList.push(createItems(todos[i]));
    }
}

// Hàm tạo một todo item li>label>input
function createItems(todo) {
    let li = document.createElement("li");
    li.className = "items";

    let input = document.createElement("input");
    input.type = "checkbox";
    input.dataset.id = todo.id;

    // Gắn sự kiện cho checkbox
    input.onchange = function () {
        // Khi check, cập nhật trong todos list
        todos[this.dataset.id - 1].completed = this.checked;
        // Animation tý
        li.style.transform = "translateX(15px)";
        li.style.opacity = 0;

        // Sau khi animation
        setTimeout(() => {
            // Xóa node cũ
            // Lưu ý node vẫn còn tồn tại trong JS
            li.remove();
            // Trả lại style ban đầu (bên trên animated)
            li.style.transform = "";
            li.style.opacity = 1;

            // Check vừa bấm hoàn thành hay chưa
            if (this.checked) {
                // Nếu hoàn thành, cập nhật lại doingList (xóa bớt phần tử)
                doingList = doingList.filter((i) => i != li);
                // Thêm chính phần tử đó vào completed
                completedList.push(li);
            } else {
                // Ngược lại
                completedList = completedList.filter((i) => i != li);
                doingList.push(li);
            }

            // Cập nhật xong thì render lại
            render();
            // Alert báo đã cập nhật
            showAlert("Đã cập nhật nhé 😊");
        }, 250); // Đợi animation xong
    };

    // Kiểm tra thuộc tính completed, nếu true thì thêm thuộc tính check cho checkbox
    todo.completed && (input.checked = true);

    // Tạo label, append input
    let label = document.createElement("label");
    label.append(input);
    label.append(todo.title);

    // Append label vào li, then return
    li.append(label);
    return li;
}

let form = document.forms.todo;
let doing = document.getElementById("doing-list");
let completed = document.getElementById("completed-list");
let alertwrapper = document.getElementById("alert-wrapper");

// Thêm sự kiện cho form
form.addEventListener("submit", function (ev) {
    // Ngăn event mặc định, không cho trình duyệt load lại
    ev.preventDefault();
    let input = form.elements.new;

    // Kiểm tra nếu input rỗng thì chửi
    if (input.value.trim() == "") {
        input.placeholder = "Hey, write something stupid";
        return;
    }

    // Tạo object todo mới, thêm vào mảng todos
    let newTodo = {
        id: todos.length + 1,
        title: this.elements.new.value,
        completed: false,
    };
    todos.push(newTodo);
    // Tạo một node mới, push vào doingList
    doingList.push(createItems(newTodo));
    // Reset form
    this.elements.new.value = "";
    input.placeholder = "What do you want to do?";
    // Render lại =]]
    render();
    // Alert báo đã thêm thành công
    showAlert("Đã thêm rồi nhé 🤣");
});

function showAlert(msg) {
    let div = document.createElement("div");
    div.className = "alert";

    let p = document.createElement("p");
    p.textContent = msg;

    let icon = document.createElement("span");
    icon.className = "material-icons";
    icon.textContent = "close";

    div.append(p, icon);

    alertwrapper.append(div);
    let timer = setTimeout(() => {
        div.classList.add("flyout");

        setTimeout(() => div.remove(), 300);
    }, 4700);

    icon.onclick = () => {
        clearTimeout(timer);
        div.classList.add("flyout");
        setTimeout(() => div.remove(), 300);
    };
}

// Hàm render, duyệt qua 2 mảng doingList và completedList (chứa các node đã tạo)
// Kiểm tra node đã có trong DOM hay chưa
// Nếu chưa có thì thêm vào, i cmn zi
function render() {
    if (doingList.length > 0) {
        // Thêm cái text hiển thị nếu không có node nào
        doing.lastElementChild.style.display = "none";
        doingList.forEach((i) => {
            if (!doing.contains(i)) {
                doing.prepend(i);
            }
        });
    } else {
        doing.lastElementChild.style.display = "block";
    }

    if (completedList.length > 0) {
        completed.lastElementChild.style.display = "none";
        completedList.forEach((i) => {
            if (!completed.contains(i)) {
                completed.prepend(i);
            }
        });
    } else {
        completed.lastElementChild.style.display = "block";
    }
}

// Chạy hàm render ban đầu
render();
