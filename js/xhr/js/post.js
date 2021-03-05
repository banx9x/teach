import get, { loading, createPostDetail, createComment } from "./util.js";

const postContent = document.getElementById("post-content");
const postComment = document.getElementById("post-comment");

const spinner = loading();

let postUrl = new URL(window.location.href);
let id = postUrl.searchParams.get("id");

postUrl = new URL("https://jsonplaceholder.typicode.com/posts/" + id);
postUrl.searchParams.set("_embed", "comments");

get({
    method: "GET",
    url: postUrl,
})
    .then((result) => {
        let post = result.data;

        document.title = post.title;
        postContent.insertAdjacentHTML("afterbegin", createPostDetail(post));
        post.comments.forEach((comment) =>
            postComment.insertAdjacentHTML("beforeend", createComment(comment))
        );

        spinner.remove();
    })
    .catch((e) => console.log(e));
