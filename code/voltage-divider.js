/* jshint esversion: 6 */

// calculate resistors for a voltage divider
const R1 = 1200;        // Your current resistor (alter this)
const Vout = 3.3;       // The voltage you are trying to achieve (always 3.3) across the resistor R2
const Vin = 5;          // The input voltage (always 5)

const R2 = (Vout * R1) / (Vin - Vout);

console.log(`The resistor you need is approximately ${R2}`);
