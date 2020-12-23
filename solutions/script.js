// Viết hàm random(a-b)
// Arrow function syntax
let random = (a, b) => Math.floor(Math.random() * (b - a)) + a;

// Declare function syntax
function random(a, b) {
  return Math.floor(Math.random() * (b - a)) + a;
}

// Viết hàm isTrianble(a, b, c)
// Arrow function syntax
let isTriangle = (a, b, c) => a + b > c && b + c > a && a + c > b;

// Declare function syntax
function isTriangle(a, b, c) {
  return a + b > c && b + c > a && a + c > b;
}

// Viết hàm guesNumber()
// Arrow function syntax
let guessNumber = () => {
  let rand = random(1, 11);
  let guess = prompt("Guess a random number between 1 - 10");
  let count = 1;

  while (count < 3 && guess != null && rand != guess) {
    guess = prompt("Wrong!\nGuess another number");
    count++;
  }

  if (rand == guess) {
    console.log("Â mây zing gút chóp");
  } else if (count == 3) {
    console.log("You guessed too much wrong");
  } else {
    console.log("Quit game");
  }
};

// Declare function syntax
function guessNumber() {
  let rand = random(1, 11);
  let guess = prompt("Guess a random number between 1 - 10");
  let count = 1;

  while (count < 3 && guess != null && rand != guess) {
    guess = prompt("Wrong!\nGuess another number");
    count++;
  }

  if (rand == guess) {
    console.log("Â mây zing gút chóp");
  } else if (count == 3) {
    console.log("You guessed too much wrong");
  } else {
    console.log("Quit game");
  }
}

// Viết hàm nearest(a, b)
// Arrow function syntax
let nearest = (a, b) => {
  let rangeA = a < 100 ? 100 - a : a - 100;
  let rangeB = b < 100 ? 100 - b : b - 100;

  return rangeA < rangeB ? a : b;
};

// Declare function syntax
function nearest(a, b) {
  let rangeA = a < 100 ? 100 - a : a - 100;
  let rangeB = b < 100 ? 100 - b : b - 100;

  return rangeA < rangeB ? a : b;
}

// Viết hàm isSequense(a, b, c)
// Arrow function syntax
let isSequense = (a, b, c) => (a > b && b > c) || (a < b && b < c);

// Declare function syntax
function isSequense(a, b, c) {
  return (a > b && b > c) || (a < b && b < c);
}

// Viết hàm countDecimal(n)
// Arrow function syntax
let countDecimal = (n) => {
  let str = n.toString().split(".");

  return str.length == 1 ? 0 : str[1].length;
};

// Declare function syntax
function countDecimal(n) {
  let str = n.toString().split(".");

  return str.length == 1 ? 0 : str[1].length;
}

// Viết hàm isAscending(n)
// Arrow function syntax
let isAscending = (n) => {
  let temp, rem;
  while (n > 10) {
    rem = n % 10;
    n = (n - (n % 10)) / 10;

    if (rem <= n % 10) {
      return false;
    }
  }
  return true;
};

// Declare function syntax
function isAscending(n) {
  let temp, rem;
  while (n > 10) {
    rem = n % 10;
    n = (n - (n % 10)) / 10;

    if (rem <= n % 10) {
      return false;
    }
  }
  return true;
}

// Viết hàm countEven(n)
// Arrow function syntax
let countEven = (n) => {
  let rem;
  let count = 0;
  while (n > 1) {
    rem = n % 10;

    if (rem % 2 == 0) {
      count++;
    }

    n = (n - (n % 10)) / 10;
  }

  return count;
};

// Declare function syntax
function countEven(n) {
  let rem;
  let count = 0;
  while (n > 1) {
    rem = n % 10;

    if (rem % 2 == 0) {
      count++;
    }

    n = (n - (n % 10)) / 10;
  }

  return count;
}

// Viết hàm find(n)
// Arrow function syntax
let find = (n) => {
  let sum = 0;

  for (let i = 0; ; i++) {
    sum += i;

    if (sum == n) {
      return i;
    }

    if (sum > n) {
      return i - 1;
    }
  }
};

// Declare function syntax
function find(n) {
  let sum = 0;

  for (let i = 0; ; i++) {
    sum += i;

    if (sum == n) {
      return i;
    }

    if (sum > n) {
      return i - 1;
    }
  }
}

// Viết hàm sum(val1, unit1, val2, unit2)
let _km = (value, from) => {
  switch (from) {
    case "km":
      return value;
    case "m":
      return value * 0.001;
    case "dm":
      return value * 0.0001;
    case "cm":
      return value * 0.00001;
    case "mm":
      return value * 0.000001;
    default:
      return NaN;
  }
};

// Arrow function syntax
let sum = (val1, unit1, val2, unit2) => {
  let result;
  switch (unit1) {
    case "km":
      result = _km(val1, unit1) + _km(val2, unit2);
      return result;
    case "m":
      result = _km(val1, unit1) + _km(val2, unit2);
      return result * 1000;
    case "dm":
      result = _km(val1, unit1) + _km(val2, unit2);
      return result * 10000;
    case "cm":
      result = _km(val1, unit1) + _km(val2, unit2);
      return result * 100000;
    case "mm":
      result = _km(val1, unit1) + _km(val2, unit2);
      return result * 1000000;
    default:
      return NaN;
  }
};

// Declare function syntax
function sum(val1, unit1, val2, unit2) {
  let result;
  switch (unit1) {
    case "km":
      result = _km(val1, unit1) + _km(val2, unit2);
      return result;
    case "m":
      result = _km(val1, unit1) + _km(val2, unit2);
      return result * 10 ** 2;
    case "dm":
      result = _km(val1, unit1) + _km(val2, unit2);
      return result * 10 ** 3;
    case "cm":
      result = _km(val1, unit1) + _km(val2, unit2);
      return result * 10 ** 4;
    case "mm":
      result = _km(val1, unit1) + _km(val2, unit2);
      return result * 10 ** 5;
    default:
      return NaN;
  }
}
