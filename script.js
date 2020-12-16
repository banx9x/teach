// Viết chương trình cho phép nhập vào chiều dài, chiều rộng của hình chữ nhật, tính và in ra chu vi, diện tích của hình chữ nhật

let w = +prompt("Chiều rộng");
let h = +prompt("Chiều cao");

let perimeter = 2 * (w + h);
let area = w * h;

console.log(`Chiều rộng: ${w}`);
console.log(`Chiều dài: ${h}`);
console.log(`Chu vi hình chữ nhật là: ${perimeter}`);

console.log(`Diện tích hình chữ nhật là: ${area}`);

// Viết chương trình cho phép nhập vào bán kính hình tròn, tính và in ra chu vi, diện tích của hình tròn

let r = +prompt("Bán kính hình tròn");

let perimeter = 2 * 3.14 * r;
let area = 3.14 * r ** 2;

console.log(`Bán kính: ${r}`);
console.log(`Chu vi hình tròn là: ${perimeter}`);
console.log(`Diện tích hình tròn là: ${area}`);

// Viết chương trình cho phép nhập vào hệ số a, b của phương trình bậc nhất ax + b = 0, tính và in ra nghiệm của phương trình

let a = +prompt("Hệ số a");
let b = +prompt("Hệ số b");

let x = -b / a;

console.log(`Nghiệm phương trình ${a}x + ${b} là: ${x}`);

// Viết chương trình cho phép nhập vào một số là đơn vị cm, tính và in ra giá trị tương ứng ở các đơn vị mm, m, km

let cm = +prompt("Nhập số cm");

let mm = cm * 10;
let dm = cm / 10;
let m = cm / 100;
let km = cm / 100000;

console.log(`Số cm: ${cm}`);
console.log(`Số mm tương ứng: ${mm}`);
console.log(`Số dm tương ứng: ${dm}`);
console.log(`Số m tương ứng: ${m}`);
console.log(`Số km tương ứng: ${km}`);

// Viết chương trình cho phép nhập vào một số là nhiệt độ có đơn vị Celsius, in ra nhiệt độ ở đơn vị Fahrenheit và Kevin tương ứng

let celsius = +prompt("Nhiệt độ Celsius");

let fahrenheit = (9 / 5) * celsius + 32;
let kevin = celsius + 273.15;

console.log(`Nhiệt độ Celsius: ${celsius}`);
console.log(`Nhiệt độ Farenheit tương ứng: ${fahrenheit}`);
console.log(`Nhiệt độ Kevin tương ứng: ${kevin}`);

// Viết chương trình cho phép nhập một số phút tính từ 0h, tính và in ra giờ/phút tương ứng

let minutes = +prompt("Nhập số phút (tính từ 0h)");

console.log(`Số phút: ${minutes}`);

let hours = minutes / 60 - ((minutes / 60) % 1);
minutes -= hours * 60;

console.log(`${hours}h:${minutes}p`);

// Viết chương trình cho phép nhập ba số, kiểm tra và in ra số lớn nhất

let n1 = +prompt("Nhập số thứ nhất");
let n2 = +prompt("Nhập số thứ 2");
let n3 = +prompt("Nhập số thứ 3");

if (isNaN(n1) || isNaN(n2) || isNaN(n3)) {
  console.log("Vui lòng nhập một số hợp lệ! 😒");
} else if (n1 >= n2 && n1 >= n3) {
  console.log(`Số lớn nhất là: ${n1}`);
} else if (n2 >= n1 && n2 >= n3) {
  console.log(`Số lớn nhất là: ${n2}`);
} else {
  console.log(`Số lớn nhất là: ${n3}`);
}

// Viết chương trình cho phép nhập một số, kiểm tra và in ra số đó có chia hết cho 5 và 11 hay không

let n = +prompt("Nhập một số");

if (isNaN(n)) {
  console.log("Vui lòng nhập một số hợp lệ! 😒");
} else if (n % 5 == 0 && n % 11 == 0) {
  console.log(`${n} chia hết cho 5 và 11`);
} else {
  console.log(`${n} không chia hết cho 5 và 11`);
}

