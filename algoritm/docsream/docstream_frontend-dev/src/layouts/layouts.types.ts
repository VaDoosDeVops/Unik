export enum AppLayoutsEnum {
  default = 'default',
  main = 'main',
}

export const AppLayoutToFileMap: Record<AppLayoutsEnum, string> = {
  default: 'DefaultLayout.vue',
  main: 'MainLayout.vue',
};
