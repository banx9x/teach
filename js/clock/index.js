import Clock from "./clock.js";

let clock = document.getElementById("clock");
let start = document.getElementById("start");
let record = document.getElementById("record");
let stop = document.getElementById("stop");
let reset = document.getElementById("reset");
let records = document.getElementById("records");

new Clock(clock, start, record, stop, reset, records);
