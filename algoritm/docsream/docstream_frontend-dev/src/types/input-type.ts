export interface Config {
  type?: 'text' | 'search' | 'hidden' | 'email' | 'tel' | 'url' | 'number' | 'password' | undefined,
  inputmode?: 'text' | 'search' | 'none' | 'email' | 'tel' | 'url' | 'numeric' | 'decimal' | undefined,
  placeholder: string | null,
  staticPlaceholder?: string | undefined,
  maxlength?: string | number,
  autocomplete?: 'on' | 'off' | 'honorific-prefix' | 'given-name' | 'additional-name' | 'family-name' | 'honorific-suffix' | 'nickname' | 'email' | 'username' | 'new-password' | 'current-password' | 'one-time-code' | 'organization-title' | 'organization' | 'street-address' | 'shipping' | 'billing' | 'address-line1' | 'address-line2' | 'address-line3' | 'address-level4' | 'address-level3' | 'address-level2' | 'address-level1' | 'country' | 'country-name' | 'postal-code' | 'cc-name' | 'cc-given-name' | 'cc-additional-name' | 'cc-family-name' | 'cc-number' | 'cc-exp' | 'cc-exp-month' | 'cc-exp-year' | 'cc-csc' | 'cc-type' | 'transaction-currency' | 'transaction-amount' | 'language' | 'bday' | 'bday-day' | 'bday-month' | 'bday-year' | 'sex' | 'tel' | 'tel-country-code' | 'tel-national' | 'tel-area-code' | 'tel-local' | 'tel-extension' | 'impp' | 'url' | 'photo' | 'webauthn',
  mask?: string | undefined,
  mustFilled?: boolean | undefined,
  autoFocus?: boolean,
  readonly?: boolean,
  ta?: boolean,
  theme?: 'white' | 'gray',
  small?: boolean,
}

export interface Error {
  code: string | number,
  exist: boolean,
  text: string
}
