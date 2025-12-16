export const EMAIL_REGEXP = /^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/iu;

export function isEmailValid(value: string) {
  return EMAIL_REGEXP.test(value);
}

export function validateEmail(email: string): string {
  if (email.length === 0) {
    return 'Email не указан';
  }
  if (!isEmailValid(email)) {
    return 'Некорректный формат email';
  }
  return '';
}

export function isNotEmpty(value: string, message = 'Пустое поле'): string {
  if (value.length === 0) {
    return message;
  }
  return '';
}
