export default function handler(req, res) {
    const USER_ID = "john_doe_17091999";
    const EMAIL = "john@xyz.com";
    const ROLL_NUMBER = "ABCD123";

    if (req.method === 'POST') {
        const { data } = req.body;
        const numbers = [];
        const alphabets = [];
        const highest_alphabet = [];

        for (const item of data) {
            if (!isNaN(item)) {
                numbers.push(item);
            } else if (item.length === 1 && /^[a-zA-Z]$/.test(item)) {
                alphabets.push(item);
            }
        }

        if (alphabets.length > 0) {
            const highestChar = alphabets.reduce((a, b) => a.toUpperCase() > b.toUpperCase() ? a : b);
            highest_alphabet.push(highestChar);
        }

        res.status(200).json({
            is_success: true,
            user_id: USER_ID,
            email: EMAIL,
            roll_number: ROLL_NUMBER,
            numbers: numbers,
            alphabets: alphabets,
            highest_alphabet: highest_alphabet,
        });
    } else if (req.method === 'GET') {
        res.status(200).json({ operation_code: 1 });
    } else {
        res.setHeader('Allow', ['GET', 'POST']);
        res.status(405).end(Method ${req.method} Not Allowed);
    }
}
