create database finance_nifty50;
use finance_nifty50;

drop table Companies;
drop table StockPrices;

CREATE TABLE Companies (
    CompanyID VARCHAR(255) PRIMARY KEY,
    Name VARCHAR(255),
    Symbol VARCHAR(255),
    INDEX idx_symbol (Symbol)
);

CREATE TABLE StockPrices (
    Date DATE,
    Open FLOAT,
    High FLOAT,
    Low FLOAT,
    Close FLOAT,
    Adj_Close FLOAT,
    Volume BIGINT,
    Symbol VARCHAR(255),
    FOREIGN KEY (Symbol) REFERENCES Companies(Symbol)
);

drop table Companies;
drop table StockPrices;

select * from Companies;
select * from StockPrices;

SHOW COLUMNS FROM Companies;


SHOW TABLES IN finance_nifty50;

