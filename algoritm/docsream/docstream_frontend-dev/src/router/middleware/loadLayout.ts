import type { RouteLocationNormalized } from 'vue-router';
import { AppLayoutsEnum, AppLayoutToFileMap } from '@/layouts/layouts.types';

export default async function loadLayoutMiddleware(
  route: RouteLocationNormalized,
): Promise<void> {
  const routeCopy = { ...route };
  const layout = routeCopy.meta.layout as AppLayoutsEnum | undefined;
  const normalizedLayoutName: AppLayoutsEnum = layout || AppLayoutsEnum.default;
  const fileName = AppLayoutToFileMap[normalizedLayoutName];
  const fileNameWithoutExtension = fileName.split('.vue')[0];
  const component = await import(`@/layouts/${fileNameWithoutExtension}.vue`);
  routeCopy.meta.layoutComponent = component.default;
}
