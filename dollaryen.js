
const dollarrate = 109;

const dollaryen = (name, price)=>{
  
  console.log(`${name}は、${price}ドル`);

  price = price * dollarrate;

  console.log(`${price}円です。`);

  console.log("----------------------");

}

dollaryen("花", 2);
dollaryen("水", 1);
