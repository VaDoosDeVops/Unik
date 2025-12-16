export const allowedTypes = [
  'application/msword',
  'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  'application/rtf',
  'application/pdf',
  'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  'application/vnd.ms-excel',
];
export const fileResolution = [
  {
    type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    resolution: 'docx',
  }, {
    type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    resolution: 'xlsx',
  },
  {
    type: 'application/pdf',
    resolution: 'pdf',
  },
  {
    type: 'application/rtf',
    resolution: 'rtf',
  },
  {
    type: 'application/msword',
    resolution: 'doc',
  },
  {
    type: 'application/vnd.ms-excel',
    resolution: 'xls',
  },
];
export const allowedSeparate = [['xls', 'xlsx'], ['pdf', 'doc', 'docx', 'rtf']];

export enum DifferenceType {
  DELETED,
  CHANGED,
  ADDED,
}
