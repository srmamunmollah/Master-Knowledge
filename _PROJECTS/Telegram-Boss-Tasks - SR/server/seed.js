require('dotenv').config();
const { insertTask, listTasks } = require('./db');

const sampleMessages = [
  'Please prepare the Q3 report by Friday',
  'Call the vendor about the delayed shipment',
  'Review the new hire contract before Monday',
];

for (const [i, text] of sampleMessages.entries()) {
  insertTask({
    messageText: text,
    createdAt: new Date().toISOString(),
    telegramMessageId: null,
    // Negative fake ids so they never collide with real Telegram update_ids (always positive).
    telegramUpdateId: -(i + 1),
  });
}

console.log(`Seeded ${sampleMessages.length} placeholder tasks.`);
console.log(listTasks());
