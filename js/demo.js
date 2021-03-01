
function asynchronous(callback) {
    console.log("I'm doing my job");
    callback();
}

asynchronous(() => {
    asynchronous(() => {
        asynchronous(() => {
            asynchronous(() => {
                asynchronous(() => {
                    asynchronous(() => {
                        // lol
                    })
                })
            })
        })
    })
});

