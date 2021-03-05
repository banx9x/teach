export const ITEMS_PER_PAGE = 5;

export default function (options) {
    const { method, url, body } = options;
    let result = {};

    return new Promise((resolve, reject) => {
        let xhr = new XMLHttpRequest();
        xhr.responseType = "json";

        xhr.open(method, url);
        xhr.send(body ? body : null);

        xhr.onload = () => {
            if (xhr.status == 200) {
                result.data = xhr.response;
                result.headers = xhr
                    .getAllResponseHeaders()
                    .split("\r\n")
                    .reduce((obj, item) => {
                        let [key, value] = item.split(": ");
                        obj[key] = value;
                        return obj;
                    }, {});
                resolve(result);
            } else {
                reject(xhr.status + ":" + xhr.statusText);
            }
        };

        xhr.onerror = () => reject("Ooops!");
    });
}

export function loading() {
    let div = document.createElement("div");
    div.className = "loading";
    document.body.appendChild(div);
    return div;
}

export function createPost(post, user) {
    let html = `
        <div class="post">
            <a class="post-link" href="post.html?id=${post.id}">
                <h3 class="post-title">${post.title}</h3>
            </a>

            <p class="post-short-desciption">${post.body}</p>
            <p class="post-author">By
                <a class="author-link" href="postbyuser.html?userId=${user.id}">
                    ${user.username}
                </a>
            </p>
        </div>
    `;

    return html;
}

export function createPostDetail(post) {
    let html = `
        <div class="post">
            <h2 class="post-title">${post.title}</h2>
            <p class="post-desciption">${post.body}</p>
        </div>
    `;

    return html;
}

export function createComment(comment) {
    let html = `
        <div class="comment">
            <h4 class="comment-name">${comment.name}</h4>
            <p class="comment-email">${comment.email}</p>
            <p class="comment-body">${comment.body}</p>
        </div>
    `;
    return html;
}

export function createPagination(total, current, link) {
    let frag = document.createDocumentFragment();

    if (total == 1) {
        return frag;
    }

    for (let i = 1; i <= total; i++) {
        if (i == 1 || i == total || (i > current - 2 && i < current + 2)) {
            let a = document.createElement("a");
            a.classList.add("pagination-item");

            if (i != current) {
                a.href = link + i;
            } else {
                a.classList.add("current");
            }

            a.textContent = i == 1 ? "First" : i == total ? "Last" : i;

            frag.appendChild(a);
        }
    }

    return frag;
}

export function changeItemsPerPage() {
    let url = new URL(window.location.href);
    let limit = url.searchParams.get("_limit") || ITEMS_PER_PAGE;
    let select = document.getElementById("posts-per-page");
    select.value = limit;

    select.onchange = function (e) {
        url.searchParams.set("_limit", e.target.value);
        window.location.href = url;
    };
}
