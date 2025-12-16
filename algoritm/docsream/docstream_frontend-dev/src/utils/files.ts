import PdfIcon from '@/components/icons/PdfIcon.vue';
import WordIcon from '@/components/icons/WordIcon.vue';
import XlsxIcon from '@/components/icons/XlsxIcon.vue';
import RtfIcon from '@/components/icons/RtfIcon.vue';

export const getTypeFile = (fileName: string) => {
  // eslint-disable-next-line no-param-reassign
  if (fileName) {
    fileName = fileName.toLowerCase();
    const lastDotIndex = fileName.lastIndexOf('.');
    if (lastDotIndex === -1) {
      return fileName;
    }
    return fileName.substring(lastDotIndex + 1);
  }
  return 'false';
};
export const getNameFile = (fileName: string) => {
  // eslint-disable-next-line no-param-reassign
  fileName = fileName.toLowerCase();
  const lastDotIndex = fileName.lastIndexOf('.');
  if (lastDotIndex === -1) {
    return fileName;
  }
  return fileName.substring(0, lastDotIndex);
};
export const documentIcons = [{
  icon: PdfIcon,
  type: ['pdf'],
}, {
  icon: WordIcon,
  type: ['doc', 'docx'],
}, {
  type: ['xlsx', 'xls'],
  icon: XlsxIcon,
}, { type: ['rtf'], icon: RtfIcon }];

export const styleMap = [
  // "p[style-name='Heading 1'] => h1:fresh",
  // "p[style-name='Heading 2'] => h2:fresh",
  // "p[style-name='Heading 3'] => h3:fresh",
  // "p[style-name='Heading 4'] => h4:fresh",
  // "p[style-name='Heading 5'] => h5:fresh",
  // "p[style-name='Heading 6'] => h6:fresh",
  "p[style-name='Normal'] => p.normal",
  // "p[style-name='Subtitle'] => h2.subtitle",
  'b => strong',
  "highlight[color='yellow'] => mark.yellow-highlight",
  "highlight[color='green'] => mark.green-highlight",
  "highlight[color='red'] => mark.red-highlight",
  "br[type='page'] => hr.page-break",
  'i => em',
  'u => u',
  'strike => s',
  'b => em',
  "p[style-name='List Paragraph'] => ul > li:fresh",
  "p[style-name='Bullet List'] => ul > li:fresh",
  "p[style-name='Numbered List'] => ol > li:fresh",
  "p[style-name='Quote'] => blockquote:fresh",
  "r[style-name='Hyperlink'] => a",
  'table => table',
  'tr => tr',
  'td => td',
  'th => th',
  "p[style-name='Table Heading'] => th:fresh",
  "r[style-name='Superscript'] => sup",
  "r[style-name='Subscript'] => sub",
  "p[style-name='Code'] => pre:fresh",
  "r[style-name='Code'] => code",
  "p[alignment='center'] => p.text-center",
  "p[align='right'] => p.text-right",
  "p[style-name='Centered Text'] => p.text-center",
  "p[style-name='left-aligned'] => p.left-aligned:fresh",
  "p[style-name='center-aligned'] => p.center-aligned:fresh",
  "p[style-name='right-aligned'] => p.right-aligned:fresh",
  "br[type='line'] => br",
];
