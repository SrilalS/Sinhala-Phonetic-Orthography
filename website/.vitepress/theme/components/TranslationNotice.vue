<script setup lang="ts">
// Shown above a translated research page: links the English original and warns when the
// original changed after the translation was made (see transformPageData in config.mts).
import { computed } from "vue";
import { useData, withBase } from "vitepress";

const { frontmatter } = useData();
const tr = computed(() => frontmatter.value.translation as { original: string; stale: boolean } | undefined);
</script>

<template>
  <div v-if="tr" class="tr-notice" :class="{ stale: tr.stale }">
    <template v-if="tr.stale">
      ⚠️ මෙම පරිවර්තනය කළ පසු ඉංග්‍රීසි මුල් ලේඛනය යාවත්කාලීන වී ඇත. නවතම අන්තර්ගතය සඳහා
      <a :href="withBase(tr.original)">ඉංග්‍රීසි පිටපත</a> බලන්න.
    </template>
    <template v-else>
      මෙය ඉංග්‍රීසි මුල් ලේඛනයේ පරිවර්තනයකි. දෙකෙහි වෙනසක් ඇත්නම්
      <a :href="withBase(tr.original)">ඉංග්‍රීසි පිටපත</a> නිවැරදි යැයි සලකන්න.
    </template>
  </div>
</template>

<style scoped>
.tr-notice { font-size: 13px; line-height: 1.6; color: var(--vp-c-text-2); background: var(--vp-c-bg-soft); border: 1px solid var(--vp-c-divider); border-radius: 8px; padding: 8px 14px; margin-bottom: 24px; }
.tr-notice a { color: var(--vp-c-brand-1); text-decoration: underline; text-underline-offset: 2px; }
.tr-notice.stale { color: var(--vp-c-text-1); background: var(--st-rare-bg); border-color: var(--st-rare); }
</style>
