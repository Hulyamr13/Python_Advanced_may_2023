-- Create the "logs" table
CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    account_id INT,
    old_sum NUMERIC,
    new_sum NUMERIC
);

-- Create the trigger function
CREATE OR REPLACE FUNCTION trigger_fn_insert_new_entry_into_logs()
RETURNS TRIGGER AS $$
BEGIN
    -- Insert a new row into the "logs" table with the required values
    INSERT INTO logs (account_id, old_sum, new_sum)
    VALUES (OLD.id, OLD.balance, NEW.balance);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create the trigger "account_balance_change"
CREATE TRIGGER tr_account_balance_change
AFTER UPDATE OF balance ON accounts
FOR EACH ROW
WHEN (OLD.balance IS DISTINCT FROM NEW.balance)
EXECUTE FUNCTION trigger_fn_insert_new_entry_into_logs();
