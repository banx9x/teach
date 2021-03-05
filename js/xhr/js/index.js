import get, {
    loading,
    createPost,
    createPagination,
    changeItemsPerPage,
    ITEMS_PER_PAGE,
} from "./util.js";

changeItemsPerPage();

let listPosts = document.getElementById("list-posts");
let pagination = document.getElementById("pagination");

let spinner = loading();

let url = new URL(window.location.href);
let page = Number(url.searchParams.get("_page")) || 1;
let posts_per_page = Number(url.searchParams.get("_limit")) || ITEMS_PER_PAGE;

url = new URL("https://jsonplaceholder.typicode.com/posts");
url.searchParams.set("_page", page);
url.searchParams.set("_limit", posts_per_page);
url.searchParams.set("_expand", "user");

get({
    method: "GET",
    url: url,
})
    .then((result) => {
        let { data: posts, headers } = result;
        let total = Math.ceil(headers["x-total-count"] / posts_per_page);

        posts.forEach((post) => {
            listPosts.insertAdjacentHTML(
                "beforeend",
                createPost(post, post.user)
            );
        });

        pagination.appendChild(
            createPagination(total, page, `?_limit=${posts_per_page}&_page=`)
        );

        spinner.remove();
    })
    .catch((e) => console.log(e));
