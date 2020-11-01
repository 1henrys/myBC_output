-- first attempt
SELECT 
    t.id,
    t.date,
    t.amount,
    t.card
FROM transaction AS t 
INNER JOIN credit_card AS cc ON t.card = cc.card
WHERE 
    cc.id_card_holder = 2 
    OR
    cc.id_card_holder = 18
GROUP BY cc.id_card_holder
ORDER BY t.date ASC;


-- another approach
SELECT * FROM transaction AS trans
INNER JOIN credit_card AS cc ON trans.card = cc.card
WHERE 
    cc.id_card_holder = 2
    OR
    cc.id_card_holder = 18
ORDER BY trans.date ASC; 

-- final for question 1
SELECT 
    trans.date,
    trans.amount,
    cc.id_card_holder
FROM transaction AS trans
INNER JOIN credit_card AS cc ON trans.card = cc.card
WHERE 
    cc.id_card_holder = 2
    OR
    cc.id_card_holder = 18
ORDER BY trans.date ASC; 


-- final for question 2
SELECT 
    date_part('month',trans.date) AS month,
    date_part('day',trans.date) AS day,
    trans.amount
FROM transaction AS trans
JOIN credit_card AS cc ON trans.card = cc.card
WHERE 
    cc.id_card_holder = 25
    AND
    date_part('month',trans.date) <= 6
ORDER BY month, day ASC; 
