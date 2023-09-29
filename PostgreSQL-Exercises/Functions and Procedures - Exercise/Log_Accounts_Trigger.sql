-- Create the "logs" table
CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    account_id INT NOT NULL,
    old_sum NUMERIC NOT NULL,
    new_sum NUMERIC NOT NULL
);

-- Create the trigger function
CREATE OR REPLACE FUNCTION trigger_fn_insert_new_entry_into_logs() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO logs (account_id, old_sum, new_sum)
    VALUES (
        OLD.id,
        OLD.balance,
        NEW.balance
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
-- Create the trigger "account_balance_change"
CREATE TRIGGER account_balance_change
AFTER UPDATE ON accounts
FOR EACH ROW
WHEN (OLD.balance != NEW.balance)
EXECUTE FUNCTION trigger_fn_insert_new_entry_into_logs();