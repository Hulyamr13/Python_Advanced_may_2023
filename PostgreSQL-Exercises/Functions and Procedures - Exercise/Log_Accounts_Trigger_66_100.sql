CREATE TABLE IF NOT EXISTS logs (
  log_id SERIAL PRIMARY KEY,
  account_id INT NOT NULL,
  old_sum DECIMAL(19, 4) NOT NULL,
  new_sum DECIMAL(19, 4) NOT NULL
);


CREATE OR REPLACE FUNCTION trigger_fn_insert_new_entry_into_logs()
RETURNS TRIGGER AS $$
BEGIN
  IF OLD.balance <> NEW.balance THEN
    INSERT INTO logs (account_id, old_sum, new_sum)
    VALUES (OLD.id, OLD.balance, NEW.balance);
  END IF;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER account_balance_change
AFTER UPDATE ON accounts
FOR EACH ROW
EXECUTE FUNCTION trigger_fn_insert_new_entry_into_logs();
