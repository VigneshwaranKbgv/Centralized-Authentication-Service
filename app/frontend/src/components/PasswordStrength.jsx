const PasswordStrength = ({ password }) => {
  const strength = calculateStrength(password);
  return (
    <div className="password-strength">
      <div className={`strength-bar ${strength}`} />
      <span>{strength} password</span>
    </div>
  );
}; 