// Viết chương trình cho phép nhập một năm, kiểm tra và in ra năm đó có phải năm nhuận hay không

let year = +prompt("Nhập một năm");

if (isNaN(year)) {
  console.log("Vui lòng nhập một năm hợp lệ! 😒");
} else if (year % 100 == 0 && year % 400 != 0) {
  console.log(`${year} không phải năm nhuận`);
} else if (year % 4 == 0) {
  console.log(`${year} là năm nhuận`);
} else {
  console.log(`${year} không phải năm nhuận`);
}

// Viết chương trình cho phép nhập một ký tự, kiểm tra và in ra ký tự đó có thuộc bảng ký tự alphabe (a-zA-Z) hay không

let char = prompt("Nhập ký tự");

if ((char >= "a" && char <= "z") || (char >= "A" && char <= "Z")) {
  console.log(`${char} thuộc bảng ký tự alphabe`);
} else {
  console.log(`${char} không thuộc bảng ký tự alphabe 😒`);
}

// Viết chương trình cho phép nhập một ký tự, kiểm tra và in ra ký tự đó là nguyên hay phụ âm (tiếng Anh)

let char = prompt("Nhập ký tự");

if (char < "A" || (char > "Z" && char < "a") || char > "z") {
  console.log(`${char} chả phải nguyên âm cũng chả phải phụ âm 😒`);
} else {
  switch (char) {
    case "a":
    case "o":
    case "e":
    case "i":
    case "u":
    case "A":
    case "O":
    case "E":
    case "I":
    case "U":
      console.log(`${char} là nguyên âm`);
      break;

    default:
      console.log(`${char} là phụ âm`);
      break;
  }
}

// Viết chương trình cho phép nhập một ký tự, kiểm tra và in ra ký tự đó là chữ thường hay chữ in hoa

let char = prompt("Nhập ký tự");

if (char >= "a" && char <= "z") {
  console.log(`${char} là chữ in thường`);
} else if (char >= "A" && char <= "Z") {
  console.log(`${char} là chữ in hoa`);
} else {
  console.log(`${char} chả phải in thường cũng chả phải in hoa 😒`);
}

// Viết chương trình cho phép nhập ba hệ số a, b, c, của phương trình bậc 2 ax2 + bx + c = 0, tính và in ra nghiệm phương trình

let a = +prompt("Nhập hệ số a");
let b = +prompt("Nhập hệ số b");
let c = +prompt("Nhập hệ số c");

if (isNaN(a) || isNaN(b) || isNaN(c)) {
  console.log("Vui lòng nhập hệ số phù hợp 😒");
} else if (a == 0) {
  console.log("Hệ số a phải khác 0 😒");
} else {
  let delta = b ** 2 - 4 * a * c;

  if (delta < 0) {
    console.log("Phương trình vô nghiệm");
  } else if (delta == 0) {
    console.log(`Phương trình có nghiệm kép ${-b / (2 * a)}`);
  } else {
    let x1 = (-b + Math.sqrt(delta)) / (2 * a);
    let x2 = (-b - Math.sqrt(delta)) / (2 * a);

    console.log(`Phương trình có 2 nghiệm phân biệt x1 = ${x1}, x2 = ${x2}`);
  }
}

// Viết chương trình quy đổi điểm hệ số 10, sang điểm hệ chữ cho sinh viên, với điểm =< 10 là A, < 8.5 là B, < 7.0 là C, < 5.5 là D, < 4.0 là F

let mark = +prompt("Nhập điểm số");

if (isNaN(mark) || mark < 0 || mark > 10) {
  console.log("Vui lòng nhập điểm phù hợp 😒");
} else if (mark < 4) {
  console.log(`${mark} tương đương điểm: F`);
} else if (mark < 5.5) {
  console.log(`${mark} tương đương điểm: D`);
} else if (mark < 7) {
  console.log(`${mark} tương đương điểm: C`);
} else if (mark < 8.5) {
  console.log(`${mark} tương đương điểm: B`);
} else {
  console.log(`${mark} tương đương điểm: A`);
}
