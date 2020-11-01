-- Drop any pre-existing tables from earlier experiments
DROP TABLE IF EXISTS transaction;
DROP TABLE IF EXISTS credit_card;
DROP TABLE IF EXISTS card_holder;
DROP TABLE IF EXISTS merchant;
DROP TABLE IF EXISTS merchant_category;

-- Create the table "card_holder"
CREATE TABLE card_holder (
  id INT,
  name VARCHAR(255),
  PRIMARY KEY (id)
);

-- Create the table "credit_card"
CREATE TABLE credit_card (
  card VARCHAR(255),
  id_card_holder INT,
  PRIMARY KEY (card),
  FOREIGN KEY (id_card_holder) REFERENCES card_holder(id)
);

-- Create the table "merchant_category"
CREATE TABLE merchant_category (
  id INT,
  name VARCHAR(255),
  PRIMARY KEY (id)
);

-- Create the table "merchant"
CREATE TABLE merchant (
  id INT,
  name VARCHAR(255),
  id_merchant_category INT,
  PRIMARY KEY (id),
  FOREIGN KEY (id_merchant_category) REFERENCES merchant_category(id)
);

-- Create the table "transaction"
CREATE TABLE transaction (
  id INT NOT NULL,
  date TIMESTAMP,
  amount FLOAT,
  card VARCHAR(255),
  merchant INT,
  PRIMARY KEY (id),
  FOREIGN KEY (card) REFERENCES credit_card(card),
  FOREIGN KEY (merchant) REFERENCES merchant(id)
);