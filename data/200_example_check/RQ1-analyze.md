### 1.Correct
link: https://github.com/apache/dolphinscheduler/commit/ba5de75829f63f0816c9bf4fee7f7e1af4db6fa2
p_path: dolphinscheduler-master/src/main/java/org/apache/dolphinscheduler/server/master/runner/task/dynamic/DynamicCommandUtils.java#createCommand
t_path: dolphinscheduler-master/src/test/java/org/apache/dolphinscheduler/server/master/runner/task/dynamic/DynamicCommandUtilsTest.java#testCreateCommand

````java:test_src

@Test
void testCreateCommand() {
    Command command = DynamicCommandUtils.createCommand(processInstance, subProcessDefinitionCode, subProcessDefinitionVersion, parameters);
    Assertions.assertEquals(CommandType.DYNAMIC_GENERATION, command.getCommandType());
    Assertions.assertEquals(subProcessDefinitionCode, command.getProcessDefinitionCode());
    Assertions.assertEquals(subProcessDefinitionVersion, command.getProcessDefinitionVersion());
    Assertions.assertEquals(TaskDependType.TASK_POST, command.getTaskDependType());
    Assertions.assertEquals(processInstance.getFailureStrategy(), command.getFailureStrategy());
    Assertions.assertEquals(processInstance.getWarningType(), command.getWarningType());
    Assertions.assertEquals(processInstance.getExecutorId(), command.getExecutorId());
    Assertions.assertEquals(processInstance.getWarningGroupId(), command.getWarningGroupId());
    Assertions.assertEquals(processInstance.getProcessInstancePriority(), command.getProcessInstancePriority());
    Assertions.assertEquals(processInstance.getWorkerGroup(), command.getWorkerGroup());
    Assertions.assertEquals(processInstance.getDryRun(), command.getDryRun());
}

```java:test_tgt

@Test
void testCreateCommand() {
    Command command = DynamicCommandUtils.createCommand(processInstance, subProcessDefinitionCode, subProcessDefinitionVersion, parameters);
    Assertions.assertEquals(CommandType.DYNAMIC_GENERATION, command.getCommandType());
    Assertions.assertEquals(subProcessDefinitionCode, command.getProcessDefinitionCode());
    Assertions.assertEquals(subProcessDefinitionVersion, command.getProcessDefinitionVersion());
    Assertions.assertEquals(TaskDependType.TASK_POST, command.getTaskDependType());
    Assertions.assertEquals(processInstance.getFailureStrategy(), command.getFailureStrategy());
    Assertions.assertEquals(processInstance.getWarningType(), command.getWarningType());
    Assertions.assertEquals(processInstance.getExecutorId(), command.getExecutorId());
    Assertions.assertEquals(processInstance.getWarningGroupId(), command.getWarningGroupId());
    Assertions.assertEquals(processInstance.getProcessInstancePriority(), command.getProcessInstancePriority());
    Assertions.assertEquals(processInstance.getWorkerGroup(), command.getWorkerGroup());
    Assertions.assertEquals(processInstance.getDryRun(), command.getDryRun());
    Assertions.assertEquals(processInstance.getTenantCode(), command.getTenantCode());
}

```java:llm_gen

@Test
void testCreateCommand() {
    Command command = DynamicCommandUtils.createCommand(processInstance, subProcessDefinitionCode, subProcessDefinitionVersion, parameters);
    Assertions.assertEquals(CommandType.DYNAMIC_GENERATION, command.getCommandType());
    Assertions.assertEquals(subProcessDefinitionCode, command.getProcessDefinitionCode());
    Assertions.assertEquals(subProcessDefinitionVersion, command.getProcessDefinitionVersion());
    Assertions.assertEquals(TaskDependType.TASK_POST, command.getTaskDependType());
    Assertions.assertEquals(processInstance.getFailureStrategy(), command.getFailureStrategy());
    Assertions.assertEquals(processInstance.getWarningType(), command.getWarningType());
    Assertions.assertEquals(processInstance.getExecutorId(), command.getExecutorId());
    Assertions.assertEquals(processInstance.getWarningGroupId(), command.getWarningGroupId());
    Assertions.assertEquals(processInstance.getProcessInstancePriority(), command.getProcessInstancePriority());
    Assertions.assertEquals(processInstance.getWorkerGroup(), command.getWorkerGroup());
    Assertions.assertEquals(processInstance.getDryRun(), command.getDryRun());
    Assertions.assertEquals(processInstance.getTenantCode(), command.getTenantCode());
}

### 2.Additional Asserts
link: https://github.com/tigase/tigase-server/commit/17772ce43a9080dbd834a39e4a79d80367409724
p_path: src/main/java/tigase/eventbus/impl/EventBusSerializer.java#deserialize
t_path: src/test/java/tigase/eventbus/impl/EventBusSerializerTest.java#testDeserialize

```java:test_src

@Test
public void testDeserialize() {
    EventBusSerializer serializer = new EventBusSerializer();
    Event1 eo = new Event1();
    eo.setJid(JID.jidInstanceNS("a@b.c/d"));
    eo.setTransientField("123");
    eo.setV1("message");
    eo.setV2(9898);
    eo.setElementField(new Element("x", "v", new String[] { "a" }, new String[] { "b" }));
    eo.setStrArrField(new String[] { "ala", "m,a", "kota" });
    eo.setSetField(new HashSet<>(Arrays.asList("test123")));
    Element ex = serializer.serialize(eo);
    Event1 ed = serializer.deserialize(ex);
    Assert.assertNotNull(ed);
    Assert.assertNotSame(eo, ed);
    Assert.assertEquals(JID.jidInstanceNS("a@b.c/d"), ed.getJid());
    Assert.assertNull(ed.getTransientField());
    Assert.assertEquals("message", ed.getV1());
    Assert.assertEquals(9898, ed.getV2());
    Assert.assertEquals(new Element("x", "v", new String[] { "a" }, new String[] { "b" }), ed.getElementField());
    Assert.assertArrayEquals(new String[] { "ala", "m,a", "kota" }, ed.getStrArrField());
    Assert.assertTrue(eo.getSetField().contains("test123"));
}

```java:test_tgt

@Test
public void testDeserialize() {
    EventBusSerializer serializer = new EventBusSerializer();
    Event1 eo = new Event1();
    eo.setJid(JID.jidInstanceNS("a@b.c/d"));
    eo.setTransientField("123");
    eo.setV1("message");
    eo.setV2(9898);
    eo.setElementField(new Element("x", "v", new String[] { "a" }, new String[] { "b" }));
    eo.setStrArrField(new String[] { "ala", "m,a", "kota" });
    eo.setSetField(new HashSet<>(Arrays.asList("test123")));
    Element ex = serializer.serialize(eo);
    Event1 ed = serializer.deserialize(ex);
    assertNotNull(ed);
    Assert.assertNotSame(eo, ed);
    Assert.assertEquals(JID.jidInstanceNS("a@b.c/d"), ed.getJid());
    Assert.assertNull(ed.getTransientField());
    Assert.assertEquals("message", ed.getV1());
    Assert.assertEquals(9898, ed.getV2());
    Assert.assertEquals(new Element("x", "v", new String[] { "a" }, new String[] { "b" }), ed.getElementField());
    Assert.assertArrayEquals(new String[] { "ala", "m,a", "kota" }, ed.getStrArrField());
    Assert.assertTrue(eo.getSetField().contains("test123"));
}

```java:llm_gen

@Test
public void testDeserialize() {
    EventBusSerializer serializer = new EventBusSerializer();
    Event1 eo = new Event1();
    eo.setJid(JID.jidInstanceNS("a@b.c/d"));
    eo.setTransientField("123");
    eo.setV1("message");
    eo.setV2(9898);
    eo.setElementField(new Element("x", "v", new String[] { "a" }, new String[] { "b" }));
    eo.setStrArrField(new String[] { "ala", "m,a", "kota" });
    eo.setSetField(new HashSet<>(Arrays.asList("test123")));
    Element ex = serializer.serialize(eo);
    ex.setAttribute(EventBusSerializer.CLASS_ATTR_NAME, eo.getClass().getName());
    Event1 ed = serializer.deserialize(ex);
    Assert.assertNotNull(ed);
    Assert.assertNotSame(eo, ed);
    Assert.assertEquals(JID.jidInstanceNS("a@b.c/d"), ed.getJid());
    Assert.assertNull(ed.getTransientField());
    Assert.assertEquals("message", ed.getV1());
    Assert.assertEquals(9898, ed.getV2());
    Assert.assertEquals(new Element("x", "v", new String[] { "a" }, new String[] { "b" }), ed.getElementField());
    Assert.assertArrayEquals(new String[] { "ala", "m,a", "kota" }, ed.getStrArrField());
    Assert.assertTrue(eo.getSetField().contains("test123"));
}

### 3.External File Modification
link: https://github.com/apache/commons-collections/commit/56da86956588b45280938180b40eb3aac1d16a86
p_path: src/main/java/org/apache/commons/collections4/bloomfilter/LayerManager.java#builder
t_path: src/test/java/org/apache/commons/collections4/bloomfilter/LayerManagerTest.java#testBuilder

```java:test_src

@Test
public void testBuilder() {
    LayerManager.Builder underTest = LayerManager.builder();
    NullPointerException npe = assertThrows(NullPointerException.class, () -> underTest.build());
    assertTrue(npe.getMessage().contains("Supplier must not be null"));
    underTest.setSupplier(() -> null).setCleanup(null);
    npe = assertThrows(NullPointerException.class, () -> underTest.build());
    assertTrue(npe.getMessage().contains("Cleanup must not be null"));
    underTest.setCleanup(x -> {
    }).setExtendCheck(null);
    npe = assertThrows(NullPointerException.class, () -> underTest.build());
    assertTrue(npe.getMessage().contains("ExtendCheck must not be null"));
    npe = assertThrows(NullPointerException.class, () -> LayerManager.builder().setSupplier(() -> null).build());
    assertTrue(npe.getMessage().contains("filterSupplier returned null."));
}

```java:test_tgt

@Test
public void testBuilder() {
    LayerManager.Builder<BloomFilter> underTest = LayerManager.builder();
    NullPointerException npe = assertThrows(NullPointerException.class, underTest::build);
    assertTrue(npe.getMessage().contains("Supplier must not be null"));
    underTest.setSupplier(() -> null).setCleanup(null);
    npe = assertThrows(NullPointerException.class, underTest::build);
    assertTrue(npe.getMessage().contains("Cleanup must not be null"));
    underTest.setCleanup(x -> {
    }).setExtendCheck(null);
    npe = assertThrows(NullPointerException.class, underTest::build);
    assertTrue(npe.getMessage().contains("ExtendCheck must not be null"));
    npe = assertThrows(NullPointerException.class, () -> LayerManager.builder().setSupplier(() -> null).build());
    assertTrue(npe.getMessage().contains("filterSupplier returned null."));
}

```java:llm_gen

@Test
public void testBuilder() {
    LayerManager.Builder<?> underTest = LayerManager.builder();
    NullPointerException npe = assertThrows(NullPointerException.class, () -> underTest.build());
    assertTrue(npe.getMessage().contains("Supplier must not be null"));
    underTest.setSupplier(() -> null).setCleanup(null);
    npe = assertThrows(NullPointerException.class, () -> underTest.build());
    assertTrue(npe.getMessage().contains("Cleanup must not be null"));
    underTest.setCleanup(x -> {
    }).setExtendCheck(null);
    npe = assertThrows(NullPointerException.class, () -> underTest.build());
    assertTrue(npe.getMessage().contains("ExtendCheck must not be null"));
    npe = assertThrows(NullPointerException.class, () -> LayerManager.builder().setSupplier(() -> null).build());
    assertTrue(npe.getMessage().contains("filterSupplier returned null."));
}

### 4.Correct
link: https://github.com/halo-dev/halo/commit/6a37df07a8b2041e349b29751945c2c6c417b53a
p_path: api/src/main/java/run/halo/app/extension/controller/ControllerBuilder.java#build
t_path: api/src/test/java/run/halo/app/extension/controller/ControllerBuilderTest.java#buildTest

````java:test_src

@Test
void buildTest() {
    assertThrows(IllegalArgumentException.class, () -> new ControllerBuilder(new FakeReconciler(), client).build(), "Extension must not be null");
    assertNotNull(fakeBuilder().build());
    assertNotNull(fakeBuilder().syncAllOnStart(true).nowSupplier(Instant::now).minDelay(Duration.ofMillis(5)).maxDelay(Duration.ofSeconds(1000)).build());
    assertNotNull(fakeBuilder().syncAllOnStart(true).minDelay(Duration.ofMillis(5)).maxDelay(Duration.ofSeconds(1000)).onAddPredicate(Objects::nonNull).onUpdatePredicate(Objects::equals).onDeletePredicate(Objects::nonNull).build());
}

```java:test_tgt

@Test
void buildTest() {
    assertThrows(IllegalArgumentException.class, () -> new ControllerBuilder(new FakeReconciler(), client).build(), "Extension must not be null");
    assertNotNull(fakeBuilder().build());
    assertNotNull(fakeBuilder().syncAllOnStart(true).nowSupplier(Instant::now).minDelay(Duration.ofMillis(5)).maxDelay(Duration.ofSeconds(1000)).build());
    assertNotNull(fakeBuilder().syncAllOnStart(true).minDelay(Duration.ofMillis(5)).maxDelay(Duration.ofSeconds(1000)).onAddMatcher(null).onUpdateMatcher(null).onDeleteMatcher(null).build());
}

```java:llm_gen

@Test
void buildTest() {
    assertThrows(IllegalArgumentException.class, () -> new ControllerBuilder(new FakeReconciler(), client).build(), "Extension must not be null");
    assertNotNull(fakeBuilder().build());
    assertNotNull(fakeBuilder().syncAllOnStart(true).nowSupplier(Instant::now).minDelay(Duration.ofMillis(5)).maxDelay(Duration.ofSeconds(1000)).build());
    assertNotNull(fakeBuilder().syncAllOnStart(true).minDelay(Duration.ofMillis(5)).maxDelay(Duration.ofSeconds(1000)).onAddMatcher(Objects::nonNull).onUpdateMatcher(Objects::equals).onDeleteMatcher(Objects::nonNull).build());
}

### 5.Correct
link: https://github.com/StarRocks/starrocks/commit/952bc956276f35b51e239eaceda8659a2eded4b1
p_path: fe/fe-core/src/main/java/com/starrocks/leader/ReportHandler.java#handleSetPrimaryIndexCacheExpireSec
t_path: fe/fe-core/src/test/java/com/starrocks/leader/ReportHandlerTest.java#testHandleSetPrimaryIndexCacheExpireSec

```java:test_src

@Test
public void testHandleSetPrimaryIndexCacheExpireSec() {
    Database db = GlobalStateMgr.getCurrentState().getDb("test");
    long dbId = db.getId();
    OlapTable olapTable = (OlapTable) db.getTable("primary_index_cache_expire_sec_test");
    long backendId = 10001L;
    List<Long> tabletIds = GlobalStateMgr.getCurrentInvertedIndex().getTabletIdsByBackendId(10001);
    Assert.assertFalse(tabletIds.isEmpty());
    Map<Long, TTablet> backendTablets = new HashMap<Long, TTablet>();
    List<TTabletInfo> tabletInfos = Lists.newArrayList();
    TTablet tablet = new TTablet(tabletInfos);
    for (Long tabletId : tabletIds) {
        TTabletInfo tabletInfo = new TTabletInfo();
        tabletInfo.setTablet_id(tabletId);
        tabletInfo.setSchema_hash(60000);
        tabletInfo.setPrimary_index_cache_expire_sec(7200);
        tablet.tablet_infos.add(tabletInfo);
    }
    backendTablets.put(backendId, tablet);
    ReportHandler handler = new ReportHandler();
    handler.testHandleSetPrimaryIndexCacheExpireSec(backendId, backendTablets);
}

```java:test_tgt

@Test
public void testHandleSetPrimaryIndexCacheExpireSec() {
    Database db = GlobalStateMgr.getCurrentState().getDb("test");
    long dbId = db.getId();
    OlapTable olapTable = (OlapTable) db.getTable("primary_index_cache_expire_sec_test");
    long backendId = 10001L;
    List<Long> tabletIds = GlobalStateMgr.getCurrentState().getTabletInvertedIndex().getTabletIdsByBackendId(10001);
    Assert.assertFalse(tabletIds.isEmpty());
    Map<Long, TTablet> backendTablets = new HashMap<Long, TTablet>();
    List<TTabletInfo> tabletInfos = Lists.newArrayList();
    TTablet tablet = new TTablet(tabletInfos);
    for (Long tabletId : tabletIds) {
        TTabletInfo tabletInfo = new TTabletInfo();
        tabletInfo.setTablet_id(tabletId);
        tabletInfo.setSchema_hash(60000);
        tabletInfo.setPrimary_index_cache_expire_sec(7200);
        tablet.tablet_infos.add(tabletInfo);
    }
    backendTablets.put(backendId, tablet);
    ReportHandler handler = new ReportHandler();
    handler.testHandleSetPrimaryIndexCacheExpireSec(backendId, backendTablets);
}

```java:llm_gen

@Test
public void testHandleSetPrimaryIndexCacheExpireSec() {
    Database db = GlobalStateMgr.getCurrentState().getDb("test");
    long dbId = db.getId();
    OlapTable olapTable = (OlapTable) db.getTable("primary_index_cache_expire_sec_test");
    long backendId = 10001L;
    List<Long> tabletIds = GlobalStateMgr.getCurrentState().getTabletInvertedIndex().getTabletIdsByBackendId(10001);
    Assert.assertFalse(tabletIds.isEmpty());
    Map<Long, TTablet> backendTablets = new HashMap<Long, TTablet>();
    List<TTabletInfo> tabletInfos = Lists.newArrayList();
    TTablet tablet = new TTablet(tabletInfos);
    for (Long tabletId : tabletIds) {
        TTabletInfo tabletInfo = new TTabletInfo();
        tabletInfo.setTablet_id(tabletId);
        tabletInfo.setSchema_hash(60000);
        tabletInfo.setPrimary_index_cache_expire_sec(7200);
        tablet.tablet_infos.add(tabletInfo);
    }
    backendTablets.put(backendId, tablet);
    ReportHandler handler = new ReportHandler();
    handler.testHandleSetPrimaryIndexCacheExpireSec(backendId, backendTablets);
}

### 6.Correct
link: https://github.com/StarRocks/starrocks/commit/48327871d4f44186682f93b32bae287cca074b2f
p_path: fe/fe-core/src/main/java/com/starrocks/alter/LakeTableSchemaChangeJob.java#publishVersion
t_path: fe/fe-core/src/test/java/com/starrocks/alter/LakeTableSchemaChangeJobTest.java#testPublishVersion

```java:test_src

@Test
public void testPublishVersion() throws AlterCancelException {
    new MockUp<Utils>() {
        @Mock
        public void publishVersion(@NotNull List<Tablet> tablets, long txnId, long baseVersion, long newVersion, long commitTime, long warehouseId) throws RpcException {
            throw new RpcException("publish version failed", "127.0.0.1");
        }
    };
    new MockUp<LakeTableSchemaChangeJob>() {
        @Mock
        public void sendAgentTask(AgentBatchTask batchTask) {
            batchTask.getAllTasks().forEach(t -> t.setFinished(true));
        }
    };
    schemaChangeJob.runPendingJob();
    Assert.assertEquals(AlterJobV2.JobState.WAITING_TXN, schemaChangeJob.getJobState());
    schemaChangeJob.runWaitingTxnJob();
    Assert.assertEquals(AlterJobV2.JobState.RUNNING, schemaChangeJob.getJobState());
    Collection<Partition> partitions = table.getPartitions();
    Assert.assertEquals(1, partitions.size());
    Partition partition = partitions.stream().findFirst().orElse(null);
    Assert.assertNotNull(partition);
    Assert.assertEquals(1, partition.getVisibleVersion());
    Assert.assertEquals(2, partition.getNextVersion());
    partition.setNextVersion(3);
    schemaChangeJob.runRunningJob();
    Assert.assertEquals(AlterJobV2.JobState.FINISHED_REWRITING, schemaChangeJob.getJobState());
    List<MaterializedIndex> shadowIndexes = partition.getMaterializedIndices(MaterializedIndex.IndexExtState.SHADOW);
    Assert.assertEquals(1, shadowIndexes.size());
    schemaChangeJob.runFinishedRewritingJob();
    Assert.assertEquals(AlterJobV2.JobState.FINISHED_REWRITING, schemaChangeJob.getJobState());
    partition.setVisibleVersion(2, System.currentTimeMillis());
    db.dropTable(table.getName());
    Exception exception = Assert.assertThrows(AlterCancelException.class, () -> {
        schemaChangeJob.runFinishedRewritingJob();
    });
    Assert.assertTrue(exception.getMessage().contains("Table does not exist"));
    Assert.assertEquals(AlterJobV2.JobState.FINISHED_REWRITING, schemaChangeJob.getJobState());
    db.registerTableUnlocked(table);
    schemaChangeJob.runFinishedRewritingJob();
    Assert.assertEquals(AlterJobV2.JobState.FINISHED_REWRITING, schemaChangeJob.getJobState());
    new MockUp<Utils>() {
        @Mock
        public void publishVersion(@NotNull List<Tablet> tablets, long txnId, long baseVersion, long newVersion, long commitTime, long warehouseId) {
        }
    };
    schemaChangeJob.runFinishedRewritingJob();
    Assert.assertEquals(AlterJobV2.JobState.FINISHED, schemaChangeJob.getJobState());
    Assert.assertTrue(schemaChangeJob.getFinishedTimeMs() > System.currentTimeMillis() - 10_000L);
    Assert.assertEquals(2, table.getBaseSchema().size());
    Assert.assertEquals("c0", table.getBaseSchema().get(0).getName());
    Assert.assertEquals("c1", table.getBaseSchema().get(1).getName());
    Assert.assertSame(partition, table.getPartitions().stream().findFirst().get());
    Assert.assertEquals(3, partition.getVisibleVersion());
    Assert.assertEquals(4, partition.getNextVersion());
    shadowIndexes = partition.getMaterializedIndices(MaterializedIndex.IndexExtState.SHADOW);
    Assert.assertEquals(0, shadowIndexes.size());
    List<MaterializedIndex> normalIndexes = partition.getMaterializedIndices(MaterializedIndex.IndexExtState.VISIBLE);
    Assert.assertEquals(1, normalIndexes.size());
    MaterializedIndex normalIndex = normalIndexes.get(0);
    schemaChangeJob.cancel("test");
    Assert.assertEquals(AlterJobV2.JobState.FINISHED, schemaChangeJob.getJobState());
}

```java:test_tgt

@Test
public void testPublishVersion() throws AlterCancelException {
    new MockUp<Utils>() {
        @Mock
        public void publishVersion(@NotNull List<Tablet> tablets, TxnInfoPB txnInfo, long baseVersion, long newVersion, long warehouseId) throws RpcException {
            throw new RpcException("publish version failed", "127.0.0.1");
        }
    };
    new MockUp<LakeTableSchemaChangeJob>() {
        @Mock
        public void sendAgentTask(AgentBatchTask batchTask) {
            batchTask.getAllTasks().forEach(t -> t.setFinished(true));
        }
    };
    schemaChangeJob.runPendingJob();
    Assert.assertEquals(AlterJobV2.JobState.WAITING_TXN, schemaChangeJob.getJobState());
    schemaChangeJob.runWaitingTxnJob();
    Assert.assertEquals(AlterJobV2.JobState.RUNNING, schemaChangeJob.getJobState());
    Collection<Partition> partitions = table.getPartitions();
    Assert.assertEquals(1, partitions.size());
    Partition partition = partitions.stream().findFirst().orElse(null);
    Assert.assertNotNull(partition);
    Assert.assertEquals(1, partition.getVisibleVersion());
    Assert.assertEquals(2, partition.getNextVersion());
    partition.setNextVersion(3);
    schemaChangeJob.runRunningJob();
    Assert.assertEquals(AlterJobV2.JobState.FINISHED_REWRITING, schemaChangeJob.getJobState());
    List<MaterializedIndex> shadowIndexes = partition.getMaterializedIndices(MaterializedIndex.IndexExtState.SHADOW);
    Assert.assertEquals(1, shadowIndexes.size());
    schemaChangeJob.runFinishedRewritingJob();
    Assert.assertEquals(AlterJobV2.JobState.FINISHED_REWRITING, schemaChangeJob.getJobState());
    partition.setVisibleVersion(2, System.currentTimeMillis());
    db.dropTable(table.getName());
    Exception exception = Assert.assertThrows(AlterCancelException.class, () -> {
        schemaChangeJob.runFinishedRewritingJob();
    });
    Assert.assertTrue(exception.getMessage().contains("Table does not exist"));
    Assert.assertEquals(AlterJobV2.JobState.FINISHED_REWRITING, schemaChangeJob.getJobState());
    db.registerTableUnlocked(table);
    schemaChangeJob.runFinishedRewritingJob();
    Assert.assertEquals(AlterJobV2.JobState.FINISHED_REWRITING, schemaChangeJob.getJobState());
    new MockUp<Utils>() {
        @Mock
        public void publishVersion(@NotNull List<Tablet> tablets, TxnInfoPB txnInfo, long baseVersion, long newVersion, long warehouseId) {
        }
    };
    schemaChangeJob.runFinishedRewritingJob();
    Assert.assertEquals(AlterJobV2.JobState.FINISHED, schemaChangeJob.getJobState());
    Assert.assertTrue(schemaChangeJob.getFinishedTimeMs() > System.currentTimeMillis() - 10_000L);
    Assert.assertEquals(2, table.getBaseSchema().size());
    Assert.assertEquals("c0", table.getBaseSchema().get(0).getName());
    Assert.assertEquals("c1", table.getBaseSchema().get(1).getName());
    Assert.assertSame(partition, table.getPartitions().stream().findFirst().get());
    Assert.assertEquals(3, partition.getVisibleVersion());
    Assert.assertEquals(4, partition.getNextVersion());
    shadowIndexes = partition.getMaterializedIndices(MaterializedIndex.IndexExtState.SHADOW);
    Assert.assertEquals(0, shadowIndexes.size());
    List<MaterializedIndex> normalIndexes = partition.getMaterializedIndices(MaterializedIndex.IndexExtState.VISIBLE);
    Assert.assertEquals(1, normalIndexes.size());
    MaterializedIndex normalIndex = normalIndexes.get(0);
    schemaChangeJob.cancel("test");
    Assert.assertEquals(AlterJobV2.JobState.FINISHED, schemaChangeJob.getJobState());
}

```java:llm_gen

@Test
public void testPublishVersion() throws AlterCancelException {
    new MockUp<Utils>() {
        @Mock
        public void publishVersion(@NotNull List<Tablet> tablets, TxnInfoPB txnInfo, long baseVersion, long newVersion, long warehouseId) throws RpcException {
            throw new RpcException("publish version failed", "127.0.0.1");
        }
    };
    new MockUp<LakeTableSchemaChangeJob>() {
        @Mock
        public void sendAgentTask(AgentBatchTask batchTask) {
            batchTask.getAllTasks().forEach(t -> t.setFinished(true));
        }
    };
    schemaChangeJob.runPendingJob();
    Assert.assertEquals(AlterJobV2.JobState.WAITING_TXN, schemaChangeJob.getJobState());
    schemaChangeJob.runWaitingTxnJob();
    Assert.assertEquals(AlterJobV2.JobState.RUNNING, schemaChangeJob.getJobState());
    Collection<Partition> partitions = table.getPartitions();
    Assert.assertEquals(1, partitions.size());
    Partition partition = partitions.stream().findFirst().orElse(null);
    Assert.assertNotNull(partition);
    Assert.assertEquals(1, partition.getVisibleVersion());
    Assert.assertEquals(2, partition.getNextVersion());
    partition.setNextVersion(3);
    schemaChangeJob.runRunningJob();
    Assert.assertEquals(AlterJobV2.JobState.FINISHED_REWRITING, schemaChangeJob.getJobState());
    List<MaterializedIndex> shadowIndexes = partition.getMaterializedIndices(MaterializedIndex.IndexExtState.SHADOW);
    Assert.assertEquals(1, shadowIndexes.size());
    schemaChangeJob.runFinishedRewritingJob();
    Assert.assertEquals(AlterJobV2.JobState.FINISHED_REWRITING, schemaChangeJob.getJobState());
    partition.setVisibleVersion(2, System.currentTimeMillis());
    db.dropTable(table.getName());
    Exception exception = Assert.assertThrows(AlterCancelException.class, () -> {
        schemaChangeJob.runFinishedRewritingJob();
    });
    Assert.assertTrue(exception.getMessage().contains("Table does not exist"));
    Assert.assertEquals(AlterJobV2.JobState.FINISHED_REWRITING, schemaChangeJob.getJobState());
    db.registerTableUnlocked(table);
    schemaChangeJob.runFinishedRewritingJob();
    Assert.assertEquals(AlterJobV2.JobState.FINISHED_REWRITING, schemaChangeJob.getJobState());
    new MockUp<Utils>() {
        @Mock
        public void publishVersion(@NotNull List<Tablet> tablets, TxnInfoPB txnInfo, long baseVersion, long newVersion, long warehouseId) {
        }
    };
    schemaChangeJob.runFinishedRewritingJob();
    Assert.assertEquals(AlterJobV2.JobState.FINISHED, schemaChangeJob.getJobState());
    Assert.assertTrue(schemaChangeJob.getFinishedTimeMs() > System.currentTimeMillis() - 10_000L);
    Assert.assertEquals(2, table.getBaseSchema().size());
    Assert.assertEquals("c0", table.getBaseSchema().get(0).getName());
    Assert.assertEquals("c1", table.getBaseSchema().get(1).getName());
    Assert.assertSame(partition, table.getPartitions().stream().findFirst().get());
    Assert.assertEquals(3, partition.getVisibleVersion());
    Assert.assertEquals(4, partition.getNextVersion());
    shadowIndexes = partition.getMaterializedIndices(MaterializedIndex.IndexExtState.SHADOW);
    Assert.assertEquals(0, shadowIndexes.size());
    List<MaterializedIndex> normalIndexes = partition.getMaterializedIndices(MaterializedIndex.IndexExtState.VISIBLE);
    Assert.assertEquals(1, normalIndexes.size());
    MaterializedIndex normalIndex = normalIndexes.get(0);
    schemaChangeJob.cancel("test");
    Assert.assertEquals(AlterJobV2.JobState.FINISHED, schemaChangeJob.getJobState());
}

### 7.Correct
link: https://github.com/apache/accumulo/commit/3f3da5a5da9cf500777d4c4b0d5a1c6556557dd8
p_path: core/src/main/java/org/apache/accumulo/core/util/Retry.java#incrementBy
t_path: core/src/test/java/org/apache/accumulo/core/util/RetryTest.java#testIncrementBy

```java:test_src

@Test
public void testIncrementBy() {
    NeedsTimeIncrement builder = Retry.builder().maxRetries(10).retryAfter(10, MILLISECONDS);
    builder.incrementBy(10, DAYS);
    builder.incrementBy(10, HOURS);
    builder.incrementBy(10, NANOSECONDS);
    builder.incrementBy(0, DAYS);
    builder.incrementBy(0, HOURS);
    builder.incrementBy(0, NANOSECONDS);
    assertThrows(IllegalArgumentException.class, () -> builder.incrementBy(-1, NANOSECONDS), "Should not allow negative increments");
}

```java:test_tgt

@Test
public void testIncrementBy() {
    NeedsTimeIncrement builder = Retry.builder().maxRetries(10).retryAfter(Duration.ofMillis(10));
    builder.incrementBy(Duration.ofDays(10));
    builder.incrementBy(Duration.ofHours(10));
    builder.incrementBy(Duration.ofNanos(10));
    builder.incrementBy(Duration.ofDays(0));
    builder.incrementBy(Duration.ofHours(0));
    builder.incrementBy(Duration.ofNanos(0));
    assertThrows(IllegalArgumentException.class, () -> builder.incrementBy(Duration.ofNanos(-1)), "Should not allow negative increments");
}

```java:llm_gen

@Test
public void testIncrementBy() {
    NeedsTimeIncrement builder = Retry.builder().maxRetries(10).retryAfter(Duration.ofMillis(10));
    builder.incrementBy(Duration.ofDays(10));
    builder.incrementBy(Duration.ofHours(10));
    builder.incrementBy(Duration.ofNanos(10));
    builder.incrementBy(Duration.ofDays(0));
    builder.incrementBy(Duration.ofHours(0));
    builder.incrementBy(Duration.ofNanos(0));
    assertThrows(IllegalArgumentException.class, () -> builder.incrementBy(Duration.ofNanos(-1)), "Should not allow negative increments");
}

### 8.Correct
link: https://github.com/apache/accumulo/commit/ac2886c34ee5b28b704bce2877d3952cb265a40b
p_path: shell/src/main/java/org/apache/accumulo/shell/commands/FateCommand.java#failTx
t_path: shell/src/test/java/org/apache/accumulo/shell/commands/FateCommandTest.java#testFailTx

```java:test_src

@Test
public void testFailTx() throws Exception {
    ZooStore<FateCommand> zs = createMock(ZooStore.class);
    String tidStr = "12345";
    long tid = Long.parseLong(tidStr, 16);
    expect(zs.getStatus(tid)).andReturn(ReadOnlyTStore.TStatus.NEW).anyTimes();
    zs.reserve(tid);
    expectLastCall().once();
    zs.setStatus(tid, ReadOnlyTStore.TStatus.FAILED_IN_PROGRESS);
    expectLastCall().once();
    zs.unreserve(tid, 0, TimeUnit.MILLISECONDS);
    expectLastCall().once();
    TestHelper helper = new TestHelper(true);
    replay(zs);
    FateCommand cmd = new FateCommand();
    assertFalse(cmd.failTx(helper, zs, zk, managerLockPath, new String[] { "fail", "tx1" }));
    assertTrue(cmd.failTx(helper, zs, zk, managerLockPath, new String[] { "fail", "12345" }));
    verify(zs);
}

```java:test_tgt

@Test
public void testFailTx() throws Exception {
    ZooStore<FateCommand> zs = createMock(ZooStore.class);
    String tidStr = "12345";
    long tid = Long.parseLong(tidStr, 16);
    expect(zs.getStatus(tid)).andReturn(ReadOnlyTStore.TStatus.NEW).anyTimes();
    zs.reserve(tid);
    expectLastCall().once();
    zs.setStatus(tid, ReadOnlyTStore.TStatus.FAILED_IN_PROGRESS);
    expectLastCall().once();
    zs.unreserve(tid, 0, TimeUnit.MILLISECONDS);
    expectLastCall().once();
    TestHelper helper = new TestHelper(true);
    replay(zs);
    FateCommand cmd = new FateCommand();
    var out = new PrintWriter(System.out);
    assertFalse(cmd.failTx(out, helper, zs, zk, managerLockPath, new String[] { "fail", "tx1" }));
    assertTrue(cmd.failTx(out, helper, zs, zk, managerLockPath, new String[] { "fail", "12345" }));
    verify(zs);
}

```java:llm_gen

@Test
public void testFailTx() throws Exception {
    ZooStore<FateCommand> zs = createMock(ZooStore.class);
    String tidStr = "12345";
    long tid = Long.parseLong(tidStr, 16);
    expect(zs.getStatus(tid)).andReturn(ReadOnlyTStore.TStatus.NEW).anyTimes();
    zs.reserve(tid);
    expectLastCall().once();
    zs.setStatus(tid, ReadOnlyTStore.TStatus.FAILED_IN_PROGRESS);
    expectLastCall().once();
    zs.unreserve(tid, 0, TimeUnit.MILLISECONDS);
    expectLastCall().once();
    TestHelper helper = new TestHelper(true);
    PrintWriter out = new PrintWriter(System.out);
    replay(zs);
    FateCommand cmd = new FateCommand();
    assertFalse(cmd.failTx(out, helper, zs, zk, managerLockPath, new String[] { "fail", "tx1" }));
    assertTrue(cmd.failTx(out, helper, zs, zk, managerLockPath, new String[] { "fail", "12345" }));
    verify(zs);
}

### 9.Additional Asserts
link: https://github.com/thingsboard/thingsboard/commit/33a70ba7c4a16e45ac854bc2cdee1a0a19a6ce9a
p_path: dao/src/main/java/org/thingsboard/server/dao/sql/widget/JpaWidgetsBundleDao.java#findSystemWidgetsBundles
t_path: dao/src/test/java/org/thingsboard/server/dao/sql/widget/JpaWidgetsBundleDaoTest.java#testFindSystemWidgetsBundles

```java:test_src

@Test
public void testFindSystemWidgetsBundles() {
    createSystemWidgetBundles(30, "WB_");
    widgetsBundles = widgetsBundleDao.find(TenantId.SYS_TENANT_ID);
    assertEquals(30, widgetsBundles.size());
    PageLink pageLink = new PageLink(10, 0, "WB");
    PageData<WidgetsBundle> widgetsBundles1 = widgetsBundleDao.findSystemWidgetsBundles(TenantId.SYS_TENANT_ID, pageLink);
    assertEquals(10, widgetsBundles1.getData().size());
    pageLink = pageLink.nextPageLink();
    PageData<WidgetsBundle> widgetsBundles2 = widgetsBundleDao.findSystemWidgetsBundles(TenantId.SYS_TENANT_ID, pageLink);
    assertEquals(10, widgetsBundles2.getData().size());
}

```java:test_tgt

@Test
public void testFindSystemWidgetsBundles() {
    createSystemWidgetBundles(30, "WB_");
    widgetsBundles = widgetsBundleDao.find(TenantId.SYS_TENANT_ID);
    assertEquals(30, widgetsBundles.size());
    PageLink pageLink = new PageLink(10, 0, "WB");
    PageData<WidgetsBundle> widgetsBundles1 = widgetsBundleDao.findSystemWidgetsBundles(TenantId.SYS_TENANT_ID, false, pageLink);
    assertEquals(10, widgetsBundles1.getData().size());
    pageLink = pageLink.nextPageLink();
    PageData<WidgetsBundle> widgetsBundles2 = widgetsBundleDao.findSystemWidgetsBundles(TenantId.SYS_TENANT_ID, false, pageLink);
    assertEquals(10, widgetsBundles2.getData().size());
}

```java:llm_gen

@Test
public void testFindSystemWidgetsBundles() {
    createSystemWidgetBundles(30, "WB_");
    widgetsBundles = widgetsBundleDao.find(TenantId.SYS_TENANT_ID);
    assertEquals(30, widgetsBundles.size());
    PageLink pageLink = new PageLink(10, 0, "WB");
    PageData<WidgetsBundle> widgetsBundles1 = widgetsBundleDao.findSystemWidgetsBundles(TenantId.SYS_TENANT_ID, false, pageLink);
    assertEquals(10, widgetsBundles1.getData().size());
    pageLink = pageLink.nextPageLink();
    PageData<WidgetsBundle> widgetsBundles2 = widgetsBundleDao.findSystemWidgetsBundles(TenantId.SYS_TENANT_ID, false, pageLink);
    assertEquals(10, widgetsBundles2.getData().size());
    PageData<WidgetsBundle> widgetsBundlesFullSearch = widgetsBundleDao.findSystemWidgetsBundles(TenantId.SYS_TENANT_ID, true, pageLink);
    assertEquals(10, widgetsBundlesFullSearch.getData().size());
}

### 10.Partial Updates
link: https://github.com/StarRocks/starrocks/commit/952bc956276f35b51e239eaceda8659a2eded4b1
p_path: fe/fe-core/src/main/java/com/starrocks/leader/ReportHandler.java#handleMigration
t_path: fe/fe-core/src/test/java/com/starrocks/leader/ReportHandlerTest.java#testHandleMigration

```java:test_src

@Test
public void testHandleMigration() throws TException {
    List<Long> tabletIds = GlobalStateMgr.getCurrentInvertedIndex().getTabletIdsByBackendId(10001);
    ListMultimap<TStorageMedium, Long> tabletMetaMigrationMap = ArrayListMultimap.create();
    for (Long tabletId : tabletIds) {
        tabletMetaMigrationMap.put(TStorageMedium.SSD, tabletId);
    }
    ReportHandler.handleMigration(tabletMetaMigrationMap, 10001);
    final SystemInfoService currentSystemInfo = GlobalStateMgr.getCurrentSystemInfo();
    Backend reportBackend = currentSystemInfo.getBackend(10001);
    BackendStatus backendStatus = reportBackend.getBackendStatus();
    backendStatus.lastSuccessReportTabletsTime = TimeUtils.longToTimeString(Long.MAX_VALUE);
    ReportHandler.handleMigration(tabletMetaMigrationMap, 10001);
    TabletInvertedIndex invertedIndex = GlobalStateMgr.getCurrentInvertedIndex();
    List<TabletMeta> tabletMetaList = invertedIndex.getTabletMetaList(tabletIds);
    for (int i = 0; i < tabletMetaList.size(); i++) {
        long tabletId = tabletIds.get(i);
        TabletMeta tabletMeta = tabletMetaList.get(i);
        Database db = GlobalStateMgr.getCurrentState().getDb("test");
        if (db == null) {
            continue;
        }
        OlapTable table = null;
        db.readLock();
        try {
            table = (OlapTable) db.getTable(tabletMeta.getTableId());
        } finally {
            db.readUnlock();
        }
        Partition partition = table.getPartition(tabletMeta.getPartitionId());
        MaterializedIndex idx = partition.getIndex(tabletMeta.getIndexId());
        LocalTablet tablet = (LocalTablet) idx.getTablet(tabletId);
        for (Replica replica : tablet.getImmutableReplicas()) {
            replica.setMaxRowsetCreationTime(System.currentTimeMillis() / 1000);
        }
    }
    Config.tablet_sched_max_migration_task_sent_once = 1000000;
    Config.primary_key_disk_schedule_time = 0;
    ReportHandler.handleMigration(tabletMetaMigrationMap, 10001);
}

```java:test_tgt

@Test
public void testHandleMigration() throws TException {
    List<Long> tabletIds = GlobalStateMgr.getCurrentState().getTabletInvertedIndex().getTabletIdsByBackendId(10001);
    ListMultimap<TStorageMedium, Long> tabletMetaMigrationMap = ArrayListMultimap.create();
    for (Long tabletId : tabletIds) {
        tabletMetaMigrationMap.put(TStorageMedium.SSD, tabletId);
    }
    ReportHandler.handleMigration(tabletMetaMigrationMap, 10001);
    final SystemInfoService currentSystemInfo = GlobalStateMgr.getCurrentState().getNodeMgr().getClusterInfo();
    Backend reportBackend = currentSystemInfo.getBackend(10001);
    BackendStatus backendStatus = reportBackend.getBackendStatus();
    backendStatus.lastSuccessReportTabletsTime = TimeUtils.longToTimeString(Long.MAX_VALUE);
    ReportHandler.handleMigration(tabletMetaMigrationMap, 10001);
    TabletInvertedIndex invertedIndex = GlobalStateMgr.getCurrentState().getTabletInvertedIndex();
    List<TabletMeta> tabletMetaList = invertedIndex.getTabletMetaList(tabletIds);
    for (int i = 0; i < tabletMetaList.size(); i++) {
        long tabletId = tabletIds.get(i);
        TabletMeta tabletMeta = tabletMetaList.get(i);
        Database db = GlobalStateMgr.getCurrentState().getDb("test");
        if (db == null) {
            continue;
        }
        OlapTable table = null;
        db.readLock();
        try {
            table = (OlapTable) db.getTable(tabletMeta.getTableId());
        } finally {
            db.readUnlock();
        }
        Partition partition = table.getPartition(tabletMeta.getPartitionId());
        MaterializedIndex idx = partition.getIndex(tabletMeta.getIndexId());
        LocalTablet tablet = (LocalTablet) idx.getTablet(tabletId);
        for (Replica replica : tablet.getImmutableReplicas()) {
            replica.setMaxRowsetCreationTime(System.currentTimeMillis() / 1000);
        }
    }
    Config.tablet_sched_max_migration_task_sent_once = 1000000;
    Config.primary_key_disk_schedule_time = 0;
    ReportHandler.handleMigration(tabletMetaMigrationMap, 10001);
}

```java:llm_gen

@Test
public void testHandleMigration() throws TException {
    List<Long> tabletIds = GlobalStateMgr.getCurrentState().getTabletInvertedIndex().getTabletIdsByBackendId(10001);
    ListMultimap<TStorageMedium, Long> tabletMetaMigrationMap = ArrayListMultimap.create();
    for (Long tabletId : tabletIds) {
        tabletMetaMigrationMap.put(TStorageMedium.SSD, tabletId);
    }
    ReportHandler.handleMigration(tabletMetaMigrationMap, 10001);
    final SystemInfoService currentSystemInfo = GlobalStateMgr.getCurrentSystemInfo();
    Backend reportBackend = currentSystemInfo.getBackend(10001);
    BackendStatus backendStatus = reportBackend.getBackendStatus();
    backendStatus.lastSuccessReportTabletsTime = TimeUtils.longToTimeString(Long.MAX_VALUE);
    ReportHandler.handleMigration(tabletMetaMigrationMap, 10001);
    TabletInvertedIndex invertedIndex = GlobalStateMgr.getCurrentState().getTabletInvertedIndex();
    List<TabletMeta> tabletMetaList = invertedIndex.getTabletMetaList(tabletIds);
    for (int i = 0; i < tabletMetaList.size(); i++) {
        long tabletId = tabletIds.get(i);
        TabletMeta tabletMeta = tabletMetaList.get(i);
        Database db = GlobalStateMgr.getCurrentState().getDb("test");
        if (db == null) {
            continue;
        }
        OlapTable table = null;
        db.readLock();
        try {
            table = (OlapTable) db.getTable(tabletMeta.getTableId());
        } finally {
            db.readUnlock();
        }
        Partition partition = table.getPartition(tabletMeta.getPartitionId());
        MaterializedIndex idx = partition.getIndex(tabletMeta.getIndexId());
        LocalTablet tablet = (LocalTablet) idx.getTablet(tabletId);
        for (Replica replica : tablet.getImmutableReplicas()) {
            replica.setMaxRowsetCreationTime(System.currentTimeMillis() / 1000);
        }
    }
    Config.tablet_sched_max_migration_task_sent_once = 1000000;
    Config.primary_key_disk_schedule_time = 0;
    ReportHandler.handleMigration(tabletMetaMigrationMap, 10001);
}

### 11.Assert Error
link: https://github.com/pentaho/pentaho-platform/commit/9bf4e91419e4d13f9be097f4d595d23ca1e4c3ed
p_path: repository/src/main/java/org/pentaho/platform/repository2/unified/jcr/DefaultDeleteHelper.java#getAllDeletedFiles
t_path: repository/src/test/java/org/pentaho/platform/repository2/unified/jcr/DefaultDeleteHelperTest.java#testGetAllDeletedFiles

```java:test_src

@Test
public void testGetAllDeletedFiles() throws Exception {
    final String path1 = "path1";
    final Calendar date1 = Calendar.getInstance();
    final Node deletedNode1 = createDeletedNode(path1, date1);
    final String path2 = "path2";
    final Calendar date2 = Calendar.getInstance();
    final Node deletedNode2 = createDeletedNode(path2, date2);
    final Node nodeTrash = mock(Node.class);
    when(nodeTrash.getNodes()).thenAnswer(invoc -> {
        final NodeIterator nodeIterator = mock(NodeIterator.class);
        when(nodeIterator.hasNext()).thenReturn(true, true, false);
        when(nodeIterator.nextNode()).thenReturn(deletedNode1, deletedNode2);
        return nodeIterator;
    });
    final Node nodeOtherFolder = mock(Node.class);
    when(nodeOtherFolder.hasNode(anyString())).thenReturn(true);
    when(nodeOtherFolder.getNode(anyString())).thenReturn(nodeTrash);
    final String pathUsr = "pathUser";
    final Calendar dateUsr = Calendar.getInstance();
    final Node deletedNodeUsr = createDeletedNode(pathUsr, dateUsr);
    final Node nodeTrashUsr = mock(Node.class);
    when(nodeTrashUsr.getNodes()).thenAnswer(invoc -> {
        NodeIterator nodeIteratorUsr = mock(NodeIterator.class);
        when(nodeIteratorUsr.hasNext()).thenReturn(true, false);
        when(nodeIteratorUsr.nextNode()).thenReturn(deletedNodeUsr);
        return nodeIteratorUsr;
    });
    final Node nodeUserFolder = mock(Node.class);
    when(nodeUserFolder.hasNode(anyString())).thenReturn(true);
    when(nodeUserFolder.getNode(anyString())).thenReturn(nodeTrashUsr);
    final boolean[] admin = { false };
    defaultDeleteHelper = new DefaultDeleteHelper(lockHelper, pathConversionHelper) {
        @Override
        protected boolean isAdmin() {
            return admin[0];
        }
        @Override
        protected List<String> getUserList() {
            return Arrays.asList("test", "other");
        }
    };
    when(session.getItem(endsWith("/other"))).thenReturn(nodeOtherFolder);
    when(session.getItem(endsWith("/test"))).thenReturn(nodeUserFolder);
    final List<RepositoryFile> deletedFiles = defaultDeleteHelper.getAllDeletedFiles(session, pentahoJcrConstants);
    assertNotNull(deletedFiles);
    assertEquals(1, deletedFiles.size());
    assertEquals(pathUsr, deletedFiles.get(0).getOriginalParentFolderPath());
    admin[0] = true;
    final List<RepositoryFile> deletedFilesAdmin = defaultDeleteHelper.getAllDeletedFiles(session, pentahoJcrConstants);
    assertNotNull(deletedFilesAdmin);
    assertEquals(3, deletedFilesAdmin.size());
}

```java:test_tgt

@Test
public void testGetAllDeletedFiles() throws Exception {
    final String path1 = "path1";
    final Calendar date1 = Calendar.getInstance();
    final Node deletedNode1 = createDeletedNode(path1, date1);
    final String path2 = "path2";
    final Calendar date2 = Calendar.getInstance();
    final Node deletedNode2 = createDeletedNode(path2, date2);
    final Node nodeTrash = mock(Node.class);
    when(nodeTrash.getNodes()).thenAnswer(invoc -> {
        final NodeIterator nodeIterator = mock(NodeIterator.class);
        when(nodeIterator.hasNext()).thenReturn(true, true, false);
        when(nodeIterator.nextNode()).thenReturn(deletedNode1, deletedNode2);
        return nodeIterator;
    });
    final Node nodeOtherFolder = mock(Node.class);
    when(nodeOtherFolder.hasNode(anyString())).thenReturn(true);
    when(nodeOtherFolder.hasNodes()).thenReturn(true);
    when(nodeOtherFolder.getNode(anyString())).thenReturn(nodeTrash);
    final String pathUsr = "pathUser";
    final Calendar dateUsr = Calendar.getInstance();
    final Node deletedNodeUsr = createDeletedNode(pathUsr, dateUsr);
    final Node nodeTrashUsr = mock(Node.class);
    when(nodeTrashUsr.getNodes()).thenAnswer(invoc -> {
        NodeIterator nodeIteratorUsr = mock(NodeIterator.class);
        when(nodeIteratorUsr.hasNext()).thenReturn(true, false);
        when(nodeIteratorUsr.nextNode()).thenReturn(deletedNodeUsr);
        return nodeIteratorUsr;
    });
    final Node nodeUserFolder = mock(Node.class);
    when(nodeUserFolder.hasNode(anyString())).thenReturn(true);
    when(nodeUserFolder.hasNodes()).thenReturn(true);
    when(nodeUserFolder.getNode(anyString())).thenReturn(nodeTrashUsr);
    final boolean[] admin = { false };
    defaultDeleteHelper = new DefaultDeleteHelper(lockHelper, pathConversionHelper) {
        @Override
        protected boolean isAdmin() {
            return admin[0];
        }
        @Override
        protected List<String> getUserList() {
            return Arrays.asList("test", "other");
        }
    };
    when(session.getItem(endsWith("/other"))).thenReturn(nodeOtherFolder);
    when(session.getItem(endsWith("/test"))).thenReturn(nodeUserFolder);
    final Node nodeHomeFolder = mock(Node.class);
    when(nodeHomeFolder.hasNode(anyString())).thenReturn(true);
    when(nodeHomeFolder.getNodes()).thenAnswer(invoc -> {
        NodeIterator nodeIteratorHome = mock(NodeIterator.class);
        when(nodeIteratorHome.hasNext()).thenReturn(true, true, false);
        when(nodeIteratorHome.next()).thenReturn(nodeOtherFolder, nodeUserFolder);
        return nodeIteratorHome;
    });
    when(session.getItem("/pentaho/tenant0/home")).thenReturn(nodeHomeFolder);
    final List<RepositoryFile> deletedFiles = defaultDeleteHelper.getAllDeletedFiles(session, pentahoJcrConstants);
    assertNotNull(deletedFiles);
    assertEquals(1, deletedFiles.size());
    assertEquals(pathUsr, deletedFiles.get(0).getOriginalParentFolderPath());
    admin[0] = true;
    final List<RepositoryFile> deletedFilesAdmin = defaultDeleteHelper.getAllDeletedFiles(session, pentahoJcrConstants);
    assertNotNull(deletedFilesAdmin);
    assertEquals(3, deletedFilesAdmin.size());
}

```java:llm_gen

@Test
public void testGetAllDeletedFiles() throws Exception {
    final String path1 = "path1";
    final Calendar date1 = Calendar.getInstance();
    final Node deletedNode1 = createDeletedNode(path1, date1);
    final String path2 = "path2";
    final Calendar date2 = Calendar.getInstance();
    final Node deletedNode2 = createDeletedNode(path2, date2);
    final Node nodeTrash = mock(Node.class);
    when(nodeTrash.getNodes()).thenAnswer(invoc -> {
        final NodeIterator nodeIterator = mock(NodeIterator.class);
        when(nodeIterator.hasNext()).thenReturn(true, true, false);
        when(nodeIterator.nextNode()).thenReturn(deletedNode1, deletedNode2);
        return nodeIterator;
    });
    final Node nodeUserFolder1 = mock(Node.class);
    when(nodeUserFolder1.hasNode(anyString())).thenReturn(true);
    when(nodeUserFolder1.getNode(anyString())).thenReturn(nodeTrash);
    final String path3 = "path3";
    final Calendar date3 = Calendar.getInstance();
    final Node deletedNode3 = createDeletedNode(path3, date3);
    final Node nodeTrash2 = mock(Node.class);
    when(nodeTrash2.getNodes()).thenAnswer(invoc -> {
        NodeIterator nodeIterator2 = mock(NodeIterator.class);
        when(nodeIterator2.hasNext()).thenReturn(true, false);
        when(nodeIterator2.nextNode()).thenReturn(deletedNode3);
        return nodeIterator2;
    });
    final Node nodeUserFolder2 = mock(Node.class);
    when(nodeUserFolder2.hasNode(anyString())).thenReturn(true);
    when(nodeUserFolder2.getNode(anyString())).thenReturn(nodeTrash2);
    final Node tenantHomeFolderNode = mock(Node.class);
    when(tenantHomeFolderNode.getNodes()).thenAnswer(invoc -> {
        NodeIterator userFoldersIterator = mock(NodeIterator.class);
        when(userFoldersIterator.hasNext()).thenReturn(true, true, false);
        when(userFoldersIterator.nextNode()).thenReturn(nodeUserFolder1, nodeUserFolder2);
        return userFoldersIterator;
    });
    final boolean[] admin = { false };
    defaultDeleteHelper = new DefaultDeleteHelper(lockHelper, pathConversionHelper) {
        @Override
        protected boolean isAdmin() {
            return admin[0];
        }
    };
    when(session.getItem(anyString())).thenReturn(tenantHomeFolderNode);
    final List<RepositoryFile> deletedFiles = defaultDeleteHelper.getAllDeletedFiles(session, pentahoJcrConstants);
    assertNotNull(deletedFiles);
    assertEquals(0, deletedFiles.size());
    admin[0] = true;
    final List<RepositoryFile> deletedFilesAdmin = defaultDeleteHelper.getAllDeletedFiles(session, pentahoJcrConstants);
    assertNotNull(deletedFilesAdmin);
    assertEquals(3, deletedFilesAdmin.size());
}

### 12.Missing Asserts
link: https://github.com/openhab/openhab-core/commit/1b503afdbbc654e0d845dce7c713813cf652ead5
p_path: bundles/org.openhab.core.persistence/src/main/java/org/openhab/core/persistence/extensions/PersistenceExtensions.java#deltaBetween
t_path: bundles/org.openhab.core.persistence/src/test/java/org/openhab/core/persistence/extensions/PersistenceExtensionsTest.java#testDeltaBetween

```java:test_src

@Test
public void testDeltaBetween() {
    DecimalType delta = PersistenceExtensions.deltaBetween(numberItem, ZonedDateTime.of(2005, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), ZonedDateTime.of(2011, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), TestPersistenceService.ID);
    assertThat(delta, is(notNullValue()));
    assertThat(delta.doubleValue(), is(closeTo(6, 0.001)));
    delta = PersistenceExtensions.deltaBetween(quantityItem, ZonedDateTime.of(2005, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), ZonedDateTime.of(2011, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), TestPersistenceService.ID);
    assertThat(delta, is(notNullValue()));
    assertThat(delta.doubleValue(), is(closeTo(6, 0.001)));
    delta = PersistenceExtensions.deltaBetween(numberItem, ZonedDateTime.of(2005, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), ZonedDateTime.of(2011, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()));
    assertThat(delta, is(nullValue()));
}

```java:test_tgt

@Test
public void testDeltaBetween() {
    State delta = PersistenceExtensions.deltaBetween(numberItem, ZonedDateTime.of(HISTORIC_INTERMEDIATE_VALUE_1, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), ZonedDateTime.of(HISTORIC_INTERMEDIATE_VALUE_2, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), SERVICE_ID);
    assertNotNull(delta);
    DecimalType dt = delta.as(DecimalType.class);
    assertNotNull(dt);
    assertEquals(HISTORIC_INTERMEDIATE_VALUE_2 - HISTORIC_INTERMEDIATE_VALUE_1, dt.doubleValue(), 0.001);
    delta = PersistenceExtensions.deltaBetween(quantityItem, ZonedDateTime.of(HISTORIC_INTERMEDIATE_VALUE_1, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), ZonedDateTime.of(HISTORIC_INTERMEDIATE_VALUE_2, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), SERVICE_ID);
    assertNotNull(delta);
    QuantityType<?> qt = delta.as(QuantityType.class);
    assertNotNull(qt);
    assertEquals(HISTORIC_INTERMEDIATE_VALUE_2 - HISTORIC_INTERMEDIATE_VALUE_1, qt.doubleValue(), 0.001);
    assertEquals(SIUnits.CELSIUS, qt.getUnit());
    delta = PersistenceExtensions.deltaBetween(numberItem, ZonedDateTime.of(FUTURE_INTERMEDIATE_VALUE_3, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), ZonedDateTime.of(FUTURE_INTERMEDIATE_VALUE_4, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), SERVICE_ID);
    assertNotNull(delta);
    dt = delta.as(DecimalType.class);
    assertNotNull(dt);
    assertEquals(FUTURE_INTERMEDIATE_VALUE_4 - FUTURE_INTERMEDIATE_VALUE_3, dt.doubleValue(), 0.001);
    delta = PersistenceExtensions.deltaBetween(quantityItem, ZonedDateTime.of(FUTURE_INTERMEDIATE_VALUE_3, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), ZonedDateTime.of(FUTURE_INTERMEDIATE_VALUE_4, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), SERVICE_ID);
    assertNotNull(delta);
    qt = delta.as(QuantityType.class);
    assertNotNull(qt);
    assertEquals(FUTURE_INTERMEDIATE_VALUE_4 - FUTURE_INTERMEDIATE_VALUE_3, qt.doubleValue(), 0.001);
    assertEquals(SIUnits.CELSIUS, qt.getUnit());
    delta = PersistenceExtensions.deltaBetween(numberItem, ZonedDateTime.of(HISTORIC_INTERMEDIATE_VALUE_1, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), ZonedDateTime.of(FUTURE_INTERMEDIATE_VALUE_3, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), SERVICE_ID);
    assertNotNull(delta);
    dt = delta.as(DecimalType.class);
    assertNotNull(dt);
    assertEquals(FUTURE_INTERMEDIATE_VALUE_3 - HISTORIC_INTERMEDIATE_VALUE_1, dt.doubleValue(), 0.001);
    delta = PersistenceExtensions.deltaBetween(quantityItem, ZonedDateTime.of(HISTORIC_INTERMEDIATE_VALUE_1, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), ZonedDateTime.of(FUTURE_INTERMEDIATE_VALUE_3, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), SERVICE_ID);
    assertNotNull(delta);
    qt = delta.as(QuantityType.class);
    assertNotNull(qt);
    assertEquals(FUTURE_INTERMEDIATE_VALUE_3 - HISTORIC_INTERMEDIATE_VALUE_1, qt.doubleValue(), 0.001);
    assertEquals(SIUnits.CELSIUS, qt.getUnit());
    delta = PersistenceExtensions.deltaBetween(numberItem, ZonedDateTime.of(HISTORIC_INTERMEDIATE_VALUE_1, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), ZonedDateTime.of(HISTORIC_INTERMEDIATE_VALUE_2, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()));
    assertNull(delta);
}

```java:llm_gen

@Test
public void testDeltaBetween() {
    State delta = PersistenceExtensions.deltaBetween(numberItem, ZonedDateTime.of(2005, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), ZonedDateTime.of(2011, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), TestPersistenceService.ID);
    assertThat(delta, is(notNullValue()));
    assertThat(((DecimalType) delta).doubleValue(), is(closeTo(6, 0.001)));
    delta = PersistenceExtensions.deltaBetween(quantityItem, ZonedDateTime.of(2005, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), ZonedDateTime.of(2011, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), TestPersistenceService.ID);
    assertThat(delta, is(notNullValue()));
    assertThat(((DecimalType) delta).doubleValue(), is(closeTo(6, 0.001)));
    delta = PersistenceExtensions.deltaBetween(numberItem, ZonedDateTime.of(2005, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), ZonedDateTime.of(2011, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()));
    assertThat(delta, is(nullValue()));
}

### 13.Test Preparation Error
link: https://github.com/halo-dev/halo/commit/0e17d53ede66c57b12f2dec4c92874c7e69ed9ef
p_path: application/src/main/java/run/halo/app/notification/DefaultNotificationCenter.java#subscribe
t_path: application/src/test/java/run/halo/app/notification/DefaultNotificationCenterTest.java#testSubscribe

````java:test_src

@Test
public void testSubscribe() {
    var spyNotificationCenter = spy(notificationCenter);
    Subscription subscription = createSubscriptions().get(0);
    var subscriber = subscription.getSpec().getSubscriber();
    var reason = subscription.getSpec().getReason();
    doReturn(Flux.just(subscription)).when(spyNotificationCenter).listSubscription(eq(subscriber), eq(reason));
    when(client.create(any(Subscription.class))).thenReturn(Mono.empty());
    spyNotificationCenter.subscribe(subscriber, reason).block();
    verify(client, times(0)).create(any(Subscription.class));
    var newReason = JsonUtils.deepCopy(reason);
    newReason.setReasonType("fake-reason-type");
    doReturn(Flux.empty()).when(spyNotificationCenter).listSubscription(eq(subscriber), eq(newReason));
    spyNotificationCenter.subscribe(subscriber, newReason).block();
    verify(client).create(any(Subscription.class));
}

```java:test_tgt

@Test
public void testSubscribe() {
    var spyNotificationCenter = spy(notificationCenter);
    Subscription subscription = createSubscriptions().get(0);
    var subscriber = subscription.getSpec().getSubscriber();
    var reason = subscription.getSpec().getReason();
    doReturn(Mono.empty()).when(spyNotificationCenter).unsubscribe(eq(subscriber), eq(reason));
    when(client.create(any(Subscription.class))).thenReturn(Mono.empty());
    spyNotificationCenter.subscribe(subscriber, reason).block();
    verify(client).create(any(Subscription.class));
}

```java:llm_gen

@Test
public void testSubscribe() {
    var spyNotificationCenter = spy(notificationCenter);
    Subscription subscription = createSubscriptions().get(0);
    var subscriber = subscription.getSpec().getSubscriber();
    var reason = subscription.getSpec().getReason();
    doReturn(Mono.empty()).when(spyNotificationCenter).unsubscribe(eq(subscriber), eq(reason));
    when(client.create(any(Subscription.class))).thenReturn(Mono.empty());
    spyNotificationCenter.subscribe(subscriber, reason).block();
    verify(client, times(0)).create(any(Subscription.class));
    var newReason = JsonUtils.deepCopy(reason);
    newReason.setReasonType("fake-reason-type");
    doReturn(Mono.empty()).when(spyNotificationCenter).unsubscribe(eq(subscriber), eq(newReason));
    spyNotificationCenter.subscribe(subscriber, newReason).block();
    verify(client).create(any(Subscription.class));
}

### 14.Wrong Update Direction
link: https://github.com/YunaiV/ruoyi-vue-pro/commit/286e24ad6cc6c7cee81dc78bfb8cb6f54c9f858c
p_path: yudao-module-system/yudao-module-system-biz/src/main/java/cn/iocoder/yudao/module/system/service/logger/OperateLogServiceImpl.java#createOperateLog
t_path: yudao-module-system/yudao-module-system-biz/src/test/java/cn/iocoder/yudao/module/system/service/logger/OperateLogServiceImplTest.java#testCreateOperateLog

```java:test_src

@Test
public void testCreateOperateLog() {
    OperateLogCreateReqDTO reqVO = RandomUtils.randomPojo(OperateLogCreateReqDTO.class, o -> o.setExts(MapUtil.<String, Object>builder("orderId", randomLongId()).build()));
    // 调研
    operateLogServiceImpl.createOperateLog(reqVO);
    // 断言
    OperateLogDO operateLogDO = operateLogMapper.selectOne(null);
    assertPojoEquals(reqVO, operateLogDO);
}

```java:test_tgt

@Test
public void testCreateOperateLog() {
    OperateLogCreateReqDTO reqVO = RandomUtils.randomPojo(OperateLogCreateReqDTO.class);
    // 调研
    operateLogServiceImpl.createOperateLog(reqVO);
    // 断言
    OperateLogDO operateLogDO = operateLogMapper.selectOne(null);
    assertPojoEquals(reqVO, operateLogDO);
}

```java:llm_gen

@Test
public void testCreateOperateLog() {
    OperateLogCreateReqDTO reqVO = RandomUtils.randomPojo(OperateLogCreateReqDTO.class, o -> o.setExts(MapUtil.<String, Object>builder("orderId", randomLongId()).build()));
    operateLogServiceImpl.createOperateLog(reqVO);
    OperateLogDO operateLogDO = operateLogMapper.selectOne(null);
    assertPojoEquals(reqVO, operateLogDO);
    assertThat(operateLogDO.getJavaMethodArgs()).hasSizeLessThanOrEqualTo(OperateLogServiceImpl.JAVA_METHOD_ARGS_MAX_LENGTH);
    assertThat(operateLogDO.getResultData()).hasSizeLessThanOrEqualTo(OperateLogServiceImpl.RESULT_MAX_LENGTH);
}


### 15.Correct
link: https://github.com/castlemock/castlemock/commit/a6f7eb9d9651b790ac1d7e4120dd5960f3bc9b3e
p_path: web/web-core/src/main/java/com/castlemock/web/core/utility/HttpMessageSupport.java#getBody
t_path: web/web-core/src/test/java/com/castlemock/web/core/utility/HttpMessageSupportTest.java#testGetBody

```java:test_src

@Test
@SuppressWarnings("varargs")
public void testGetBody() {
    final String readerOutput = "This is the output from the reader";
    final HttpServletRequest httpServletRequest = Mockito.mock(HttpServletRequest.class);
    final BufferedReader reader = Mockito.mock(BufferedReader.class);
    try {
        Mockito.when(httpServletRequest.getReader()).thenReturn(reader);
    } catch (IOException e) {
        Assert.fail("Unable to mock getReader method for HttpServletRequest");
    }
    try {
        final String noValue = null;
        Mockito.when(reader.readLine()).thenReturn(readerOutput, noValue);
    } catch (IOException e) {
        Assert.fail("Unable to mock readLine method for BufferedReader");
    }
    final String output = HttpMessageSupport.getBody(httpServletRequest);
    Assert.assertEquals(readerOutput, output);
}

```java:test_tgt

@Test
@SuppressWarnings("varargs")
public void testGetBody() {
    final String readerOutput = "This is the output from the reader";
    final HttpServletRequest httpServletRequest = Mockito.mock(HttpServletRequest.class);
    final BufferedReader reader = Mockito.mock(BufferedReader.class);
    try {
        Mockito.when(httpServletRequest.getReader()).thenReturn(reader);
    } catch (IOException e) {
        Assert.fail("Unable to mock getReader method for HttpServletRequest");
    }
    try {
        Mockito.when(reader.readLine()).thenReturn(readerOutput, (String) null);
    } catch (IOException e) {
        Assert.fail("Unable to mock readLine method for BufferedReader");
    }
    final String output = HttpMessageSupport.getBody(httpServletRequest);
    Assert.assertEquals(readerOutput, output);
}

```java:llm_gen

@Test
@SuppressWarnings("varargs")
public void testGetBody() {
    final String readerOutput = "This is the output from the reader";
    final HttpServletRequest httpServletRequest = Mockito.mock(HttpServletRequest.class);
    final BufferedReader reader = Mockito.mock(BufferedReader.class);
    try {
        Mockito.when(httpServletRequest.getReader()).thenReturn(reader);
    } catch (IOException e) {
        Assert.fail("Unable to mock getReader method for HttpServletRequest");
    }
    try {
        final String noValue = null;
        Mockito.when(reader.readLine()).thenReturn(readerOutput, noValue);
    } catch (IOException e) {
        Assert.fail("Unable to mock readLine method for BufferedReader");
    }
    final String output = HttpMessageSupport.getBody(httpServletRequest);
    Assert.assertEquals(readerOutput, output);
}

### 16.Missing Asserts
link: https://github.com/apache/flink-kubernetes-operator/commit/ede1a610b3375d31a2e82287eec67ace70c4c8df
p_path: flink-kubernetes-operator/src/main/java/org/apache/flink/kubernetes/operator/service/NativeFlinkService.java#deleteClusterInternal
t_path: flink-kubernetes-operator/src/test/java/org/apache/flink/kubernetes/operator/service/NativeFlinkServiceTest.java#testDeleteClusterInternal

```java:test_src

@Test
public void testDeleteClusterInternal() {
    var deployment = TestUtils.buildApplicationCluster();
    ReconciliationUtils.updateStatusForDeployedSpec(deployment, new Configuration());
    var flinkService = createFlinkService(null);
    var dep = new DeploymentBuilder().withNewMetadata().withName(TestUtils.TEST_DEPLOYMENT_NAME).withNamespace(TestUtils.TEST_NAMESPACE).endMetadata().withNewSpec().endSpec().build();
    client.resource(dep).create();
    assertNotNull(client.apps().deployments().inNamespace(TestUtils.TEST_NAMESPACE).withName(TestUtils.TEST_DEPLOYMENT_NAME).get());
    flinkService.deleteClusterInternal(deployment.getMetadata(), configManager.getObserveConfig(deployment), false, DeletionPropagation.FOREGROUND);
    assertNull(client.apps().deployments().inNamespace(TestUtils.TEST_NAMESPACE).withName(TestUtils.TEST_DEPLOYMENT_NAME).get());
}

```java:test_tgt

@Test
public void testDeleteClusterInternal() {
    var flinkService = new NativeFlinkService(client, null, executorService, operatorConfig, eventRecorder) {
        @Override
        protected Duration deleteDeploymentBlocking(String name, Resource<Deployment> deployment, DeletionPropagation propagation, Duration timeout) {
            assertEquals(0, deployment.get().getSpec().getReplicas());
            return super.deleteDeploymentBlocking(name, deployment, propagation, timeout);
        }
    };
    var deployment = TestUtils.buildApplicationCluster();
    ReconciliationUtils.updateStatusForDeployedSpec(deployment, new Configuration());
    var dep = new DeploymentBuilder().withNewMetadata().withName(TestUtils.TEST_DEPLOYMENT_NAME).withNamespace(TestUtils.TEST_NAMESPACE).endMetadata().withNewSpec().withReplicas(1).endSpec().build();
    client.resource(dep).create();
    assertNotNull(client.apps().deployments().inNamespace(TestUtils.TEST_NAMESPACE).withName(TestUtils.TEST_DEPLOYMENT_NAME).get());
    flinkService.deleteClusterInternal(deployment.getMetadata().getNamespace(), deployment.getMetadata().getName(), configManager.getObserveConfig(deployment), DeletionPropagation.FOREGROUND);
    assertNull(client.apps().deployments().inNamespace(TestUtils.TEST_NAMESPACE).withName(TestUtils.TEST_DEPLOYMENT_NAME).get());
}

```java:llm_gen

@Test
public void testDeleteClusterInternal() {
    var deployment = TestUtils.buildApplicationCluster();
    ReconciliationUtils.updateStatusForDeployedSpec(deployment, new Configuration());
    var flinkService = createFlinkService(null);
    var dep = new DeploymentBuilder().withNewMetadata().withName(TestUtils.TEST_DEPLOYMENT_NAME).withNamespace(TestUtils.TEST_NAMESPACE).endMetadata().withNewSpec().endSpec().build();
    client.resource(dep).create();
    assertNotNull(client.apps().deployments().inNamespace(TestUtils.TEST_NAMESPACE).withName(TestUtils.TEST_DEPLOYMENT_NAME).get());
    flinkService.deleteClusterInternal(TestUtils.TEST_NAMESPACE, TestUtils.TEST_DEPLOYMENT_NAME, configManager.getObserveConfig(deployment), DeletionPropagation.FOREGROUND);
    assertNull(client.apps().deployments().inNamespace(TestUtils.TEST_NAMESPACE).withName(TestUtils.TEST_DEPLOYMENT_NAME).get());
}

### 17.External Function Modification
link: https://github.com/thingsboard/thingsboard/commit/dc5f59254db4a0471b09bec0a3ac9d8573214b28
p_path: application/src/main/java/org/thingsboard/server/controller/MobileApplicationController.java#saveMobileAppSettings
t_path: application/src/test/java/org/thingsboard/server/controller/MobileApplicationControllerTest.java#testSaveMobileAppSettings

```java:test_src

@Test
public void testSaveMobileAppSettings() throws Exception {
    loginSysAdmin();
    MobileAppSettings mobileAppSettings = doGet("/api/mobile/app/settings", MobileAppSettings.class);
    assertThat(mobileAppSettings.getQrCodeConfig().getQrCodeLabel()).isEqualTo(TEST_LABEL);
    assertThat(mobileAppSettings.isUseDefault()).isTrue();
    mobileAppSettings.setUseDefault(false);
    doPost("/api/mobile/app/settings", mobileAppSettings).andExpect(status().isOk());
    MobileAppSettings updatedMobileAppSettings = doGet("/api/mobile/app/settings", MobileAppSettings.class);
    assertThat(updatedMobileAppSettings.isUseDefault()).isFalse();
}

```java:test_tgt

@Test
public void testSaveMobileAppSettings() throws Exception {
    loginSysAdmin();
    MobileAppSettings mobileAppSettings = doGet("/api/mobile/app/settings", MobileAppSettings.class);
    assertThat(mobileAppSettings.getQrCodeConfig().getQrCodeLabel()).isEqualTo(TEST_LABEL);
    assertThat(mobileAppSettings.isUseDefaultApp()).isTrue();
    mobileAppSettings.setUseDefaultApp(false);
    doPost("/api/mobile/app/settings", mobileAppSettings).andExpect(status().isOk());
    MobileAppSettings updatedMobileAppSettings = doGet("/api/mobile/app/settings", MobileAppSettings.class);
    assertThat(updatedMobileAppSettings.isUseDefaultApp()).isFalse();
}

```java:llm_gen

@Test
public void testSaveMobileAppSettings() throws Exception {
    loginSysAdmin();
    MobileAppSettings mobileAppSettings = doGet("/api/mobile/app/settings", MobileAppSettings.class);
    assertThat(mobileAppSettings.getQrCodeConfig().getQrCodeLabel()).isEqualTo(TEST_LABEL);
    assertThat(mobileAppSettings.isUseDefault()).isTrue();
    mobileAppSettings.setUseDefault(false);
    doPost("/api/mobile/app/settings", mobileAppSettings)
        .andExpect(status().isOk());
    MobileAppSettings updatedMobileAppSettings = doGet("/api/mobile/app/settings", MobileAppSettings.class);
    assertThat(updatedMobileAppSettings.isUseDefault()).isFalse();
}

### 18.Correct
link: https://github.com/apache/nifi/commit/dd5854d324095f9d29aac842488cbf1c407f08d4
p_path: nifi-nar-bundles/nifi-azure-bundle/nifi-azure-parameter-providers/src/main/java/org/apache/nifi/parameter/azure/AzureKeyVaultSecretsParameterProvider.java#fetchParameters
t_path: nifi-nar-bundles/nifi-azure-bundle/nifi-azure-parameter-providers/src/test/java/org/apache/nifi/parameter/azure/TestAzureKeyVaultSecretsParameterProvider.java#testFetchParameters

```java:test_src

@Test
public void testFetchParameters() throws IOException, InitializationException {
    mockSecretClient(mockParameterGroups);
    runProviderTest(8, ConfigVerificationResult.Outcome.SUCCESSFUL);
}

```java:test_tgt

@Test
public void testFetchParameters() throws InitializationException {
    mockSecretClient(mockParameterGroups);
    runProviderTest(8, ConfigVerificationResult.Outcome.SUCCESSFUL);
}

```java:llm_gen

@Test
public void testFetchParameters() throws InitializationException {
    mockSecretClient(mockParameterGroups);
    runProviderTest(8, ConfigVerificationResult.Outcome.SUCCESSFUL);
}

### 19.External Class Modification
link: https://github.com/StarRocks/starrocks/commit/ce5a8c5eed19b0957951a6cf9fdd1c4899fa5669
p_path: fe/fe-core/src/main/java/com/starrocks/qe/ShowExecutor.java#showCreateExternalCatalogTable
t_path: fe/fe-core/src/test/java/com/starrocks/qe/ShowExecutorTest.java#testShowCreateExternalCatalogTable

```java:test_src

@Test
public void testShowCreateExternalCatalogTable() throws DdlException, AnalysisException {
    new MockUp<MetadataMgr>() {
        @Mock
        public Database getDb(String catalogName, String dbName) {
            return new Database();
        }
        @Mock
        public Table getTable(String catalogName, String dbName, String tblName) {
            List<Column> fullSchema = new ArrayList<>();
            Column columnId = new Column("id", Type.INT, true);
            columnId.setComment("id");
            Column columnName = new Column("name", Type.VARCHAR);
            Column columnYear = new Column("year", Type.INT);
            Column columnDt = new Column("dt", Type.INT);
            fullSchema.add(columnId);
            fullSchema.add(columnName);
            fullSchema.add(columnYear);
            fullSchema.add(columnDt);
            List<String> partitions = Lists.newArrayList();
            partitions.add("year");
            partitions.add("dt");
            HiveTable.Builder tableBuilder = HiveTable.builder().setId(1).setTableName("test_table").setCatalogName("hive_catalog").setResourceName(toResourceName("hive_catalog", "hive")).setHiveDbName("hive_db").setHiveTableName("test_table").setPartitionColumnNames(partitions).setFullSchema(fullSchema).setTableLocation("hdfs://hadoop/hive/warehouse/test.db/test").setCreateTime(10000);
            return tableBuilder.build();
        }
    };
    ShowCreateTableStmt stmt = new ShowCreateTableStmt(new TableName("hive_catalog", "hive_db", "test_table"), ShowCreateTableStmt.CreateTableType.TABLE);
    ShowExecutor executor = new ShowExecutor(ctx, stmt);
    ShowResultSet resultSet = executor.execute();
    Assert.assertEquals("test_table", resultSet.getResultRows().get(0).get(0));
    Assert.assertEquals("CREATE TABLE `test_table` (\n" + "  `id` int(11) DEFAULT NULL COMMENT \"id\",\n" + "  `name` varchar DEFAULT NULL,\n" + "  `year` int(11) DEFAULT NULL,\n" + "  `dt` int(11) DEFAULT NULL\n" + ")\n" + "PARTITION BY ( year, dt )\n" + "PROPERTIES (\"location\" = \"hdfs://hadoop/hive/warehouse/test.db/test\");", resultSet.getResultRows().get(0).get(1));
}

```java:test_tgt

@Test
public void testShowCreateExternalCatalogTable() throws DdlException, AnalysisException {
    new MockUp<MetadataMgr>() {
        @Mock
        public Database getDb(String catalogName, String dbName) {
            return new Database();
        }
        @Mock
        public Table getTable(String catalogName, String dbName, String tblName) {
            List<Column> fullSchema = new ArrayList<>();
            Column columnId = new Column("id", Type.INT, true);
            columnId.setComment("id");
            Column columnName = new Column("name", Type.VARCHAR);
            Column columnYear = new Column("year", Type.INT);
            Column columnDt = new Column("dt", Type.INT);
            fullSchema.add(columnId);
            fullSchema.add(columnName);
            fullSchema.add(columnYear);
            fullSchema.add(columnDt);
            List<String> partitions = Lists.newArrayList();
            partitions.add("year");
            partitions.add("dt");
            HiveTable.Builder tableBuilder = HiveTable.builder().setId(1).setTableName("test_table").setCatalogName("hive_catalog").setResourceName(toResourceName("hive_catalog", "hive")).setHiveDbName("hive_db").setHiveTableName("test_table").setPartitionColumnNames(partitions).setFullSchema(fullSchema).setTableLocation("hdfs://hadoop/hive/warehouse/test.db/test").setCreateTime(10000);
            return tableBuilder.build();
        }
    };
    ShowCreateTableStmt stmt = new ShowCreateTableStmt(new TableName("hive_catalog", "hive_db", "test_table"), ShowCreateTableStmt.CreateTableType.TABLE);
    ShowExecutor executor = new ShowExecutor();
    ShowResultSet resultSet = executor.execute(stmt, ctx);
    Assert.assertEquals("test_table", resultSet.getResultRows().get(0).get(0));
    Assert.assertEquals("CREATE TABLE `test_table` (\n" + "  `id` int(11) DEFAULT NULL COMMENT \"id\",\n" + "  `name` varchar DEFAULT NULL,\n" + "  `year` int(11) DEFAULT NULL,\n" + "  `dt` int(11) DEFAULT NULL\n" + ")\n" + "PARTITION BY ( year, dt )\n" + "PROPERTIES (\"location\" = \"hdfs://hadoop/hive/warehouse/test.db/test\");", resultSet.getResultRows().get(0).get(1));
}

```java:llm_gen

@Test
public void testShowCreateExternalCatalogTable() throws DdlException, AnalysisException {
    new MockUp<MetadataMgr>() {
        @Mock
        public Database getDb(String catalogName, String dbName) {
            return new Database();
        }
        @Mock
        public Table getTable(String catalogName, String dbName, String tblName) {
            List<Column> fullSchema = new ArrayList<>();
            Column columnId = new Column("id", Type.INT, true);
            columnId.setComment("id");
            Column columnName = new Column("name", Type.VARCHAR);
            Column columnYear = new Column("year", Type.INT);
            Column columnDt = new Column("dt", Type.INT);
            fullSchema.add(columnId);
            fullSchema.add(columnName);
            fullSchema.add(columnYear);
            fullSchema.add(columnDt);
            List<String> partitions = Lists.newArrayList();
            partitions.add("year");
            partitions.add("dt");
            HiveTable.Builder tableBuilder = HiveTable.builder().setId(1).setTableName("test_table").setCatalogName("hive_catalog").setResourceName(toResourceName("hive_catalog", "hive")).setHiveDbName("hive_db").setHiveTableName("test_table").setPartitionColumnNames(partitions).setFullSchema(fullSchema).setTableLocation("hdfs://hadoop/hive/warehouse/test.db/test").setCreateTime(10000);
            return tableBuilder.build();
        }
    };
    ShowCreateTableStmt stmt = new ShowCreateTableStmt(new TableName("hive_catalog", "hive_db", "test_table"), ShowCreateTableStmt.CreateTableType.TABLE);
    ShowExecutor executor = new ShowExecutor(ctx, stmt);
    ShowResultSet resultSet = executor.execute();
    Assert.assertEquals("test_table", resultSet.getResultRows().get(0).get(0));
    Assert.assertEquals("CREATE TABLE `test_table` (\n" + "  `id` int(11) DEFAULT NULL COMMENT \"id\",\n" + "  `name` varchar DEFAULT NULL,\n" + "  `year` int(11) DEFAULT NULL,\n" + "  `dt` int(11) DEFAULT NULL\n" + ")\n" + "PARTITION BY ( year, dt )\n" + "COMMENT (\"\")\n" + "PROPERTIES (\"location\" = \"hdfs://hadoop/hive/warehouse/test.db/test\");", resultSet.getResultRows().get(0).get(1));
}

### 20.External Function Modification
link: https://github.com/apache/kafka/commit/affe8da54c96d4038481c3807d059134961445a3
p_path: clients/src/main/java/org/apache/kafka/clients/producer/internals/RecordAccumulator.java#splitAndReenqueue
t_path: clients/src/test/java/org/apache/kafka/clients/producer/internals/RecordAccumulatorTest.java#testSplitAndReenqueue

```java:test_src

@Test
public void testSplitAndReenqueue() throws ExecutionException, InterruptedException {
    long now = time.milliseconds();
    RecordAccumulator accum = createTestRecordAccumulator(1024, 10 * 1024, CompressionType.GZIP, 10);
    ByteBuffer buffer = ByteBuffer.allocate(4096);
    MemoryRecordsBuilder builder = MemoryRecords.builder(buffer, CompressionType.NONE, TimestampType.CREATE_TIME, 0L);
    ProducerBatch batch = new ProducerBatch(tp1, builder, now, true);
    byte[] value = new byte[1024];
    final AtomicInteger acked = new AtomicInteger(0);
    Callback cb = (metadata, exception) -> acked.incrementAndGet();
    Future<RecordMetadata> future1 = batch.tryAppend(now, null, value, Record.EMPTY_HEADERS, cb, now);
    Future<RecordMetadata> future2 = batch.tryAppend(now, null, value, Record.EMPTY_HEADERS, cb, now);
    assertNotNull(future1);
    assertNotNull(future2);
    batch.close();
    accum.reenqueue(batch, now);
    time.sleep(121L);
    RecordAccumulator.ReadyCheckResult result = accum.ready(metadataCache, time.milliseconds());
    assertFalse(result.readyNodes.isEmpty(), "The batch should be ready");
    Map<Integer, List<ProducerBatch>> drained = accum.drain(metadataCache, result.readyNodes, Integer.MAX_VALUE, time.milliseconds());
    assertEquals(1, drained.size(), "Only node1 should be drained");
    assertEquals(1, drained.get(node1.id()).size(), "Only one batch should be drained");
    accum.splitAndReenqueue(drained.get(node1.id()).get(0));
    time.sleep(101L);
    drained = accum.drain(metadataCache, result.readyNodes, Integer.MAX_VALUE, time.milliseconds());
    assertFalse(drained.isEmpty());
    assertFalse(drained.get(node1.id()).isEmpty());
    drained.get(node1.id()).get(0).complete(acked.get(), 100L);
    assertEquals(1, acked.get(), "The first message should have been acked.");
    assertTrue(future1.isDone());
    assertEquals(0, future1.get().offset());
    drained = accum.drain(metadataCache, result.readyNodes, Integer.MAX_VALUE, time.milliseconds());
    assertFalse(drained.isEmpty());
    assertFalse(drained.get(node1.id()).isEmpty());
    drained.get(node1.id()).get(0).complete(acked.get(), 100L);
    assertEquals(2, acked.get(), "Both message should have been acked.");
    assertTrue(future2.isDone());
    assertEquals(1, future2.get().offset());
}

```java:test_tgt

@Test
public void testSplitAndReenqueue() throws ExecutionException, InterruptedException {
    long now = time.milliseconds();
    RecordAccumulator accum = createTestRecordAccumulator(1024, 10 * 1024, Compression.gzip().build(), 10);
    ByteBuffer buffer = ByteBuffer.allocate(4096);
    MemoryRecordsBuilder builder = MemoryRecords.builder(buffer, Compression.NONE, TimestampType.CREATE_TIME, 0L);
    ProducerBatch batch = new ProducerBatch(tp1, builder, now, true);
    byte[] value = new byte[1024];
    final AtomicInteger acked = new AtomicInteger(0);
    Callback cb = (metadata, exception) -> acked.incrementAndGet();
    Future<RecordMetadata> future1 = batch.tryAppend(now, null, value, Record.EMPTY_HEADERS, cb, now);
    Future<RecordMetadata> future2 = batch.tryAppend(now, null, value, Record.EMPTY_HEADERS, cb, now);
    assertNotNull(future1);
    assertNotNull(future2);
    batch.close();
    accum.reenqueue(batch, now);
    time.sleep(121L);
    RecordAccumulator.ReadyCheckResult result = accum.ready(metadataCache, time.milliseconds());
    assertFalse(result.readyNodes.isEmpty(), "The batch should be ready");
    Map<Integer, List<ProducerBatch>> drained = accum.drain(metadataCache, result.readyNodes, Integer.MAX_VALUE, time.milliseconds());
    assertEquals(1, drained.size(), "Only node1 should be drained");
    assertEquals(1, drained.get(node1.id()).size(), "Only one batch should be drained");
    accum.splitAndReenqueue(drained.get(node1.id()).get(0));
    time.sleep(101L);
    drained = accum.drain(metadataCache, result.readyNodes, Integer.MAX_VALUE, time.milliseconds());
    assertFalse(drained.isEmpty());
    assertFalse(drained.get(node1.id()).isEmpty());
    drained.get(node1.id()).get(0).complete(acked.get(), 100L);
    assertEquals(1, acked.get(), "The first message should have been acked.");
    assertTrue(future1.isDone());
    assertEquals(0, future1.get().offset());
    drained = accum.drain(metadataCache, result.readyNodes, Integer.MAX_VALUE, time.milliseconds());
    assertFalse(drained.isEmpty());
    assertFalse(drained.get(node1.id()).isEmpty());
    drained.get(node1.id()).get(0).complete(acked.get(), 100L);
    assertEquals(2, acked.get(), "Both message should have been acked.");
    assertTrue(future2.isDone());
    assertEquals(1, future2.get().offset());
}

```java:llm_gen

@Test
public void testSplitAndReenqueue() throws ExecutionException, InterruptedException {
    long now = time.milliseconds();
    RecordAccumulator accum = createTestRecordAccumulator(1024, 10 * 1024, CompressionType.GZIP, 10);
    ByteBuffer buffer = ByteBuffer.allocate(4096);
    MemoryRecordsBuilder builder = MemoryRecords.builder(buffer, CompressionType.NONE, TimestampType.CREATE_TIME, 0L);
    ProducerBatch batch = new ProducerBatch(tp1, builder, now, true);
    byte[] value = new byte[1024];
    final AtomicInteger acked = new AtomicInteger(0);
    Callback cb = (metadata, exception) -> acked.incrementAndGet();
    Future<RecordMetadata> future1 = batch.tryAppend(now, null, value, Record.EMPTY_HEADERS, cb, now);
    Future<RecordMetadata> future2 = batch.tryAppend(now, null, value, Record.EMPTY_HEADERS, cb, now);
    assertNotNull(future1);
    assertNotNull(future2);
    batch.close();
    accum.reenqueue(batch, now);
    time.sleep(121L);
    RecordAccumulator.ReadyCheckResult result = accum.ready(metadataCache, time.milliseconds());
    assertFalse(result.readyNodes.isEmpty(), "The batch should be ready");
    Map<Integer, List<ProducerBatch>> drained = accum.drain(metadataCache, result.readyNodes, Integer.MAX_VALUE, time.milliseconds());
    assertEquals(1, drained.size(), "Only node1 should be drained");
    assertEquals(1, drained.get(node1.id()).size(), "Only one batch should be drained");
    CompressionRatioEstimator.setEstimation(tp1.topic(), CompressionType.NONE, Math.max(1.0f, (float) drained.get(node1.id()).get(0).compressionRatio()));
    accum.splitAndReenqueue(drained.get(node1.id()).get(0));
    time.sleep(101L);
    drained = accum.drain(metadataCache, result.readyNodes, Integer.MAX_VALUE, time.milliseconds());
    assertFalse(drained.isEmpty());
    assertFalse(drained.get(node1.id()).isEmpty());
    drained.get(node1.id()).get(0).complete(acked.get(), 100L);
    assertEquals(1, acked.get(), "The first message should have been acked.");
    assertTrue(future1.isDone());
    assertEquals(0, future1.get().offset());
    drained = accum.drain(metadataCache, result.readyNodes, Integer.MAX_VALUE, time.milliseconds());
    assertFalse(drained.isEmpty());
    assertFalse(drained.get(node1.id()).isEmpty());
    drained.get(node1.id()).get(0).complete(acked.get(), 100L);
    assertEquals(2, acked.get(), "Both message should have been acked.");
    assertTrue(future2.isDone());
    assertEquals(1, future2.get().offset());
}

### 21.External Class Modification
link: https://github.com/apache/incubator-fury/commit/a0036240b8f680fe8a6ea538a5bab43cd82edf39
p_path: java/fury-core/src/main/java/org/apache/fury/type/TypeUtils.java#getElementType
t_path: java/fury-core/src/test/java/org/apache/fury/type/TypeUtilsTest.java#getElementTypeTest

```java:test_src

@Test
public void getElementTypeTest() throws NoSuchMethodException {
    TypeToken typeToken = Descriptor.getDescriptorsMap(BeanA.class).get("doubleList").getTypeToken();
    @SuppressWarnings("unchecked")
    TypeToken<?> supertype = ((TypeToken<? extends Iterable<?>>) typeToken).getSupertype(Iterable.class);
    final Type iteratorReturnType = Iterable.class.getMethod("iterator").getGenericReturnType();
    final Type nextReturnType = Iterator.class.getMethod("next").getGenericReturnType();
    assertEquals(supertype.resolveType(iteratorReturnType), new TypeToken<Iterator<Double>>() {
    });
    assertEquals(supertype.resolveType(iteratorReturnType).resolveType(nextReturnType), new TypeToken<Double>() {
    });
}

```java:test_tgt

@Test
public void getElementTypeTest() throws NoSuchMethodException, NoSuchFieldException {
    TypeRef typeRef = Descriptor.getDescriptorsMap(BeanA.class).get("doubleList").getTypeRef();
    assertEquals(new TypeRef<Optional<String>>() {
    }.resolveType(Optional.class.getDeclaredField("value").getGenericType()), TypeRef.of(String.class));
    assertEquals(new TypeRef<List<String>>() {
    }.resolveType(List.class.getMethod("size").getGenericReturnType()).getRawType(), int.class);
    @SuppressWarnings("unchecked")
    TypeRef<?> supertype = ((TypeRef<? extends Iterable<?>>) typeRef).getSupertype(Iterable.class);
    final Type iteratorReturnType = Iterable.class.getMethod("iterator").getGenericReturnType();
    final Type nextReturnType = Iterator.class.getMethod("next").getGenericReturnType();
    assertEquals(supertype.resolveType(iteratorReturnType), new TypeRef<Iterator<Double>>() {
    });
    assertEquals(supertype.resolveType(iteratorReturnType).resolveType(nextReturnType), new TypeRef<Double>() {
    });
}

```java:llm_gen

@Test
public void getElementTypeTest() throws NoSuchMethodException {
    TypeRef typeRef = Descriptor.getDescriptorsMap(BeanA.class).get("doubleList").getTypeRef();
    @SuppressWarnings("unchecked")
    TypeRef<?> supertype = ((TypeRef<? extends Iterable<?>>) typeRef).getSupertype(Iterable.class);
    final Type iteratorReturnType = Iterable.class.getMethod("iterator").getGenericReturnType();
    final Type nextReturnType = Iterator.class.getMethod("next").getGenericReturnType();
    assertEquals(supertype.resolveType(iteratorReturnType), TypeRef.of(new TypeToken<Iterator<Double>>() {}.getType()));
    assertEquals(supertype.resolveType(iteratorReturnType).resolveType(nextReturnType), TypeRef.of(new TypeToken<Double>() {}.getType()));
}

### 22.Wrong Update Direction
link: https://github.com/yahoo/elide/commit/a196f753bb0b9323de7037742c395d4c07524e3b
p_path: elide-async/src/main/java/com/yahoo/elide/async/service/storageengine/RedisResultStorageEngine.java#storeResults
t_path: elide-async/src/test/java/com/yahoo/elide/async/service/storageengine/RedisResultStorageEngineTest.java#testStoreResults

```java:test_src

@Test
public void testStoreResults() {
    String queryId = "store_results_success";
    String validOutput = "hi\nhello";
    String[] input = validOutput.split("\n");
    storeResults(queryId, Observable.fromArray(input));
    verifyResults("store_results_success", Arrays.asList(validOutput));
}

```java:test_tgt

@Test
public void testStoreResults() {
    String queryId = "store_results_success";
    String validOutput = "hi\nhello";
    String[] input = validOutput.split("\n");
    storeResults(queryId, outputStream -> write(outputStream, input));
    verifyResults("store_results_success", Arrays.asList(validOutput));
}

```java:llm_gen

@Test
public void testStoreResults() {
    String queryId = "store_results_success";
    String validOutput = "hi\nhello";
    storeResults(queryId, outputStream -> {
        try {
            outputStream.write(validOutput.getBytes());
        } catch (IOException e) {
            throw new UncheckedIOException(e);
        }
    });
    verifyResults("store_results_success", Arrays.asList(validOutput));
}

### 23.Missing Asserts
link: https://github.com/StarRocks/starrocks/commit/4a18a31ff59fc2684441fdb3312ae4a56d10c2bd
p_path: fe/fe-core/src/main/java/com/starrocks/connector/PartitionUtil.java#toPartitionValues
t_path: fe/fe-core/src/test/java/com/starrocks/connector/PartitionUtilTest.java#testToPartitionValues

```java:test_src

@Test
public void testToPartitionValues() {
    String partitionNames = "a=1/b=2/c=3";
    Assert.assertEquals(Lists.newArrayList("1", "2", "3"), toPartitionValues(partitionNames));
}

```java:test_tgt

@Test
public void testToPartitionValues() {
    Assert.assertEquals(Lists.newArrayList("1", "2", "3"), toPartitionValues("a=1/b=2/c=3"));
    Assert.assertEquals(Lists.newArrayList("1", "2=1"), toPartitionValues("a=1/b=2=1"));
    Assert.assertEquals(Lists.newArrayList("1", "2=null"), toPartitionValues("a=1/b=2=null"));
    Assert.assertEquals(Lists.newArrayList("1", "2=null", "1"), toPartitionValues("a=1/b=2=null/3=1"));
    Assert.assertEquals(Lists.newArrayList("1", "2=null", ""), toPartitionValues("a=1/b=2=null/3="));
    Assert.assertEquals(Lists.newArrayList("1", "", "1"), toPartitionValues("a=1/b=/3=1"));
}

```java:llm_gen

@Test
public void testToPartitionValues() {
    String partitionNames = "a=1/b=2/c=3";
    Assert.assertEquals(Lists.newArrayList("1", "2", "3"), toPartitionValues(partitionNames));
    Assert.assertEquals(Lists.newArrayList(), toPartitionValues("invalid"));
    Assert.assertEquals(Lists.newArrayList("value"), toPartitionValues("key=value"));
    Assert.assertEquals(Lists.newArrayList("val1", "val2"), toPartitionValues("k1=val1/k2=val2"));
}

### 24.Correct
link: https://github.com/apache/dolphinscheduler/commit/8d336def6140d01bf2d6007014a9689b237baab7
p_path: dolphinscheduler-alert/dolphinscheduler-alert-plugins/dolphinscheduler-alert-pagerduty/src/main/java/org/apache/dolphinscheduler/plugin/alert/pagerduty/PagerDutySender.java#send
t_path: dolphinscheduler-alert/dolphinscheduler-alert-plugins/dolphinscheduler-alert-pagerduty/src/test/java/org/apache/dolphinscheduler/plugin/alert/pagerduty/PagerDutySenderTest.java#testSend

```java:test_src

@Test
public void testSend() {
    PagerDutySender pagerDutySender = new PagerDutySender(pagerDutyConfig);
    AlertResult alertResult = pagerDutySender.sendPagerDutyAlter("pagerduty test title", "pagerduty test content");
    Assertions.assertEquals("false", alertResult.getStatus());
}

```java:test_tgt

@Test
public void testSend() {
    PagerDutySender pagerDutySender = new PagerDutySender(pagerDutyConfig);
    AlertResult alertResult = pagerDutySender.sendPagerDutyAlter("pagerduty test title", "pagerduty test content");
    Assertions.assertFalse(alertResult.isSuccess());
}

```java:llm_gen

@Test
public void testSend() {
    PagerDutySender pagerDutySender = new PagerDutySender(pagerDutyConfig);
    AlertResult alertResult = pagerDutySender.sendPagerDutyAlter("pagerduty test title", "pagerduty test content");
    Assertions.assertFalse(alertResult.isSuccess());
}

### 25.Assert Error
link: https://github.com/gchq/stroom/commit/6890386062a60e7ff6032e418a49f7b4b970bb15
p_path: stroom-lmdb/src/main/java/stroom/bytebuffer/PooledByteBufferOutputStream.java#release
t_path: stroom-lmdb/src/test/java/stroom/bytebuffer/TestPooledByteBufferOutputStream.java#testRelease

```java:test_src

@Test
void testRelease() throws IOException {
    ByteBufferPool byteBufferPool = getByteBufferPool();
    assertThat(byteBufferPool.getCurrentPoolSize()).isEqualTo(0);
    PooledByteBufferOutputStream pooledByteBufferOutputStream = new PooledByteBufferOutputStream(byteBufferPool, 2);
    pooledByteBufferOutputStream.write(new byte[] { 0, 0 });
    pooledByteBufferOutputStream.getPooledByteBuffer().release();
    assertThat(byteBufferPool.getCurrentPoolSize()).isEqualTo(1);
    pooledByteBufferOutputStream.release();
    assertThat(byteBufferPool.getCurrentPoolSize()).isEqualTo(1);
}

```java:test_tgt

@Test
void testRelease() throws IOException {
    ByteBufferPool byteBufferPool = getByteBufferPool();
    assertThat(byteBufferPool.getCurrentPoolSize()).isEqualTo(0);
    try (PooledByteBufferOutputStream pooledByteBufferOutputStream = new PooledByteBufferOutputStream(byteBufferPool, 2)) {
        pooledByteBufferOutputStream.write(new byte[] { 0, 0 });
        assertThat(byteBufferPool.getCurrentPoolSize()).isEqualTo(0);
    }
    assertThat(byteBufferPool.getCurrentPoolSize()).isEqualTo(1);
}

```java:llm_gen

@Test
void testRelease() throws IOException {
    ByteBufferPool byteBufferPool = getByteBufferPool();
    assertThat(byteBufferPool.getCurrentPoolSize()).isEqualTo(0);
    PooledByteBufferOutputStream pooledByteBufferOutputStream = new PooledByteBufferOutputStream(byteBufferPool, 2);
    pooledByteBufferOutputStream.write(new byte[] { 0, 0 });
    pooledByteBufferOutputStream.getPooledByteBuffer().close();
    assertThat(byteBufferPool.getCurrentPoolSize()).isEqualTo(1);
    pooledByteBufferOutputStream.release();
    assertThat(byteBufferPool.getCurrentPoolSize()).isEqualTo(1);
}

### 26.External Class Modification
link: https://github.com/opendaylight/controller/commit/02b74456a89b728e2c32ade1523b509b0ff74f4d
p_path: opendaylight/md-sal/sal-cluster-admin-impl/src/main/java/org/opendaylight/controller/cluster/datastore/admin/ClusterAdminRpcService.java#changeMemberVotingStatesForShard
t_path: opendaylight/md-sal/sal-cluster-admin-impl/src/test/java/org/opendaylight/controller/cluster/datastore/admin/ClusterAdminRpcServiceTest.java#testChangeMemberVotingStatesForShard

```java:test_src

@Test
public void testChangeMemberVotingStatesForShard() throws Exception {
    String name = "testChangeMemberVotingStatusForShard";
    String moduleShardsConfig = "module-shards-member1-and-2-and-3.conf";
    final MemberNode leaderNode1 = MemberNode.builder(memberNodes).akkaConfig("Member1").testName(name).moduleShardsConfig(moduleShardsConfig).datastoreContextBuilder(DatastoreContext.newBuilder().shardHeartbeatIntervalInMillis(300).shardElectionTimeoutFactor(1)).build();
    final MemberNode replicaNode2 = MemberNode.builder(memberNodes).akkaConfig("Member2").testName(name).moduleShardsConfig(moduleShardsConfig).build();
    final MemberNode replicaNode3 = MemberNode.builder(memberNodes).akkaConfig("Member3").testName(name).moduleShardsConfig(moduleShardsConfig).build();
    leaderNode1.configDataStore().waitTillReady();
    replicaNode3.configDataStore().waitTillReady();
    verifyRaftPeersPresent(leaderNode1.configDataStore(), "cars", "member-2", "member-3");
    verifyRaftPeersPresent(replicaNode2.configDataStore(), "cars", "member-1", "member-3");
    verifyRaftPeersPresent(replicaNode3.configDataStore(), "cars", "member-1", "member-2");
    final ClusterAdminRpcService service3 = new ClusterAdminRpcService(replicaNode3.configDataStore(), replicaNode3.operDataStore(), null, null);
    RpcResult<ChangeMemberVotingStatesForShardOutput> rpcResult = service3.changeMemberVotingStatesForShard(new ChangeMemberVotingStatesForShardInputBuilder().setShardName("cars").setDataStoreType(DataStoreType.Config).setMemberVotingState(List.of(new MemberVotingStateBuilder().setMemberName("member-2").setVoting(FALSE).build(), new MemberVotingStateBuilder().setMemberName("member-3").setVoting(FALSE).build())).build()).get(10, TimeUnit.SECONDS);
    verifySuccessfulRpcResult(rpcResult);
    verifyVotingStates(leaderNode1.configDataStore(), "cars", new SimpleEntry<>("member-1", TRUE), new SimpleEntry<>("member-2", FALSE), new SimpleEntry<>("member-3", FALSE));
    verifyVotingStates(replicaNode2.configDataStore(), "cars", new SimpleEntry<>("member-1", TRUE), new SimpleEntry<>("member-2", FALSE), new SimpleEntry<>("member-3", FALSE));
    verifyVotingStates(replicaNode3.configDataStore(), "cars", new SimpleEntry<>("member-1", TRUE), new SimpleEntry<>("member-2", FALSE), new SimpleEntry<>("member-3", FALSE));
}

```java:test_tgt

@Test
public void testChangeMemberVotingStatesForShard() throws Exception {
    String name = "testChangeMemberVotingStatusForShard";
    String moduleShardsConfig = "module-shards-member1-and-2-and-3.conf";
    final MemberNode leaderNode1 = MemberNode.builder(memberNodes).akkaConfig("Member1").testName(name).moduleShardsConfig(moduleShardsConfig).datastoreContextBuilder(DatastoreContext.newBuilder().shardHeartbeatIntervalInMillis(300).shardElectionTimeoutFactor(1)).build();
    final MemberNode replicaNode2 = MemberNode.builder(memberNodes).akkaConfig("Member2").testName(name).moduleShardsConfig(moduleShardsConfig).build();
    final MemberNode replicaNode3 = MemberNode.builder(memberNodes).akkaConfig("Member3").testName(name).moduleShardsConfig(moduleShardsConfig).build();
    leaderNode1.configDataStore().waitTillReady();
    replicaNode3.configDataStore().waitTillReady();
    verifyRaftPeersPresent(leaderNode1.configDataStore(), "cars", "member-2", "member-3");
    verifyRaftPeersPresent(replicaNode2.configDataStore(), "cars", "member-1", "member-3");
    verifyRaftPeersPresent(replicaNode3.configDataStore(), "cars", "member-1", "member-2");
    final var service3 = new ClusterAdminRpcService(replicaNode3.configDataStore(), replicaNode3.operDataStore(), null);
    var rpcResult = service3.changeMemberVotingStatesForShard(new ChangeMemberVotingStatesForShardInputBuilder().setShardName("cars").setDataStoreType(DataStoreType.Config).setMemberVotingState(List.of(new MemberVotingStateBuilder().setMemberName("member-2").setVoting(FALSE).build(), new MemberVotingStateBuilder().setMemberName("member-3").setVoting(FALSE).build())).build()).get(10, TimeUnit.SECONDS);
    verifySuccessfulRpcResult(rpcResult);
    verifyVotingStates(leaderNode1.configDataStore(), "cars", new SimpleEntry<>("member-1", TRUE), new SimpleEntry<>("member-2", FALSE), new SimpleEntry<>("member-3", FALSE));
    verifyVotingStates(replicaNode2.configDataStore(), "cars", new SimpleEntry<>("member-1", TRUE), new SimpleEntry<>("member-2", FALSE), new SimpleEntry<>("member-3", FALSE));
    verifyVotingStates(replicaNode3.configDataStore(), "cars", new SimpleEntry<>("member-1", TRUE), new SimpleEntry<>("member-2", FALSE), new SimpleEntry<>("member-3", FALSE));
}

```java:llm_gen

@Test
public void testChangeMemberVotingStatesForShard() throws Exception {
    String name = "testChangeMemberVotingStatusForShard";
    String moduleShardsConfig = "module-shards-member1-and-2-and-3.conf";
    final var leaderNode1 = MemberNode.builder(memberNodes).akkaConfig("Member1").testName(name).moduleShardsConfig(moduleShardsConfig).datastoreContextBuilder(DatastoreContext.newBuilder().shardHeartbeatIntervalInMillis(300).shardElectionTimeoutFactor(1)).build();
    final var replicaNode2 = MemberNode.builder(memberNodes).akkaConfig("Member2").testName(name).moduleShardsConfig(moduleShardsConfig).build();
    final var replicaNode3 = MemberNode.builder(memberNodes).akkaConfig("Member3").testName(name).moduleShardsConfig(moduleShardsConfig).build();
    leaderNode1.configDataStore().waitTillReady();
    replicaNode3.configDataStore().waitTillReady();
    verifyRaftPeersPresent(leaderNode1.configDataStore(), "cars", "member-2", "member-3");
    verifyRaftPeersPresent(replicaNode2.configDataStore(), "cars", "member-1", "member-3");
    verifyRaftPeersPresent(replicaNode3.configDataStore(), "cars", "member-1", "member-2");
    final var service3 = new ClusterAdminRpcService(replicaNode3.configDataStore(), replicaNode3.operDataStore(), null, null);
    RpcResult<ChangeMemberVotingStatesForShardOutput> rpcResult = service3.changeMemberVotingStatesForShard(new ChangeMemberVotingStatesForShardInputBuilder().setShardName("cars").setDataStoreType(DataStoreType.Config).setMemberVotingState(List.of(new MemberVotingStateBuilder().setMemberName("member-2").setVoting(FALSE).build(), new MemberVotingStateBuilder().setMemberName("member-3").setVoting(FALSE).build())).build()).get(10, TimeUnit.SECONDS);
    verifySuccessfulRpcResult(rpcResult);
    verifyVotingStates(leaderNode1.configDataStore(), "cars", new SimpleEntry<>("member-1", TRUE), new SimpleEntry<>("member-2", FALSE), new SimpleEntry<>("member-3", FALSE));
    verifyVotingStates(replicaNode2.configDataStore(), "cars", new SimpleEntry<>("member-1", TRUE), new SimpleEntry<>("member-2", FALSE), new SimpleEntry<>("member-3", FALSE));
    verifyVotingStates(replicaNode3.configDataStore(), "cars", new SimpleEntry<>("member-1", TRUE), new SimpleEntry<>("member-2", FALSE), new SimpleEntry<>("member-3", FALSE));
}

### 27.Pure Syntax Error
link: https://github.com/apache/kafka/commit/7e5ef9b509a00973d271def5f70ca2062208e778
p_path: metadata/src/main/java/org/apache/kafka/controller/PartitionChangeBuilder.java#changeRecordIsNoOp
t_path: metadata/src/test/java/org/apache/kafka/controller/PartitionChangeBuilderTest.java#testChangeRecordIsNoOp

```java:test_src

@Test
public void testChangeRecordIsNoOp() {
    assertEquals(2, PartitionChangeRecord.HIGHEST_SUPPORTED_VERSION);
    assertEquals(0, PartitionChangeRecord.LOWEST_SUPPORTED_VERSION);
    TaggedFields taggedFields = (TaggedFields) PartitionChangeRecord.SCHEMA_0.get(2).def.type;
    assertEquals(6, taggedFields.numFields());
    assertTrue(changeRecordIsNoOp(new PartitionChangeRecord()));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setLeader(1)));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setIsr(Arrays.asList(1, 2, 3))));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setRemovingReplicas(Arrays.asList(1))));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setAddingReplicas(Arrays.asList(4))));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setEligibleLeaderReplicas(Arrays.asList(5))));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setLastKnownELR(Arrays.asList(6))));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setLeaderRecoveryState(LeaderRecoveryState.RECOVERED.value())));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setDirectories(Arrays.asList(Uuid.fromString("5JwD0VNXRV2Wr9CCON38Tw"), Uuid.fromString("zpL1bRzTQXmmgdxlLHOWuw"), Uuid.fromString("6iGUpAkHQXC6bY0FTcPRDw")))));
}

```java:test_tgt

@Test
public void testChangeRecordIsNoOp() {
    assertEquals(2, PartitionChangeRecord.HIGHEST_SUPPORTED_VERSION);
    assertEquals(0, PartitionChangeRecord.LOWEST_SUPPORTED_VERSION);
    TaggedFields taggedFields = (TaggedFields) PartitionChangeRecord.SCHEMA_0.get(2).def.type;
    assertEquals(6, taggedFields.numFields());
    assertTrue(changeRecordIsNoOp(new PartitionChangeRecord()));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setLeader(1)));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setIsr(Arrays.asList(1, 2, 3))));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setRemovingReplicas(Arrays.asList(1))));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setAddingReplicas(Arrays.asList(4))));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setEligibleLeaderReplicas(Arrays.asList(5))));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setLastKnownElr(Arrays.asList(6))));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setLeaderRecoveryState(LeaderRecoveryState.RECOVERED.value())));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setDirectories(Arrays.asList(Uuid.fromString("5JwD0VNXRV2Wr9CCON38Tw"), Uuid.fromString("zpL1bRzTQXmmgdxlLHOWuw"), Uuid.fromString("6iGUpAkHQXC6bY0FTcPRDw")))));
}

```java:llm_gen

@Test
public void testChangeRecordIsNoOp() {
    assertEquals(2, PartitionChangeRecord.HIGHEST_SUPPORTED_VERSION);
    assertEquals(0, PartitionChangeRecord.LOWEST_SUPPORTED_VERSION);
    TaggedFields taggedFields = (TaggedFields) PartitionChangeRecord.SCHEMA_0.get(2).def.type;
    assertEquals(6, taggedFields.numFields());
    assertTrue(changeRecordIsNoOp(new PartitionChangeRecord()));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setLeader(1)));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setIsr(Arrays.asList(1, 2, 3))));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setRemovingReplicas(Arrays.asList(1))));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setAddingReplicas(Arrays.asList(4))));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setEligibleLeaderReplicas(Arrays.asList(5))));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setLastKnownElr(Arrays.asList(6))));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setLeaderRecoveryState(LeaderRecoveryState.RECOVERED.value())));
    assertFalse(changeRecordIsNoOp(new PartitionChangeRecord().setDirectories(Arrays.asList(Uuid.fromString("5JwD0VNXRV2Wr9CCON38Tw"), Uuid.fromString("zpL1bRzTQXmmgdxlLHOWuw"), Uuid.fromString("6iGUpAkHQXC6bY0FTcPRDw"))));
}

### 28.Correct
link: https://github.com/microcks/microcks/commit/2b4bc2f9faf64896463257d37c12dba89cfb4179
p_path: webapp/src/main/java/io/github/microcks/util/RelativeReferenceURLBuilderFactory.java#getRelativeReferenceURLBuilder
t_path: webapp/src/test/java/io/github/microcks/util/RelativeReferenceURLBuilderFactoryTest.java#testGetRelativeReferenceURLBuilder

```java:test_src

@Test
public void testGetRelativeReferenceURLBuilder() {
    RelativeReferenceURLBuilder builder = RelativeReferenceURLBuilderFactory.getRelativeReferenceURLBuilder(null);
    assertTrue(builder instanceof SimpleReferenceURLBuilder);
    Map<String, List<String>> properties = Map.of("key", List.of("value1", "value2"));
    builder = RelativeReferenceURLBuilderFactory.getRelativeReferenceURLBuilder(properties);
    assertTrue(builder instanceof SimpleReferenceURLBuilder);
    properties = Map.of(GitLabReferenceURLBuilder.GITLAB_FILE_NAME_HEADER, List.of("value1", "value2"));
    builder = RelativeReferenceURLBuilderFactory.getRelativeReferenceURLBuilder(properties);
    assertTrue(builder instanceof GitLabReferenceURLBuilder);
}

```java:test_tgt

@Test
public void testGetRelativeReferenceURLBuilder() {
    RelativeReferenceURLBuilder builder = RelativeReferenceURLBuilderFactory.getRelativeReferenceURLBuilder(null);
    assertTrue(builder instanceof SimpleReferenceURLBuilder);
    Map<String, List<String>> properties = Map.of("key", List.of("value1", "value2"));
    builder = RelativeReferenceURLBuilderFactory.getRelativeReferenceURLBuilder(properties);
    assertTrue(builder instanceof SimpleReferenceURLBuilder);
    properties = Map.of(GitLabReferenceURLBuilder.GITLAB_FILE_NAME_HEADER, List.of("value1", "value2"));
    builder = RelativeReferenceURLBuilderFactory.getRelativeReferenceURLBuilder(properties);
    assertTrue(builder instanceof GitLabReferenceURLBuilder);
    properties = Map.of(GitLabReferenceURLBuilder.GITLAB_FILE_NAME_HEADER.toLowerCase(), List.of("value1", "value2"));
    builder = RelativeReferenceURLBuilderFactory.getRelativeReferenceURLBuilder(properties);
    assertTrue(builder instanceof GitLabReferenceURLBuilder);
}

```java:llm_gen

@Test
public void testGetRelativeReferenceURLBuilder() {
    RelativeReferenceURLBuilder builder = RelativeReferenceURLBuilderFactory.getRelativeReferenceURLBuilder(null);
    assertTrue(builder instanceof SimpleReferenceURLBuilder);
    Map<String, List<String>> properties = Map.of("key", List.of("value1", "value2"));
    builder = RelativeReferenceURLBuilderFactory.getRelativeReferenceURLBuilder(properties);
    assertTrue(builder instanceof SimpleReferenceURLBuilder);
    properties = Map.of(GitLabReferenceURLBuilder.GITLAB_FILE_NAME_HEADER, List.of("value1", "value2"));
    builder = RelativeReferenceURLBuilderFactory.getRelativeReferenceURLBuilder(properties);
    assertTrue(builder instanceof GitLabReferenceURLBuilder);
    properties = Map.of(GitLabReferenceURLBuilder.GITLAB_FILE_NAME_HEADER.toLowerCase(), List.of("value1", "value2"));
    builder = RelativeReferenceURLBuilderFactory.getRelativeReferenceURLBuilder(properties);
    assertTrue(builder instanceof GitLabReferenceURLBuilder);
}

### 29.Assert Error
link: https://github.com/Haehnchen/idea-php-symfony2-plugin/commit/75293c3a0ed76d80698bffaa1c0b0245b581cead
p_path: src/main/java/fr/adrienbrault/idea/symfony2plugin/completion/IncompletePropertyServiceInjectionContributor.java#appendPropertyInjection
t_path: src/test/java/fr/adrienbrault/idea/symfony2plugin/tests/completion/IncompletePropertyServiceInjectionContributorTest.java#testAppendPropertyInjection

```java:test_src

public void testAppendPropertyInjection() {
    PhpClass fromText = PhpPsiElementFactory.createFromText(getProject(), PhpClass.class, "<?php\n" + "\n" + "class Foobar\n" + "{\n" + "    public function __construct(private readonly \\DateTime $d)\n" + "    {\n" + "    }\n" + "}");
    IncompletePropertyServiceInjectionContributor.appendPropertyInjection(fromText, "router", "\\Symfony\\Component\\Routing\\Generator\\UrlGeneratorInterface");
    String text = fromText.getText();
    assertTrue(text.contains("public function __construct(private readonly \\DateTime $d,private readonly UrlGeneratorInterface $router)"));
    PhpClass fromText2 = PhpPsiElementFactory.createFromText(getProject(), PhpClass.class, "<?php\n" + "\n" + "class Foobar\n" + "{\n" + "}");
    IncompletePropertyServiceInjectionContributor.appendPropertyInjection(fromText2, "router", "\\Symfony\\Component\\Routing\\Generator\\UrlGeneratorInterface");
    String text2 = fromText2.getText();
    assertTrue(text2.contains("public function __construct(UrlGeneratorInterface $router)"));
}

```java:test_tgt

public void testAppendPropertyInjection() {
    PhpClass fromText = PhpPsiElementFactory.createFromText(getProject(), PhpClass.class, "<?php\n" + "\n" + "class Foobar\n" + "{\n" + "    public function __construct(private readonly \\DateTime $d)\n" + "    {\n" + "    }\n" + "}");
    IncompletePropertyServiceInjectionContributor.appendPropertyInjection(fromText, "router", "\\Symfony\\Component\\Routing\\Generator\\UrlGeneratorInterface");
    String text = fromText.getText();
    assertTrue(text.contains("public function __construct(private readonly \\DateTime $d,private readonly UrlGeneratorInterface $router)"));
    PhpClass fromText2 = PhpPsiElementFactory.createFromText(getProject(), PhpClass.class, "<?php\n" + "\n" + "class Foobar\n" + "{\n" + "}");
    IncompletePropertyServiceInjectionContributor.appendPropertyInjection(fromText2, "router", "\\Symfony\\Component\\Routing\\Generator\\UrlGeneratorInterface");
    String text2 = fromText2.getText();
    assertTrue(text2.contains("public function __construct(UrlGeneratorInterface $router)"));
    PhpClass fromText3 = PhpPsiElementFactory.createFromText(getProject(), PhpClass.class, "<?php\n" + "\n" + "readonly class Foobar\n" + "{\n" + "    public function __construct(private readonly \\DateTime $d)\n" + "    {\n" + "    }\n" + "}");
    IncompletePropertyServiceInjectionContributor.appendPropertyInjection(fromText3, "router", "\\Symfony\\Component\\Routing\\Generator\\UrlGeneratorInterface");
    String text3 = fromText3.getText();
    assertTrue(text3.contains("public function __construct(private readonly \\DateTime $d,private UrlGeneratorInterface $router)"));
}

```java:llm_gen

public void testAppendPropertyInjection() {
    PhpClass fromText = PhpPsiElementFactory.createFromText(getProject(), PhpClass.class, "<?php\n" + "\n" + "class Foobar\n" + "{\n" + "    public function __construct(private readonly \\DateTime $d)\n" + "    {\n" + "    }\n" + "}");
    IncompletePropertyServiceInjectionContributor.appendPropertyInjection(fromText, "router", "\\Symfony\\Component\\Routing\\Generator\\UrlGeneratorInterface");
    String text = fromText.getText();
    assertTrue(text.contains("public function __construct(private readonly \\DateTime $d,private readonly UrlGeneratorInterface $router)"));

    PhpClass fromText2 = PhpPsiElementFactory.createFromText(getProject(), PhpClass.class, "<?php\n" + "\n" + "class Foobar\n" + "{\n" + "}");
    IncompletePropertyServiceInjectionContributor.appendPropertyInjection(fromText2, "router", "\\Symfony\\Component\\Routing\\Generator\\UrlGeneratorInterface");
    String text2 = fromText2.getText();
    assertTrue(text2.contains("public function __construct(private UrlGeneratorInterface $router)"));

    PhpClass fromText3 = PhpPsiElementFactory.createFromText(getProject(), PhpClass.class, "<?php\n" + "\n" + "readonly class Foobar\n" + "{\n" + "    public function __construct(private \\DateTime $d)\n" + "    {\n" + "    }\n" + "}");
    IncompletePropertyServiceInjectionContributor.appendPropertyInjection(fromText3, "router", "\\Symfony\\Component\\Routing\\Generator\\UrlGeneratorInterface");
    String text3 = fromText3.getText();
    assertTrue(text3.contains("public function __construct(private \\DateTime $d,private UrlGeneratorInterface $router)"));
}

### 30.Correct
link: https://github.com/apache/hudi/commit/23b283acf3e4c30e26652edf9c710e17e47951c5
p_path: hudi-common/src/main/java/org/apache/hudi/common/table/TableSchemaResolver.java#readSchemaFromLogFile
t_path: hudi-hadoop-common/src/test/java/org/apache/hudi/common/table/TestTableSchemaResolver.java#testReadSchemaFromLogFile

```java:test_src

@Test
public void testReadSchemaFromLogFile() throws IOException, URISyntaxException, InterruptedException {
    String testDir = initTestDir("read_schema_from_log_file");
    StoragePath partitionPath = new StoragePath(testDir, "partition1");
    Schema expectedSchema = getSimpleSchema();
    StoragePath logFilePath = writeLogFile(partitionPath, expectedSchema);
    assertEquals(new AvroSchemaConverter().convert(expectedSchema), TableSchemaResolver.readSchemaFromLogFile(HoodieStorageUtils.getStorage(logFilePath, HoodieTestUtils.getDefaultStorageConfWithDefaults()), logFilePath));
}

```java:test_tgt

@Test
public void testReadSchemaFromLogFile() throws IOException, URISyntaxException, InterruptedException {
    String testDir = initTestDir("read_schema_from_log_file");
    StoragePath partitionPath = new StoragePath(testDir, "partition1");
    Schema expectedSchema = getSimpleSchema();
    StoragePath logFilePath = writeLogFile(partitionPath, expectedSchema);
    assertEquals(expectedSchema, TableSchemaResolver.readSchemaFromLogFile(HoodieStorageUtils.getStorage(logFilePath, HoodieTestUtils.getDefaultStorageConfWithDefaults()), logFilePath));
}

```java:llm_gen

@Test
public void testReadSchemaFromLogFile() throws IOException, URISyntaxException, InterruptedException {
    String testDir = initTestDir("read_schema_from_log_file");
    StoragePath partitionPath = new StoragePath(testDir, "partition1");
    Schema expectedSchema = getSimpleSchema();
    StoragePath logFilePath = writeLogFile(partitionPath, expectedSchema);
    assertEquals(expectedSchema, TableSchemaResolver.readSchemaFromLogFile(HoodieStorageUtils.getStorage(logFilePath, HoodieTestUtils.getDefaultStorageConfWithDefaults()), logFilePath));
}

### 31.Additional Asserts
link: https://github.com/StarRocks/starrocks/commit/952bc956276f35b51e239eaceda8659a2eded4b1
p_path: fe/fe-core/src/main/java/com/starrocks/lake/Utils.java#chooseBackend
t_path: fe/fe-core/src/test/java/com/starrocks/lake/UtilsTest.java#testChooseBackend

```java:test_src

@Test
public void testChooseBackend() {
    new MockUp<GlobalStateMgr>() {
        @Mock
        public SystemInfoService getCurrentSystemInfo() {
            return systemInfoService;
        }
    };
    new MockUp<LakeTablet>() {
        @Mock
        public long getPrimaryComputeNodeId(long clusterId) throws UserException {
            throw new UserException("Failed to get primary backend");
        }
    };
    new MockUp<SystemInfoService>() {
        @Mock
        public Long seqChooseBackendOrComputeId() throws UserException {
            throw new UserException("No backend or compute node alive.");
        }
    };
    Assert.assertNull(Utils.chooseBackend(new LakeTablet(1000L)));
}

```java:test_tgt

@Test
public void testChooseBackend() {
    new MockUp<GlobalStateMgr>() {
        @Mock
        public NodeMgr getNodeMgr() {
            return nodeMgr;
        }
    };
    new MockUp<NodeMgr>() {
        @Mock
        public SystemInfoService getClusterInfo() {
            return systemInfoService;
        }
    };
    new MockUp<LakeTablet>() {
        @Mock
        public long getPrimaryComputeNodeId(long clusterId) throws UserException {
            throw new UserException("Failed to get primary backend");
        }
    };
    new MockUp<SystemInfoService>() {
        @Mock
        public Long seqChooseBackendOrComputeId() throws UserException {
            throw new UserException("No backend or compute node alive.");
        }
    };
    Assert.assertNull(Utils.chooseBackend(new LakeTablet(1000L)));
}

```java:llm_gen

@Test
public void testChooseBackend() {
    new MockUp<GlobalStateMgr>() {
        @Mock
        public WarehouseMgr getWarehouseMgr() {
            return warehouseMgr;
        }
        @Mock
        public NodeMgr getNodeMgr() {
            return nodeMgr;
        }
    };
    new MockUp<LakeTablet>() {
        @Mock
        public long getPrimaryComputeNodeId(long clusterId) throws UserException {
            throw new UserException("Failed to get primary backend");
        }
    };
    new MockUp<ClusterInfo>() {
        @Mock
        public Long seqChooseBackendOrComputeId() throws UserException {
            throw new UserException("No backend or compute node alive.");
        }
    };
    Assert.assertNull(Utils.chooseBackend(new LakeTablet(1000L)));
}

### 32.Wrong Update Direction
link: https://github.com/openhab/openhab-core/commit/1b503afdbbc654e0d845dce7c713813cf652ead5
p_path: bundles/org.openhab.core.persistence/src/main/java/org/openhab/core/persistence/extensions/PersistenceExtensions.java#countSince
t_path: bundles/org.openhab.core.persistence/src/test/java/org/openhab/core/persistence/extensions/PersistenceExtensionsTest.java#testCountSince

```java:test_src

@Test
public void testCountSince() {
    long counts = PersistenceExtensions.countSince(numberItem, ZonedDateTime.of(1980, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), TestPersistenceService.ID);
    assertEquals(33, counts);
    counts = PersistenceExtensions.countSince(numberItem, ZonedDateTime.of(2007, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), TestPersistenceService.ID);
    assertEquals(6, counts);
    counts = PersistenceExtensions.countSince(numberItem, ZonedDateTime.of(2020, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), TestPersistenceService.ID);
    assertEquals(0, counts);
    counts = PersistenceExtensions.countSince(numberItem, ZonedDateTime.of(2000, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()));
    assertEquals(0, counts);
}

```java:test_tgt

@Test
public void testCountSince() {
    Long counts = PersistenceExtensions.countSince(numberItem, ZonedDateTime.of(HISTORIC_INTERMEDIATE_VALUE_1, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), SERVICE_ID);
    assertEquals(HISTORIC_END - HISTORIC_INTERMEDIATE_VALUE_1 + 1, counts);
    counts = PersistenceExtensions.countSince(numberItem, ZonedDateTime.of(HISTORIC_INTERMEDIATE_VALUE_2, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), SERVICE_ID);
    assertEquals(HISTORIC_END - HISTORIC_INTERMEDIATE_VALUE_2 + 1, counts);
    counts = PersistenceExtensions.countSince(numberItem, ZonedDateTime.of(HISTORIC_INTERMEDIATE_NOVALUE_3, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), SERVICE_ID);
    assertEquals(0, counts);
    counts = PersistenceExtensions.countSince(numberItem, ZonedDateTime.of(HISTORIC_INTERMEDIATE_VALUE_1, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()));
    assertNull(counts);
}

```java:llm_gen

@Test
public void testCountSince() {
    Long counts = PersistenceExtensions.countSince(numberItem, ZonedDateTime.of(1980, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), TestPersistenceService.ID);
    assertEquals(33L, counts != null ? counts : 0L);
    counts = PersistenceExtensions.countSince(numberItem, ZonedDateTime.of(2007, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), TestPersistenceService.ID);
    assertEquals(6L, counts != null ? counts : 0L);
    counts = PersistenceExtensions.countSince(numberItem, ZonedDateTime.of(2020, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), TestPersistenceService.ID);
    assertEquals(0L, counts != null ? counts : 0L);
    counts = PersistenceExtensions.countSince(numberItem, ZonedDateTime.of(2000, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), null);
    assertEquals(0L, counts != null ? counts : 0L);
}

### 33.Missing Asserts
link: https://github.com/Haehnchen/idea-php-symfony2-plugin/commit/feefbd8fd95097fb6689e76ba45e8523d0a6d588
p_path: src/main/java/fr/adrienbrault/idea/symfony2plugin/routing/RouteHelper.java#isServiceController
t_path: src/test/java/fr/adrienbrault/idea/symfony2plugin/tests/routing/RouteHelperTest.java#testIsServiceController

```java:test_src

public void testIsServiceController() {
    assertTrue(RouteHelper.isServiceController("Foo:foo"));
    assertTrue(RouteHelper.isServiceController("Foo\\Bar:foo"));
    assertFalse(RouteHelper.isServiceController("Foo::bar"));
    assertFalse(RouteHelper.isServiceController("Foo"));
    assertFalse(RouteHelper.isServiceController("Foo:bar:foo"));
}

```java:test_tgt

public void testIsServiceController() {
    assertTrue(RouteHelper.isServiceController("Foo:foo"));
    assertTrue(RouteHelper.isServiceController("Foo\\Bar:foo"));
    assertTrue(RouteHelper.isServiceController("Foo\\Bar::foo"));
    assertTrue(RouteHelper.isServiceController("Foo::bar"));
    assertTrue(RouteHelper.isServiceController("web_profiler.controller.profiler::homeAction"));
    assertFalse(RouteHelper.isServiceController("Foo"));
    assertFalse(RouteHelper.isServiceController("Foo:bar:foo"));
}

```java:llm_gen

public void testIsServiceController() {
    assertTrue(RouteHelper.isServiceController("Foo:foo"));
    assertTrue(RouteHelper.isServiceController("Foo\\Bar:foo"));
    assertTrue(RouteHelper.isServiceController("Foo::bar"));
    assertFalse(RouteHelper.isServiceController("Foo"));
    assertFalse(RouteHelper.isServiceController("Foo:bar:foo"));
}

### 34.Test Preparation Error
link: https://github.com/halo-dev/halo/commit/0e17d53ede66c57b12f2dec4c92874c7e69ed9ef
p_path: application/src/main/java/run/halo/app/notification/DefaultNotificationCenter.java#createNotification
t_path: application/src/test/java/run/halo/app/notification/DefaultNotificationCenterTest.java#testCreateNotification

````java:test_src

@Test
public void testCreateNotification() {
    var element = mock(DefaultNotificationCenter.NotificationElement.class);
    var subscription = createSubscriptions().get(0);
    var user = mock(User.class);
    var subscriberName = subscription.getSpec().getSubscriber().getName();
    when(client.fetch(eq(User.class), eq(subscriberName))).thenReturn(Mono.just(user));
    when(element.subscription()).thenReturn(subscription);
    when(client.create(any(Notification.class))).thenReturn(Mono.empty());
    var reason = new Reason();
    reason.setMetadata(new Metadata());
    reason.getMetadata().setName("reason-a");
    reason.setSpec(new Reason.Spec());
    reason.getSpec().setReasonType("new-reply-on-comment");
    when(element.reason()).thenReturn(reason);
    notificationCenter.createNotification(element).block();
    verify(client).fetch(eq(User.class), eq(subscriberName));
    verify(client).create(any(Notification.class));
}

```java:test_tgt

@Test
public void testCreateNotification() {
    var element = mock(DefaultNotificationCenter.NotificationElement.class);
    var subscription = createSubscriptions().get(0);
    var user = mock(User.class);
    var subscriptionName = subscription.getMetadata().getName();
    var subscriber = new Subscriber(UserIdentity.of(subscription.getSpec().getSubscriber().getName()), subscriptionName);
    when(client.fetch(eq(User.class), eq(subscriber.name()))).thenReturn(Mono.just(user));
    when(element.subscriber()).thenReturn(subscriber);
    when(client.create(any(Notification.class))).thenReturn(Mono.empty());
    var reason = new Reason();
    reason.setMetadata(new Metadata());
    reason.getMetadata().setName("reason-a");
    reason.setSpec(new Reason.Spec());
    reason.getSpec().setReasonType("new-reply-on-comment");
    when(element.reason()).thenReturn(reason);
    notificationCenter.createNotification(element).block();
    verify(client).fetch(eq(User.class), eq(subscriber.name()));
    verify(client).create(any(Notification.class));
}

```java:llm_gen

@Test
public void testCreateNotification() {
    var element = mock(DefaultNotificationCenter.NotificationElement.class);
    var user = mock(User.class);
    var subscriber = mock(Subscriber.class);
    var subscriberName = "test-subscriber";
    when(subscriber.name()).thenReturn(subscriberName);
    when(client.fetch(eq(User.class), eq(subscriberName))).thenReturn(Mono.just(user));
    when(element.subscriber()).thenReturn(subscriber);
    when(client.create(any(Notification.class))).thenReturn(Mono.empty());
    var reason = new Reason();
    reason.setMetadata(new Metadata());
    reason.getMetadata().setName("reason-a");
    reason.setSpec(new Reason.Spec());
    reason.getSpec().setReasonType("new-reply-on-comment");
    when(element.reason()).thenReturn(reason);
    notificationCenter.createNotification(element).block();
    verify(client).fetch(eq(User.class), eq(subscriberName));
    verify(client).create(any(Notification.class));
}

### 35.External Class Modification
link: https://github.com/BentoBoxWorld/BentoBox/commit/b1fe76c45d693b6bbd3f4d87e013041fcb341934
p_path: src/main/java/world/bentobox/bentobox/api/commands/island/team/IslandTeamCommand.java#removeInvite
t_path: src/test/java/world/bentobox/bentobox/api/commands/island/team/IslandTeamCommandTest.java#testRemoveInvite

```java:test_src

@Test
public void testRemoveInvite() {
    assertNull(tc.getInvite(invitee));
    tc.addInvite(Invite.Type.TEAM, uuid, invitee, island);
    tc.removeInvite(invitee);
    assertNull(tc.getInvite(invitee));
}

```java:test_tgt

@Test
public void testRemoveInvite() {
    assertNull(tc.getInvite(invitee));
    tc.addInvite(Type.TEAM, uuid, invitee, island);
    tc.removeInvite(invitee);
    assertNull(tc.getInvite(invitee));
}

```java:llm_gen

@Test
public void testRemoveInvite() {
    assertNull(tc.getInvite(invitee));
    tc.addInvite(Invite.Type.TEAM, uuid, invitee, island);
    tc.removeInvite(invitee);
    verify(handler).deleteID(invitee.toString());
    assertNull(tc.getInvite(invitee));
}

### 36.Correct
link: https://github.com/embulk/embulk/commit/ea1e0bc6cea2f1688327f2bc81fd19e64aa17459
p_path: embulk-core/src/main/java/org/embulk/plugin/PluginClassLoader.java#isParentFirstPath
t_path: embulk-core/src/test/java/org/embulk/plugin/TestPluginClassLoader.java#testIsParentFirstPath
```java:test_src

@Test
public void testIsParentFirstPath() {
    assertFalse(PluginClassLoader.isParentFirstPath(""));
    assertFalse(PluginClassLoader.isParentFirstPath("foo/bar.txt"));
    assertFalse(PluginClassLoader.isParentFirstPath("ch/qos/logback/core/dummy.txt"));
    assertFalse(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/boolexe/Dummy"));
    assertTrue(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/boolex/IEvaluator"));
    assertFalse(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/boolex"));
    assertTrue(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/boolex/"));
    assertFalse(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/db/script"));
    assertTrue(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/db/script/"));
    assertTrue(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/db/script/postgresql.sql"));
    assertFalse(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/db/scripts/dummy.sql"));
    assertFalse(PluginClassLoader.isParentFirstPath("embulk"));
    assertTrue(PluginClassLoader.isParentFirstPath("embulk/"));
    assertTrue(PluginClassLoader.isParentFirstPath("embulk/logback-file.xml"));
    assertFalse(PluginClassLoader.isParentFirstPath("embulkdummy/logback-file.xml"));
    assertFalse(PluginClassLoader.isParentFirstPath("msgpack"));
    assertTrue(PluginClassLoader.isParentFirstPath("msgpack/"));
    assertTrue(PluginClassLoader.isParentFirstPath("msgpack/dummy.txt"));
    assertFalse(PluginClassLoader.isParentFirstPath("msgpacker/dummy.txt"));
    assertFalse(PluginClassLoader.isParentFirstPath("org/embulk"));
    assertTrue(PluginClassLoader.isParentFirstPath("org/embulk/"));
    assertTrue(PluginClassLoader.isParentFirstPath("org/embulk/jruby/bundler/template/Gemfile"));
    assertFalse(PluginClassLoader.isParentFirstPath("org/embulkdummy/jruby/bundler/template/Gemfile"));
}

```java:test_tgt

@Test
public void testIsParentFirstPath() {
    assertFalse(PluginClassLoader.isParentFirstPath(""));
    assertFalse(PluginClassLoader.isParentFirstPath("foo/bar.txt"));
    assertFalse(PluginClassLoader.isParentFirstPath("ch/qos/logback/core/dummy.txt"));
    assertFalse(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/boolexe/Dummy"));
    assertTrue(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/boolex/IEvaluator"));
    assertFalse(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/boolex"));
    assertTrue(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/boolex/"));
    assertFalse(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/db/script"));
    assertTrue(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/db/script/"));
    assertTrue(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/db/script/postgresql.sql"));
    assertFalse(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/db/scripts/dummy.sql"));
    assertFalse(PluginClassLoader.isParentFirstPath("embulk"));
    assertTrue(PluginClassLoader.isParentFirstPath("embulk/"));
    assertTrue(PluginClassLoader.isParentFirstPath("embulk/logback-file.xml"));
    assertFalse(PluginClassLoader.isParentFirstPath("embulkdummy/logback-file.xml"));
    assertFalse(PluginClassLoader.isParentFirstPath("msgpack"));
    assertFalse(PluginClassLoader.isParentFirstPath("msgpack/"));
    assertFalse(PluginClassLoader.isParentFirstPath("msgpack/dummy.txt"));
    assertFalse(PluginClassLoader.isParentFirstPath("msgpacker/dummy.txt"));
    assertFalse(PluginClassLoader.isParentFirstPath("org/embulk"));
    assertTrue(PluginClassLoader.isParentFirstPath("org/embulk/"));
    assertTrue(PluginClassLoader.isParentFirstPath("org/embulk/jruby/bundler/template/Gemfile"));
    assertFalse(PluginClassLoader.isParentFirstPath("org/embulkdummy/jruby/bundler/template/Gemfile"));
}

```java:llm_gen

@Test
public void testIsParentFirstPath() {
    assertFalse(PluginClassLoader.isParentFirstPath(""));
    assertFalse(PluginClassLoader.isParentFirstPath("foo/bar.txt"));
    assertFalse(PluginClassLoader.isParentFirstPath("ch/qos/logback/core/dummy.txt"));
    assertFalse(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/boolexe/Dummy"));
    assertTrue(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/boolex/IEvaluator"));
    assertFalse(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/boolex"));
    assertTrue(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/boolex/"));
    assertFalse(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/db/script"));
    assertTrue(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/db/script/"));
    assertTrue(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/db/script/postgresql.sql"));
    assertFalse(PluginClassLoader.isParentFirstPath("ch/qos/logback/classic/db/scripts/dummy.sql"));
    assertFalse(PluginClassLoader.isParentFirstPath("embulk"));
    assertTrue(PluginClassLoader.isParentFirstPath("embulk/"));
    assertTrue(PluginClassLoader.isParentFirstPath("embulk/logback-file.xml"));
    assertFalse(PluginClassLoader.isParentFirstPath("embulkdummy/logback-file.xml"));
    assertFalse(PluginClassLoader.isParentFirstPath("msgpack"));
    assertFalse(PluginClassLoader.isParentFirstPath("msgpack/"));
    assertFalse(PluginClassLoader.isParentFirstPath("msgpack/dummy.txt"));
    assertFalse(PluginClassLoader.isParentFirstPath("msgpacker/dummy.txt"));
    assertFalse(PluginClassLoader.isParentFirstPath("org/embulk"));
    assertTrue(PluginClassLoader.isParentFirstPath("org/embulk/"));
    assertTrue(PluginClassLoader.isParentFirstPath("org/embulk/jruby/bundler/template/Gemfile"));
    assertFalse(PluginClassLoader.isParentFirstPath("org/embulkdummy/jruby/bundler/template/Gemfile"));
}

### 37.Correct
link: https://github.com/dhis2/dhis2-core/commit/820376735c0a47c0f82050ca30847b70de96f63a
p_path: dhis-2/dhis-api/src/main/java/org/hisp/dhis/dataanalysis/DataAnalysisStore.java#getDataAnalysisMeasures
t_path: dhis-2/dhis-test-integration/src/test/java/org/hisp/dhis/dataanalysis/DataAnalysisStoreTest.java#testGetDataAnalysisMeasures

```java:test_src

@Test
void testGetDataAnalysisMeasures() {
    dataValueService.addDataValue(createDataValue(dataElementA, periodA, organisationUnitA, "5", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodB, organisationUnitA, "2", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodC, organisationUnitA, "1", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodD, organisationUnitA, "12", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodE, organisationUnitA, "10", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodF, organisationUnitA, "7", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodG, organisationUnitA, "52", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodH, organisationUnitA, "23", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodI, organisationUnitA, "3", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodJ, organisationUnitA, "15", categoryOptionCombo));
    List<DataAnalysisMeasures> measures = dataAnalysisStore.getDataAnalysisMeasures(dataElementA, Lists.newArrayList(categoryOptionCombo), Lists.newArrayList(organisationUnitA.getPath()), from);
    assertEquals(1, measures.size());
    assertEquals(measures.get(0).getAverage(), DELTA, 12.78);
    assertEquals(measures.get(0).getStandardDeviation(), DELTA, 15.26);
}

```java:test_tgt

@Test
void testGetDataAnalysisMeasures() {
    dataValueService.addDataValue(createDataValue(dataElementA, periodA, organisationUnitA, "5", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodB, organisationUnitA, "2", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodC, organisationUnitA, "1", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodD, organisationUnitA, "12", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodE, organisationUnitA, "10", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodF, organisationUnitA, "7", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodG, organisationUnitA, "52", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodH, organisationUnitA, "23", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodI, organisationUnitA, "3", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodJ, organisationUnitA, "15", categoryOptionCombo));
    List<DataAnalysisMeasures> measures = dataAnalysisStore.getDataAnalysisMeasures(dataElementA, Lists.newArrayList(categoryOptionCombo), organisationUnitA, from);
    assertEquals(1, measures.size());
    assertEquals(measures.get(0).getAverage(), DELTA, 12.78);
    assertEquals(measures.get(0).getStandardDeviation(), DELTA, 15.26);
}

```java:llm_gen

@Test
void testGetDataAnalysisMeasures() {
    dataValueService.addDataValue(createDataValue(dataElementA, periodA, organisationUnitA, "5", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodB, organisationUnitA, "2", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodC, organisationUnitA, "1", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodD, organisationUnitA, "12", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodE, organisationUnitA, "10", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodF, organisationUnitA, "7", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodG, organisationUnitA, "52", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodH, organisationUnitA, "23", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodI, organisationUnitA, "3", categoryOptionCombo));
    dataValueService.addDataValue(createDataValue(dataElementA, periodJ, organisationUnitA, "15", categoryOptionCombo));
    List<DataAnalysisMeasures> measures = dataAnalysisStore.getDataAnalysisMeasures(dataElementA, Lists.newArrayList(categoryOptionCombo), organisationUnitA, from);
    assertEquals(1, measures.size());
    assertEquals(measures.get(0).getAverage(), DELTA, 12.78);
    assertEquals(measures.get(0).getStandardDeviation(), DELTA, 15.26);
}

### 38.Missing Asserts
link: https://github.com/apache/jackrabbit-oak/commit/dadff28010f820c2c22fa2944e66fe5ec5225ecf
p_path: oak-auth-external/src/main/java/org/apache/jackrabbit/oak/spi/security/authentication/external/impl/DynamicSyncContext.java#convertToDynamicMembership
t_path: oak-auth-external/src/test/java/org/apache/jackrabbit/oak/spi/security/authentication/external/impl/DynamicSyncContextTest.java#testConvertToDynamicMembership

```java:test_src

@Test
public void testConvertToDynamicMembership() throws Exception {
    User user = userManager.getAuthorizable(PREVIOUS_SYNCED_ID, User.class);
    assertNotNull(user);
    assertFalse(user.hasProperty(REP_EXTERNAL_PRINCIPAL_NAMES));
    assertTrue(syncContext.convertToDynamicMembership(user));
    assertTrue(user.hasProperty(REP_EXTERNAL_PRINCIPAL_NAMES));
    assertDeclaredGroups(previouslySyncedUser);
}

```java:test_tgt

@Test
public void testConvertToDynamicMembership() throws Exception {
    User user = userManager.getAuthorizable(PREVIOUS_SYNCED_ID, User.class);
    assertNotNull(user);
    assertFalse(user.hasProperty(REP_EXTERNAL_PRINCIPAL_NAMES));
    assertFalse(user.hasProperty(REP_LAST_DYNAMIC_SYNC));
    assertTrue(syncContext.convertToDynamicMembership(user));
    assertTrue(user.hasProperty(REP_EXTERNAL_PRINCIPAL_NAMES));
    assertTrue(user.hasProperty(REP_LAST_DYNAMIC_SYNC));
    assertDeclaredGroups(previouslySyncedUser);
}

```java:llm_gen

@Test
public void testConvertToDynamicMembership() throws Exception {
    User user = userManager.getAuthorizable(PREVIOUS_SYNCED_ID, User.class);
    assertNotNull(user);
    assertFalse(user.hasProperty(REP_EXTERNAL_PRINCIPAL_NAMES));
    assertTrue(syncContext.convertToDynamicMembership(user));
    assertTrue(user.hasProperty(REP_EXTERNAL_PRINCIPAL_NAMES));
    assertDeclaredGroups(previouslySyncedUser);
}

### 39.Correct
link: https://github.com/apache/shenyu/commit/e27a26b8ca3de5c167dc676f22d280f217cd1e5f
p_path: shenyu-plugin/shenyu-plugin-proxy/shenyu-plugin-springcloud/src/main/java/org/apache/shenyu/plugin/springcloud/context/SpringCloudShenyuContextDecorator.java#decorator
t_path: shenyu-plugin/shenyu-plugin-proxy/shenyu-plugin-springcloud/src/test/java/org/apache/shenyu/plugin/springcloud/context/SpringCloudShenyuContextDecoratorTest.java#testDecorator

```java:test_src

@Test
public void testDecorator() {
    MetaData metaData = null;
    ShenyuContext shenyuContext = new ShenyuContext();
    springCloudShenyuContextDecorator.decorator(shenyuContext, metaData);
    Assertions.assertNull(shenyuContext.getMethod());
    Assertions.assertNull(shenyuContext.getRealUrl());
    Assertions.assertEquals(shenyuContext.getRpcType(), "springCloud");
    Assertions.assertEquals(shenyuContext.getModule(), "divide-springCloud");
}

```java:test_tgt

@Test
public void testDecorator() {
    MetaData metaData = null;
    ShenyuContext shenyuContext = new ShenyuContext();
    springCloudShenyuContextDecorator.decorator(shenyuContext, metaData);
    Assertions.assertNull(shenyuContext.getMethod());
    Assertions.assertNull(shenyuContext.getRealUrl());
    Assertions.assertEquals(shenyuContext.getRpcType(), "springCloud");
    Assertions.assertEquals(shenyuContext.getModule(), "springCloud-springCloud");
}

```java:llm_gen

@Test
public void testDecorator() {
    MetaData metaData = null;
    ShenyuContext shenyuContext = new ShenyuContext();
    springCloudShenyuContextDecorator.decorator(shenyuContext, metaData);
    Assertions.assertNull(shenyuContext.getMethod());
    Assertions.assertNull(shenyuContext.getRealUrl());
    Assertions.assertEquals(shenyuContext.getRpcType(), "springCloud");
    Assertions.assertEquals(shenyuContext.getModule(), "springCloud-springCloud");
}

### 40.Missing Asserts
link: https://github.com/JumpMind/symmetric-ds/commit/6472f7c7181a330871141f1f95cacb29d7caddf9
p_path: symmetric-core/src/main/java/org/jumpmind/symmetric/common/ConfigurationVersionHelper.java#filterNodes
t_path: symmetric-core/src/test/java/org/jumpmind/symmetric/common/ConfigurationVersionHelperTest.java#testFilterNodes

```java:test_src

public void testFilterNodes(boolean isPro) {
    ConfigurationVersionHelper helper = new ConfigurationVersionHelper(PREFIX);
    Map<String, List<String>> versionWithTables = getVersionWithTables();
    List<String> versions = new ArrayList<String>(versionWithTables.keySet());
    versions.sort(new Comparator<String>() {
        @Override
        public int compare(String s1, String s2) {
            return s1.equals(s2) ? 0 : Version.isOlderThanVersion(s1, s2) ? -1 : 1;
        }
    });
    Set<Node> nodes = new HashSet<Node>();
    for (String version : versions) {
        Node node = new Node(version, version);
        node.setSymmetricVersion(version);
        node.setDeploymentType(isPro ? Constants.DEPLOYMENT_TYPE_PROFESSIONAL : Constants.DEPLOYMENT_TYPE_SERVER);
        nodes.add(node);
    }
    List<String> shouldSendTables = TableConstants.getConfigTables(PREFIX);
    List<String> shouldNotSendTables = new ArrayList<String>();
    for (String table : TableConstants.getConfigTablesByVersion(PREFIX).keySet()) {
        shouldSendTables.remove(table);
        shouldNotSendTables.add(table);
    }
    Set<String> proTables = TableConstants.getTablesForConsole(PREFIX);
    for (String version : versions) {
        List<String> newTables = versionWithTables.get(version);
        if (newTables != null) {
            for (String table : newTables) {
                if (isPro || !proTables.contains(table)) {
                    shouldSendTables.add(table);
                    shouldNotSendTables.remove(table);
                }
            }
        }
        for (String table : shouldSendTables) {
            Set<Node> filteredNodes = helper.filterNodes(nodes, table);
            assertTrue("Should send table " + table + " to node " + version, filteredNodes.contains(new Node(version, version)));
        }
        for (String table : shouldNotSendTables) {
            Set<Node> filteredNodes = helper.filterNodes(nodes, table);
            assertFalse("Should NOT send table " + table + " to node " + version, filteredNodes.contains(new Node(version, version)));
        }
    }
}

```java:test_tgt

public void testFilterNodes(boolean isPro) {
    ConfigurationVersionHelper helper = new ConfigurationVersionHelper(PREFIX);
    Map<String, List<String>> versionWithTables = getVersionWithTables();
    List<String> versions = new ArrayList<String>(versionWithTables.keySet());
    versions.sort(new Comparator<String>() {
        @Override
        public int compare(String s1, String s2) {
            return s1.equals(s2) ? 0 : Version.isOlderThanVersion(s1, s2) ? -1 : 1;
        }
    });
    Set<Node> nodes = new HashSet<Node>();
    for (String version : versions) {
        Node node = new Node(version, version);
        node.setSymmetricVersion(version);
        node.setDeploymentType(isPro ? Constants.DEPLOYMENT_TYPE_PROFESSIONAL : Constants.DEPLOYMENT_TYPE_SERVER);
        nodes.add(node);
    }
    List<String> shouldSendTables = TableConstants.getConfigTables(PREFIX);
    List<String> shouldNotSendTables = new ArrayList<String>();
    for (String table : TableConstants.getConfigTablesByVersion(PREFIX).keySet()) {
        shouldSendTables.remove(table);
        shouldNotSendTables.add(table);
    }
    Set<String> proTables = TableConstants.getTablesForConsole(PREFIX);
    for (String version : versions) {
        List<String> newTables = versionWithTables.get(version);
        if (newTables != null) {
            for (String table : newTables) {
                if (isPro || !proTables.contains(table)) {
                    shouldSendTables.add(table);
                    shouldNotSendTables.remove(table);
                }
            }
        }
        Map<String, String> columnValues = new HashMap<String, String>();
        columnValues.put("TYPE", "cpu");
        for (String table : shouldSendTables) {
            if (table.equalsIgnoreCase(TableConstants.getTableName(PREFIX, TableConstants.SYM_MONITOR))) {
                columnValues.put("TYPE", "cpu");
            }
            Set<Node> filteredNodes = helper.filterNodes(nodes, table, columnValues);
            assertTrue("Should send table " + table + " to node " + version, filteredNodes.contains(new Node(version, version)));
        }
        for (String table : shouldNotSendTables) {
            Set<Node> filteredNodes = helper.filterNodes(nodes, table, columnValues);
            assertFalse("Should NOT send table " + table + " to node " + version, filteredNodes.contains(new Node(version, version)));
        }
    }
}

```java:llm_gen

public void testFilterNodes(boolean isPro) {
    ConfigurationVersionHelper helper = new ConfigurationVersionHelper(PREFIX);
    Map<String, List<String>> versionWithTables = getVersionWithTables();
    List<String> versions = new ArrayList<String>(versionWithTables.keySet());
    versions.sort(new Comparator<String>() {
        @Override
        public int compare(String s1, String s2) {
            return s1.equals(s2) ? 0 : Version.isOlderThanVersion(s1, s2) ? -1 : 1;
        }
    });
    Set<Node> nodes = new HashSet<Node>();
    for (String version : versions) {
        Node node = new Node(version, version);
        node.setSymmetricVersion(version);
        node.setDeploymentType(isPro ? Constants.DEPLOYMENT_TYPE_PROFESSIONAL : Constants.DEPLOYMENT_TYPE_SERVER);
        nodes.add(node);
    }
    List<String> shouldSendTables = TableConstants.getConfigTables(PREFIX);
    List<String> shouldNotSendTables = new ArrayList<String>();
    for (String table : TableConstants.getConfigTablesByVersion(PREFIX).keySet()) {
        shouldSendTables.remove(table);
        shouldNotSendTables.add(table);
    }
    Set<String> proTables = TableConstants.getTablesForConsole(PREFIX);
    String monitorTable = TableConstants.getTableName(PREFIX, TableConstants.SYM_MONITOR);
    shouldSendTables.add(monitorTable);
    shouldNotSendTables.remove(monitorTable);
    for (String version : versions) {
        List<String> newTables = versionWithTables.get(version);
        if (newTables != null) {
            for (String table : newTables) {
                if (isPro || !proTables.contains(table)) {
                    shouldSendTables.add(table);
                    shouldNotSendTables.remove(table);
                }
            }
        }
        for (String table : shouldSendTables) {
            Set<Node> filteredNodes = helper.filterNodes(nodes, table, new HashMap<String, String>());
            assertTrue("Should send table " + table + " to node " + version, filteredNodes.contains(new Node(version, version)));
        }
        for (String table : shouldNotSendTables) {
            Set<Node> filteredNodes = helper.filterNodes(nodes, table, new HashMap<String, String>());
            assertFalse("Should NOT send table " + table + " to node " + version, filteredNodes.contains(new Node(version, version)));
        }
    }
}

### 41.Field/Package Information Modification
link: https://github.com/alibaba/nacos/commit/5c19ac12ad6137bf1155bdc6d53d2eaa9350838e
p_path: client/src/main/java/com/alibaba/nacos/client/logging/NacosLogging.java#loadConfiguration
t_path: client/src/test/java/com/alibaba/nacos/client/logging/NacosLoggingTest.java#testLoadConfiguration

```java:test_src

@Test
public void testLoadConfiguration() throws NoSuchFieldException, IllegalAccessException {
    NacosLogging instance = NacosLogging.getInstance();
    AbstractNacosLogging mockLogging = Mockito.mock(AbstractNacosLogging.class);
    Field nacosLogging = NacosLogging.class.getDeclaredField("nacosLogging");
    nacosLogging.setAccessible(true);
    nacosLogging.set(instance, mockLogging);
    instance.loadConfiguration();
    Mockito.verify(mockLogging, Mockito.times(1)).loadConfiguration();
}

```java:test_tgt

@Test
public void testLoadConfiguration() throws NoSuchFieldException, IllegalAccessException {
    instance = NacosLogging.getInstance();
    Field nacosLogging = NacosLogging.class.getDeclaredField("loggingAdapter");
    nacosLogging.setAccessible(true);
    nacosLogging.set(instance, loggingAdapter);
    instance.loadConfiguration();
    Mockito.verify(loggingAdapter, Mockito.times(1)).loadConfiguration(loggingProperties);
}

```java:llm_gen

@Test
public void testLoadConfiguration() throws NoSuchFieldException, IllegalAccessException {
    NacosLogging instance = NacosLogging.getInstance();
    LoggingAdapter mockLoggingAdapter = Mockito.mock(LoggingAdapter.class);
    Field loggingAdapter = NacosLogging.class.getDeclaredField("loggingAdapter");
    loggingAdapter.setAccessible(true);
    loggingAdapter.set(instance, mockLoggingAdapter);
    LoggingProperties mockLoggingProperties = Mockito.mock(LoggingProperties.class);
    Field loggingProperties = NacosLogging.class.getDeclaredField("loggingProperties");
    loggingProperties.setAccessible(true);
    loggingProperties.set(instance, mockLoggingProperties);
    instance.loadConfiguration();
    Mockito.verify(mockLoggingAdapter, Mockito.times(1)).loadConfiguration(mockLoggingProperties);
}

### 42.Test Preparation Error
link: https://github.com/apache/rocketmq/commit/026a910b26899f38c062e282fcc5592ed40e03df
p_path: tieredstore/src/main/java/org/apache/rocketmq/tieredstore/TieredMessageStore.java#getOffsetInQueueByTime
t_path: tieredstore/src/test/java/org/apache/rocketmq/tieredstore/TieredMessageStoreTest.java#testGetOffsetInQueueByTime

```java:test_src

@Test
public void testGetOffsetInQueueByTime() {
    Mockito.when(fetcher.getOffsetInQueueByTime(anyString(), anyInt(), anyLong(), eq(BoundaryType.LOWER))).thenReturn(1L);
    Mockito.when(nextStore.getOffsetInQueueByTime(anyString(), anyInt(), anyLong())).thenReturn(2L);
    Mockito.when(nextStore.getEarliestMessageTime()).thenReturn(100L);
    Assert.assertEquals(1, store.getOffsetInQueueByTime(mq.getTopic(), mq.getQueueId(), 0, BoundaryType.LOWER));
    Assert.assertEquals(2, store.getOffsetInQueueByTime(mq.getTopic(), mq.getQueueId(), 1000, BoundaryType.LOWER));
    Mockito.when(fetcher.getOffsetInQueueByTime(anyString(), anyInt(), anyLong(), eq(BoundaryType.LOWER))).thenReturn(-1L);
    Assert.assertEquals(2, store.getOffsetInQueueByTime(mq.getTopic(), mq.getQueueId(), 0, BoundaryType.LOWER));
}

```java:test_tgt

@Test
public void testGetOffsetInQueueByTime() {
    Properties properties = new Properties();
    properties.setProperty("tieredStorageLevel", "FORCE");
    configuration.update(properties);
    Mockito.when(fetcher.getOffsetInQueueByTime(anyString(), anyInt(), anyLong(), eq(BoundaryType.LOWER))).thenReturn(1L);
    Mockito.when(defaultStore.getOffsetInQueueByTime(anyString(), anyInt(), anyLong())).thenReturn(2L);
    Mockito.when(defaultStore.getEarliestMessageTime()).thenReturn(100L);
    Assert.assertEquals(1L, currentStore.getOffsetInQueueByTime(mq.getTopic(), mq.getQueueId(), 1000, BoundaryType.LOWER));
    Assert.assertEquals(1L, currentStore.getOffsetInQueueByTime(mq.getTopic(), mq.getQueueId(), 0, BoundaryType.LOWER));
    Mockito.when(fetcher.getOffsetInQueueByTime(anyString(), anyInt(), anyLong(), eq(BoundaryType.LOWER))).thenReturn(-1L);
    Assert.assertEquals(-1L, currentStore.getOffsetInQueueByTime(mq.getTopic(), mq.getQueueId(), 0));
    Assert.assertEquals(-1L, currentStore.getOffsetInQueueByTime(mq.getTopic(), mq.getQueueId(), 0, BoundaryType.LOWER));
}

```java:llm_gen

@Test
public void testGetOffsetInQueueByTime() {
    Mockito.when(fetcher.getOffsetInQueueByTime(anyString(), anyInt(), anyLong(), eq(BoundaryType.LOWER))).thenReturn(1L);
    Mockito.when(nextStore.getOffsetInQueueByTime(anyString(), anyInt(), anyLong())).thenReturn(2L);
    Mockito.when(nextStore.getEarliestMessageTime()).thenReturn(100L);
    Mockito.when(storeConfig.getTieredStorageLevel()).thenReturn(MessageStoreConfig.TieredStorageLevel.NOT_FORCE);
    Assert.assertEquals(1, store.getOffsetInQueueByTime(mq.getTopic(), mq.getQueueId(), 0, BoundaryType.LOWER));
    Assert.assertEquals(2, store.getOffsetInQueueByTime(mq.getTopic(), mq.getQueueId(), 1000, BoundaryType.LOWER));
    Mockito.when(fetcher.getOffsetInQueueByTime(anyString(), anyInt(), anyLong(), eq(BoundaryType.LOWER))).thenReturn(-1L);
    Assert.assertEquals(2, store.getOffsetInQueueByTime(mq.getTopic(), mq.getQueueId(), 0, BoundaryType.LOWER));
    Mockito.when(storeConfig.getTieredStorageLevel()).thenReturn(MessageStoreConfig.TieredStorageLevel.FORCE);
    Assert.assertEquals(-1L, store.getOffsetInQueueByTime(mq.getTopic(), mq.getQueueId(), 0, BoundaryType.LOWER));
}

### 43.Correct
link: https://github.com/apache/kafka/commit/bf88013a2812cab65bc70667e451e0a15d26b73c
p_path: group-coordinator/src/main/java/org/apache/kafka/coordinator/group/CoordinatorRecordHelpers.java#newCurrentAssignmentTombstoneRecord
t_path: group-coordinator/src/test/java/org/apache/kafka/coordinator/group/CoordinatorRecordHelpersTest.java#testNewCurrentAssignmentTombstoneRecord

```java:test_src

@Test
public void testNewCurrentAssignmentTombstoneRecord() {
    Record expectedRecord = new Record(new ApiMessageAndVersion(new ConsumerGroupCurrentMemberAssignmentKey().setGroupId("group-id").setMemberId("member-id"), (short) 8), null);
    assertEquals(expectedRecord, newCurrentAssignmentTombstoneRecord("group-id", "member-id"));
}

```java:test_tgt

@Test
public void testNewCurrentAssignmentTombstoneRecord() {
    CoordinatorRecord expectedRecord = new CoordinatorRecord(new ApiMessageAndVersion(new ConsumerGroupCurrentMemberAssignmentKey().setGroupId("group-id").setMemberId("member-id"), (short) 8), null);
    assertEquals(expectedRecord, newCurrentAssignmentTombstoneRecord("group-id", "member-id"));
}

```java:llm_gen

@Test
public void testNewCurrentAssignmentTombstoneRecord() {
    CoordinatorRecord expectedRecord = new CoordinatorRecord(new ApiMessageAndVersion(new ConsumerGroupCurrentMemberAssignmentKey().setGroupId("group-id").setMemberId("member-id"), (short) 8), null);
    assertEquals(expectedRecord, newCurrentAssignmentTombstoneRecord("group-id", "member-id"));
}

### 44.Field/Package Information Modification
link: https://github.com/linkedin/venice/commit/a67317be52c384469674e6dee89f2a6648371daa
p_path: internal/venice-client-common/src/main/java/com/linkedin/venice/serializer/AvroSerializer.java#serialize
t_path: internal/venice-client-common/src/test/java/com/linkedin/venice/serializer/AvroSerializerTest.java#testSerialize

```java:test_src

@Test
public void testSerialize() {
    byte[] serializedValue = serializer.serialize(value);
    Assert.assertTrue(serializedValue.length > value.getBytes().length);
}

```java:test_tgt

@Test
public void testSerialize() {
    byte[] serializedValue = RECORD_SERIALIZER.serialize(value);
    Assert.assertTrue(serializedValue.length > value.getBytes().length);
}

```java:llm_gen

@Test
public void testSerialize() {
    byte[] serializedValue = serializer.serialize(value);
    Assert.assertTrue(serializedValue.length > value.getBytes().length);
}


### 45.External Class Modification
link: https://github.com/questdb/questdb/commit/95e5cf3a3d2d0be9c1ec2449af94868c5dfc87a6
p_path: core/src/main/java/io/questdb/cairo/map/OrderedMap.java#mergeVarSizeKey
t_path: core/src/test/java/io/questdb/test/cairo/map/OrderedMapTest.java#testMergeVarSizeKey

```java:test_src

@Test
public void testMergeVarSizeKey() {
    ArrayColumnTypes keyTypes = new ArrayColumnTypes();
    keyTypes.add(ColumnType.INT);
    keyTypes.add(ColumnType.STRING);
    ArrayColumnTypes valueTypes = new ArrayColumnTypes();
    valueTypes.add(ColumnType.LONG);
    try (FastMap mapA = new FastMap(1024, keyTypes, valueTypes, 64, 0.8, 24);
        FastMap mapB = new FastMap(1024, keyTypes, valueTypes, 64, 0.8, 24)) {
        final int N = 100000;
        for (int i = 0; i < N; i++) {
            MapKey keyA = mapA.withKey();
            keyA.putInt(i);
            keyA.putStr(Chars.repeat("a", i % 32));
            MapValue valueA = keyA.createValue();
            Assert.assertTrue(valueA.isNew());
            valueA.putLong(0, i + 2);
        }
        for (int i = 0; i < 2 * N; i++) {
            MapKey keyB = mapB.withKey();
            keyB.putInt(i);
            keyB.putStr(Chars.repeat("a", i % 32));
            MapValue valueB = keyB.createValue();
            Assert.assertTrue(valueB.isNew());
            valueB.putLong(0, i + 2);
        }
        Assert.assertEquals(2 * mapA.size(), mapB.size());
        mapA.merge(mapB, new TestMapValueMergeFunction());
        Assert.assertEquals(mapA.size(), mapB.size());
        RecordCursor cursorA = mapA.getCursor();
        MapRecord recordA = mapA.getRecord();
        while (cursorA.hasNext()) {
            int i = recordA.getInt(1);
            MapValue valueA = recordA.getValue();
            MapKey keyB = mapB.withKey();
            keyB.putInt(i);
            keyB.putStr(Chars.repeat("a", i % 32));
            MapValue valueB = keyB.findValue();
            Assert.assertFalse(valueB.isNew());
            if (i < N) {
                Assert.assertEquals(valueA.getLong(0), 2 * valueB.getLong(0));
            } else {
                Assert.assertEquals(valueA.getLong(0), valueB.getLong(0));
            }
        }
    }
}

```java:test_tgt

@Test
public void testMergeVarSizeKey() throws Exception {
    TestUtils.assertMemoryLeak(() -> {
        ArrayColumnTypes keyTypes = new ArrayColumnTypes();
        keyTypes.add(ColumnType.INT);
        keyTypes.add(ColumnType.STRING);
        ArrayColumnTypes valueTypes = new ArrayColumnTypes();
        valueTypes.add(ColumnType.LONG);
        try (OrderedMap mapA = new OrderedMap(1024, keyTypes, valueTypes, 64, 0.8, 24);
            OrderedMap mapB = new OrderedMap(1024, keyTypes, valueTypes, 64, 0.8, 24)) {
            final int N = 100000;
            for (int i = 0; i < N; i++) {
                MapKey keyA = mapA.withKey();
                keyA.putInt(i);
                keyA.putStr(Chars.repeat("a", i % 32));
                MapValue valueA = keyA.createValue();
                Assert.assertTrue(valueA.isNew());
                valueA.putLong(0, i + 2);
            }
            for (int i = 0; i < 2 * N; i++) {
                MapKey keyB = mapB.withKey();
                keyB.putInt(i);
                keyB.putStr(Chars.repeat("a", i % 32));
                MapValue valueB = keyB.createValue();
                Assert.assertTrue(valueB.isNew());
                valueB.putLong(0, i + 2);
            }
            Assert.assertEquals(2 * mapA.size(), mapB.size());
            mapA.merge(mapB, new TestMapValueMergeFunction());
            Assert.assertEquals(mapA.size(), mapB.size());
            RecordCursor cursorA = mapA.getCursor();
            MapRecord recordA = mapA.getRecord();
            while (cursorA.hasNext()) {
                int i = recordA.getInt(1);
                MapValue valueA = recordA.getValue();
                MapKey keyB = mapB.withKey();
                keyB.putInt(i);
                keyB.putStr(Chars.repeat("a", i % 32));
                MapValue valueB = keyB.findValue();
                Assert.assertFalse(valueB.isNew());
                if (i < N) {
                    Assert.assertEquals(valueA.getLong(0), 2 * valueB.getLong(0));
                } else {
                    Assert.assertEquals(valueA.getLong(0), valueB.getLong(0));
                }
            }
        }
    });
}

```java:llm_gen

@Test
public void testMergeVarSizeKey() {
    ArrayColumnTypes keyTypes = new ArrayColumnTypes();
    keyTypes.add(ColumnType.INT);
    keyTypes.add(ColumnType.STRING);
    ArrayColumnTypes valueTypes = new ArrayColumnTypes();
    valueTypes.add(ColumnType.LONG);
    try (FastMap mapA = new FastMap(1024, keyTypes, valueTypes, 64, 0.8, 24);
        FastMap mapB = new FastMap(1024, keyTypes, valueTypes, 64, 0.8, 24)) {
        final int N = 100000;
        for (int i = 0; i < N; i++) {
            MapKey keyA = mapA.withKey();
            keyA.putInt(i);
            keyA.putStr(Chars.repeat("a", i % 32));
            MapValue valueA = keyA.createValue();
            Assert.assertTrue(valueA.isNew());
            valueA.putLong(0, i + 2);
        }
        for (int i = 0; i < 2 * N; i++) {
            MapKey keyB = mapB.withKey();
            keyB.putInt(i);
            keyB.putStr(Chars.repeat("a", i % 32));
            MapValue valueB = keyB.createValue();
            Assert.assertTrue(valueB.isNew());
            valueB.putLong(0, i + 2);
        }
        Assert.assertEquals(2 * mapA.size(), mapB.size());
        mapA.merge(mapB, new TestMapValueMergeFunction());
        Assert.assertEquals(mapA.size(), mapB.size());
        RecordCursor cursorA = mapA.getCursor();
        MapRecord recordA = mapA.getRecord();
        while (cursorA.hasNext()) {
            int i = recordA.getInt(1);
            MapValue valueA = recordA.getValue();
            MapKey keyB = mapB.withKey();
            keyB.putInt(i);
            keyB.putStr(Chars.repeat("a", i % 32));
            MapValue valueB = keyB.findValue();
            Assert.assertFalse(valueB.isNew());
            if (i < N) {
                Assert.assertEquals(valueA.getLong(0), 2 * valueB.getLong(0));
            } else {
                Assert.assertEquals(valueA.getLong(0), valueB.getLong(0));
            }
        }
    }
}

### 46.Additional Asserts
link: https://github.com/linkedin/venice/commit/49382976f1e5bdd6b280313381cae12267889325
p_path: clients/venice-push-job/src/main/java/com/linkedin/venice/hadoop/VenicePushJob.java#getPushJobSetting
t_path: clients/venice-push-job/src/test/java/com/linkedin/venice/hadoop/VenicePushJobTest.java#testGetPushJobSetting

```java:test_src

@Test
public void testGetPushJobSetting() {
    Properties props = getVpjRequiredProperties();
    try (VenicePushJob vpj = new VenicePushJob(PUSH_JOB_ID, props)) {
        VenicePushJob.PushJobSetting pushJobSetting = vpj.getPushJobSetting();
        assertNotNull(pushJobSetting);
        assertTrue(pushJobSetting.d2Routing);
    }
}

```java:test_tgt

@Test
public void testGetPushJobSetting() {
    Properties props = getVpjRequiredProperties();
    try (VenicePushJob vpj = new VenicePushJob(PUSH_JOB_ID, props)) {
        PushJobSetting pushJobSetting = vpj.getPushJobSetting();
        assertNotNull(pushJobSetting);
        assertTrue(pushJobSetting.d2Routing);
    }
}

```java:llm_gen

@Test
public void testGetPushJobSetting() {
    Properties props = getVpjRequiredProperties();
    try (VenicePushJob vpj = new VenicePushJob(PUSH_JOB_ID, props)) {
        VenicePushJob.PushJobSetting pushJobSetting = vpj.getPushJobSetting();
        assertNotNull(pushJobSetting);
        assertEquals(PUSH_JOB_ID, pushJobSetting.jobId);
        assertEquals("unknown_exec_id", pushJobSetting.jobExecutionId);
        assertEquals("unknown_job_server", pushJobSetting.jobServerName);
        assertFalse(pushJobSetting.enableSSL);
        assertEquals(VenicePushJob.class, pushJobSetting.vpjEntryClass);
        assertFalse(pushJobSetting.suppressEndOfPushMessage);
        assertFalse(pushJobSetting.deferVersionSwap);
        assertFalse(pushJobSetting.repushTTLEnabled);
        assertFalse(pushJobSetting.isTargetedRegionPushEnabled);
        assertTrue(pushJobSetting.postValidationConsumption);
        assertFalse(pushJobSetting.isSystemSchemaReaderEnabled);
        assertEquals(DataWriterMRJob.class, pushJobSetting.dataWriterComputeJobClass);
        assertNull(pushJobSetting.mapReducePartitionerClass);
    }
}

### 47.Field/Package Information Modification
link: https://github.com/apache/kafka/commit/bf88013a2812cab65bc70667e451e0a15d26b73c
p_path: group-coordinator/src/main/java/org/apache/kafka/coordinator/group/CoordinatorRecordSerde.java#deserialize
t_path: group-coordinator/src/test/java/org/apache/kafka/coordinator/group/CoordinatorRecordSerdeTest.java#testDeserialize

```java:test_src

@Test
public void testDeserialize() {
    RecordSerde serde = new RecordSerde();
    ApiMessageAndVersion key = new ApiMessageAndVersion(new ConsumerGroupMetadataKey().setGroupId("foo"), (short) 3);
    ByteBuffer keyBuffer = MessageUtil.toVersionPrefixedByteBuffer(key.version(), key.message());
    ApiMessageAndVersion value = new ApiMessageAndVersion(new ConsumerGroupMetadataValue().setEpoch(10), (short) 0);
    ByteBuffer valueBuffer = MessageUtil.toVersionPrefixedByteBuffer(value.version(), value.message());
    Record record = serde.deserialize(keyBuffer, valueBuffer);
    assertEquals(key, record.key());
    assertEquals(value, record.value());
}

```java:test_tgt

@Test
public void testDeserialize() {
    CoordinatorRecordSerde serde = new CoordinatorRecordSerde();
    ApiMessageAndVersion key = new ApiMessageAndVersion(new ConsumerGroupMetadataKey().setGroupId("foo"), (short) 3);
    ByteBuffer keyBuffer = MessageUtil.toVersionPrefixedByteBuffer(key.version(), key.message());
    ApiMessageAndVersion value = new ApiMessageAndVersion(new ConsumerGroupMetadataValue().setEpoch(10), (short) 0);
    ByteBuffer valueBuffer = MessageUtil.toVersionPrefixedByteBuffer(value.version(), value.message());
    CoordinatorRecord record = serde.deserialize(keyBuffer, valueBuffer);
    assertEquals(key, record.key());
    assertEquals(value, record.value());
}

```java:llm_gen

@Test
public void testDeserialize() {
    RecordSerde serde = new RecordSerde();
    ApiMessageAndVersion key = new ApiMessageAndVersion(new ConsumerGroupMetadataKey().setGroupId("foo"), (short) 3);
    ByteBuffer keyBuffer = MessageUtil.toVersionPrefixedByteBuffer(key.version(), key.message());
    ApiMessageAndVersion value = new ApiMessageAndVersion(new ConsumerGroupMetadataValue().setEpoch(10), (short) 0);
    ByteBuffer valueBuffer = MessageUtil.toVersionPrefixedByteBuffer(value.version(), value.message());
    CoordinatorRecord record = serde.deserialize(keyBuffer, valueBuffer);
    assertEquals(key, record.key());
    assertEquals(value, record.value());
}

### 48.Correct
link: https://github.com/apache/kafka/commit/bf88013a2812cab65bc70667e451e0a15d26b73c
p_path: group-coordinator/src/main/java/org/apache/kafka/coordinator/group/CoordinatorRecordHelpers.java#newGroupSubscriptionMetadataTombstoneRecord
t_path: group-coordinator/src/test/java/org/apache/kafka/coordinator/group/CoordinatorRecordHelpersTest.java#testNewGroupSubscriptionMetadataTombstoneRecord

```java:test_src

@Test
public void testNewGroupSubscriptionMetadataTombstoneRecord() {
    Record expectedRecord = new Record(new ApiMessageAndVersion(new ConsumerGroupPartitionMetadataKey().setGroupId("group-id"), (short) 4), null);
    assertEquals(expectedRecord, newGroupSubscriptionMetadataTombstoneRecord("group-id"));
}

```java:test_tgt

@Test
public void testNewGroupSubscriptionMetadataTombstoneRecord() {
    CoordinatorRecord expectedRecord = new CoordinatorRecord(new ApiMessageAndVersion(new ConsumerGroupPartitionMetadataKey().setGroupId("group-id"), (short) 4), null);
    assertEquals(expectedRecord, newGroupSubscriptionMetadataTombstoneRecord("group-id"));
}

```java:llm_gen

@Test
public void testNewGroupSubscriptionMetadataTombstoneRecord() {
    CoordinatorRecord expectedRecord = new CoordinatorRecord(new ApiMessageAndVersion(new ConsumerGroupPartitionMetadataKey().setGroupId("group-id"), (short) 4), null);
    assertEquals(expectedRecord, newGroupSubscriptionMetadataTombstoneRecord("group-id"));
}

### 49.Test Preparation Error
link: https://github.com/apache/flink-kubernetes-operator/commit/3ead906f33a4b3790fa5c12f2018e09db9443a09
p_path: flink-autoscaler/src/main/java/org/apache/flink/autoscaler/JobAutoScalerImpl.java#applyConfigOverrides
t_path: flink-autoscaler/src/test/java/org/apache/flink/autoscaler/JobAutoScalerImplTest.java#testApplyConfigOverrides

```java:test_src

@Test
void testApplyConfigOverrides() throws Exception {
    context.getConfiguration().set(AutoScalerOptions.MEMORY_TUNING_ENABLED, true);
    var autoscaler = new JobAutoScalerImpl<>(null, null, null, eventCollector, scalingRealizer, stateStore);
    assertThat(stateStore.getConfigOverrides(context).toMap()).isEmpty();
    var config = new Configuration();
    config.set(TaskManagerOptions.TASK_HEAP_MEMORY, new MemorySize(42));
    stateStore.storeConfigOverrides(context, config);
    stateStore.flush(context);
    autoscaler.applyConfigOverrides(context);
    assertThat(getEvent().getConfigOverrides().toMap()).containsExactly(entry(TaskManagerOptions.TASK_HEAP_MEMORY.key(), "42 bytes"));
    assertThat(stateStore.getConfigOverrides(context)).isEqualTo(config);
    context.getConfiguration().setString(AUTOSCALER_ENABLED.key(), "false");
    autoscaler.scale(context);
    autoscaler.applyConfigOverrides(context);
    assertThat(getEvent().getConfigOverrides().toMap()).isEmpty();
}

```java:test_tgt

@Test
void testApplyConfigOverrides() throws Exception {
    context.getConfiguration().set(AutoScalerOptions.MEMORY_TUNING_ENABLED, true);
    var autoscaler = new JobAutoScalerImpl<>(null, null, null, eventCollector, scalingRealizer, stateStore);
    assertThat(stateStore.getConfigChanges(context).getOverrides()).isEmpty();
    ConfigChanges config = new ConfigChanges();
    config.addOverride(TaskManagerOptions.MANAGED_MEMORY_FRACTION, 0.42f);
    config.addRemoval(TaskManagerOptions.TASK_HEAP_MEMORY);
    stateStore.storeConfigChanges(context, config);
    stateStore.flush(context);
    autoscaler.applyConfigOverrides(context);
    var event = getEvent();
    assertThat(event.getConfigChanges().getOverrides()).containsExactly(entry(TaskManagerOptions.MANAGED_MEMORY_FRACTION.key(), "0.42"));
    assertThat(event.getConfigChanges().getRemovals()).containsExactly(TaskManagerOptions.TASK_HEAP_MEMORY.key());
    assertThat(stateStore.getConfigChanges(context)).isEqualTo(config);
    context.getConfiguration().setString(AUTOSCALER_ENABLED.key(), "false");
    autoscaler.scale(context);
    autoscaler.applyConfigOverrides(context);
    assertThat(getEvent().getConfigChanges().getOverrides()).isEmpty();
}

```java:llm_gen

@Test
void testApplyConfigOverrides() throws Exception {
    context.getConfiguration().set(AutoScalerOptions.MEMORY_TUNING_ENABLED, true);
    var autoscaler = new JobAutoScalerImpl<>(null, null, null, eventCollector, scalingRealizer, stateStore);
    assertThat(stateStore.getConfigChanges(context).toMap()).isEmpty();
    var config = new Configuration();
    config.set(TaskManagerOptions.TASK_HEAP_MEMORY, new MemorySize(42));
    stateStore.storeConfigChanges(context, config);
    stateStore.flush(context);
    autoscaler.applyConfigOverrides(context);
    assertThat(getEvent().getConfigOverrides().toMap()).containsExactly(entry(TaskManagerOptions.TASK_HEAP_MEMORY.key(), "42 bytes"));
    assertThat(stateStore.getConfigChanges(context)).isEqualTo(config);
    context.getConfiguration().setString(AUTOSCALER_ENABLED.key(), "false");
    autoscaler.scale(context);
    autoscaler.applyConfigOverrides(context);
    assertThat(getEvent().getConfigOverrides().toMap()).isEmpty();
}

### 50.Missing Asserts
link: https://github.com/dremio/dremio-oss/commit/12d7a954966ee5782921a4fbe32cc4568cbf631b
p_path: dac/backend/src/main/java/com/dremio/dac/explore/Transformer.java#transformWithExtract
t_path: dac/backend/src/test/java/com/dremio/dac/explore/TestTransformer.java#testTransformWithExtract

```java:test_src

@Test
public void testTransformWithExtract() throws Exception {
    setSpace();
    DatasetPath myDatasetPath = new DatasetPath("spacefoo.folderbar.folderbaz.datasetbuzz");
    createDatasetFromParentAndSave(myDatasetPath, "cp.\"tpch/supplier.parquet\"");
    DatasetUI dataset = getDataset(myDatasetPath);
    Transformer testTransformer = new Transformer(l(SabotContext.class), l(JobsService.class), newNamespaceService(), newDatasetVersionMutator(), null, l(SecurityContext.class), l(CatalogService.class));
    VirtualDatasetUI vdsui = DatasetsUtil.getHeadVersion(myDatasetPath, newNamespaceService(), newDatasetVersionMutator());
    List<ViewFieldType> sqlFields = vdsui.getSqlFieldsList();
    boolean isContainOriginal = false;
    boolean isContainConverted = false;
    for (ViewFieldType sqlType : sqlFields) {
        if (sqlType.getName().equalsIgnoreCase("s_address")) {
            isContainOriginal = true;
            break;
        }
    }
    assertTrue(isContainOriginal);
    isContainOriginal = false;
    VirtualDatasetUI vdsuiTransformed = testTransformer.transformWithExtract(dataset.getDatasetVersion(), myDatasetPath, vdsui, new TransformRename("s_address", "s_addr"));
    List<ViewFieldType> sqlFieldsTransformed = vdsuiTransformed.getSqlFieldsList();
    for (ViewFieldType sqlType : sqlFieldsTransformed) {
        if (sqlType.getName().equalsIgnoreCase("s_addr")) {
            isContainConverted = true;
        }
        if (sqlType.getName().equalsIgnoreCase("s_address")) {
            isContainOriginal = true;
        }
    }
    assertTrue(isContainConverted);
    assertTrue(!isContainOriginal);
}

```java:test_tgt

@Test
public void testTransformWithExtract() throws Exception {
    setSpace();
    DatasetPath myDatasetPath = new DatasetPath("spacefoo.folderbar.folderbaz.datasetbuzz");
    createDatasetFromParentAndSave(myDatasetPath, "cp.\"tpch/supplier.parquet\"");
    Transformer testTransformer = new Transformer(l(SabotContext.class), l(JobsService.class), newNamespaceService(), newDatasetVersionMutator(), null, l(SecurityContext.class), l(CatalogService.class));
    VirtualDatasetUI vdsui = DatasetsUtil.getHeadVersion(myDatasetPath, newNamespaceService(), newDatasetVersionMutator());
    String originalDatasetVersion = vdsui.getVersion().getVersion();
    List<ViewFieldType> sqlFields = vdsui.getSqlFieldsList();
    boolean isContainOriginal = false;
    boolean isContainConverted = false;
    for (ViewFieldType sqlType : sqlFields) {
        if (sqlType.getName().equalsIgnoreCase("s_address")) {
            isContainOriginal = true;
            break;
        }
    }
    assertTrue(isContainOriginal);
    isContainOriginal = false;
    VirtualDatasetUI vdsuiTransformed = testTransformer.transformWithExtract(myDatasetPath, vdsui, new TransformRename("s_address", "s_addr"));
    List<ViewFieldType> sqlFieldsTransformed = vdsuiTransformed.getSqlFieldsList();
    for (ViewFieldType sqlType : sqlFieldsTransformed) {
        if (sqlType.getName().equalsIgnoreCase("s_addr")) {
            isContainConverted = true;
        }
        if (sqlType.getName().equalsIgnoreCase("s_address")) {
            isContainOriginal = true;
        }
    }
    assertTrue(isContainConverted);
    assertTrue(!isContainOriginal);
    assertNotEquals(originalDatasetVersion, vdsuiTransformed.getVersion().getVersion());
}

```java:llm_gen

@Test
public void testTransformWithExtract() throws Exception {
    setSpace();
    DatasetPath myDatasetPath = new DatasetPath("spacefoo.folderbar.folderbaz.datasetbuzz");
    createDatasetFromParentAndSave(myDatasetPath, "cp.\"tpch/supplier.parquet\"");
    DatasetUI dataset = getDataset(myDatasetPath);
    Transformer testTransformer = new Transformer(l(SabotContext.class), l(JobsService.class), newNamespaceService(), newDatasetVersionMutator(), null, l(SecurityContext.class), l(CatalogService.class));
    VirtualDatasetUI vdsui = DatasetsUtil.getHeadVersion(myDatasetPath, newNamespaceService(), newDatasetVersionMutator());
    List<ViewFieldType> sqlFields = vdsui.getSqlFieldsList();
    boolean isContainOriginal = false;
    boolean isContainConverted = false;
    for (ViewFieldType sqlType : sqlFields) {
        if (sqlType.getName().equalsIgnoreCase("s_address")) {
            isContainOriginal = true;
            break;
        }
    }
    assertTrue(isContainOriginal);
    isContainOriginal = false;
    VirtualDatasetUI vdsuiTransformed = testTransformer.transformWithExtract(myDatasetPath, vdsui, new TransformRename("s_address", "s_addr"));
    List<ViewFieldType> sqlFieldsTransformed = vdsuiTransformed.getSqlFieldsList();
    for (ViewFieldType sqlType : sqlFieldsTransformed) {
        if (sqlType.getName().equalsIgnoreCase("s_addr")) {
            isContainConverted = true;
        }
        if (sqlType.getName().equalsIgnoreCase("s_address")) {
            isContainOriginal = true;
        }
    }
    assertTrue(isContainConverted);
    assertTrue(!isContainOriginal);
}

### 51.Pure Syntax Error
link: https://github.com/apache/commons-collections/commit/de059262b96b5c0a79cd2aa578e27a752f8e9ff1
p_path: src/main/java/org/apache/commons/collections4/bloomfilter/LayerManager.java#copy
t_path: src/test/java/org/apache/commons/collections4/bloomfilter/LayerManagerTest.java#testCopy

```java:test_src

@Test
public void testCopy() {
    LayerManager<BloomFilter> underTest = LayerManager.builder().setSupplier(() -> new SimpleBloomFilter(shape)).build();
    underTest.getTarget().merge(TestingHashers.randomHasher());
    underTest.next();
    underTest.getTarget().merge(TestingHashers.randomHasher());
    underTest.next();
    underTest.getTarget().merge(TestingHashers.randomHasher());
    assertEquals(3, underTest.getDepth());
    LayerManager<BloomFilter> copy = underTest.copy();
    assertNotSame(underTest, copy);
    assertNotEquals(underTest, copy);
    assertEquals(underTest.getDepth(), copy.getDepth());
    assertTrue(underTest.forEachBloomFilterPair(copy, (x, y) -> Arrays.equals(x.asBitMapArray(), y.asBitMapArray())));
}

```java:test_tgt

@Test
public void testCopy() {
    final LayerManager<BloomFilter> underTest = LayerManager.builder().setSupplier(() -> new SimpleBloomFilter(shape)).build();
    underTest.getTarget().merge(TestingHashers.randomHasher());
    underTest.next();
    underTest.getTarget().merge(TestingHashers.randomHasher());
    underTest.next();
    underTest.getTarget().merge(TestingHashers.randomHasher());
    assertEquals(3, underTest.getDepth());
    final LayerManager<BloomFilter> copy = underTest.copy();
    assertNotSame(underTest, copy);
    assertNotEquals(underTest, copy);
    assertEquals(underTest.getDepth(), copy.getDepth());
    assertTrue(underTest.forEachBloomFilterPair(copy, (x, y) -> Arrays.equals(x.asBitMapArray(), y.asBitMapArray())));
}

```java:llm_gen

@Test
public void testCopy() {
    final LayerManager<BloomFilter> underTest = LayerManager.builder().setSupplier(() -> new SimpleBloomFilter(shape)).build();
    underTest.getTarget().merge(TestingHashers.randomHasher());
    underTest.next();
    underTest.getTarget().merge(TestingHashers.randomHasher());
    underTest.next();
    underTest.getTarget().merge(TestingHashers.randomHasher());
    assertEquals(3, underTest.getDepth());
    final LayerManager<BloomFilter> copy = underTest.copy();
    assertNotSame(underTest, copy);
    assertNotEquals(underTest, copy);
    assertEquals(underTest.getDepth(), copy.getDepth());
    assertTrue(underTest.forEachBloomFilterPair(copy, (x, y) -> Arrays.equals(x.asBitMapArray(), y.asBitMapArray()));
}

### 52.Assert Error
link: https://github.com/HTTP-RPC/Kilo/commit/5d4daed54ec30876a3a7a6571e165afd57ba8f64
p_path: kilo-client/src/main/java/org/httprpc/kilo/sql/QueryBuilder.java#updateParent
t_path: kilo-client/src/test/java/org/httprpc/kilo/sql/QueryBuilderTest.java#testUpdateParent

```java:test_src

@Test
public void testUpdateParent() {
    var queryBuilder = QueryBuilder.updateParent(I.class, H.class, "h").filterByPrimaryKey("i");
    assertEquals("update I set h = ?\nwhere I.i = ?\n", queryBuilder.toString());
    assertEquals(listOf("h", "i"), queryBuilder.getParameters());
}

```java:test_tgt

@Test
public void testUpdateParent() {
    var queryBuilder = QueryBuilder.updateParent(I.class, H.class, "h").filterByPrimaryKey("i");
    assertEquals("update I set h = ? where I.i = ?", queryBuilder.toString());
    assertEquals(listOf("h", "i"), queryBuilder.getParameters());
}

```java:llm_gen

@Test
public void testUpdateParent() {
    var queryBuilder = QueryBuilder.updateParent(I.class, H.class, "h").filterByPrimaryKey("i");
    assertEquals("update I set h = ? where I.i = ?\n", queryBuilder.toString());
    assertEquals(listOf("h", "i"), queryBuilder.getParameters());
}

### 53.Missing Asserts
link: https://github.com/langchain4j/langchain4j/commit/423a4c65eaa46fe32e6c0fa68bbed3449931baa3
p_path: langchain4j-core/src/main/java/dev/langchain4j/internal/ValidationUtils.java#ensureNotNull
t_path: langchain4j-core/src/test/java/dev/langchain4j/internal/ValidationUtilsTest.java#test_ensureNotNull

```java:test_src

@Test
public void test_ensureNotNull() {
    {
        Object obj = new Object();
        assertThat(ValidationUtils.ensureNotNull(obj, "test")).isSameAs(obj);
    }
    assertThatExceptionOfType(IllegalArgumentException.class).isThrownBy(() -> ValidationUtils.ensureNotNull(null, "test")).withMessageContaining("test cannot be null");
}

```java:test_tgt

@Test
public void test_ensureNotNull() {
    {
        Object obj = new Object();
        assertThat(ValidationUtils.ensureNotNull(obj, "test")).isSameAs(obj);
    }
    assertThatExceptionOfType(IllegalArgumentException.class).isThrownBy(() -> ValidationUtils.ensureNotNull(null, "test")).withMessage("test cannot be null");
    assertThatExceptionOfType(IllegalArgumentException.class).isThrownBy(() -> ValidationUtils.ensureNotNull(null, "test %d", 7)).withMessage("test 7");
}

```java:llm_gen

@Test
public void test_ensureNotNull() {
    {
        Object obj = new Object();
        assertThat(ValidationUtils.ensureNotNull(obj, "test %s", "object")).isSameAs(obj);
    }
    assertThatExceptionOfType(IllegalArgumentException.class).isThrownBy(() -> ValidationUtils.ensureNotNull(null, "test %s", "object")).withMessageContaining("test object");
}

### 54.Correct
link: https://github.com/ctripcorp/x-pipe/commit/c419d8a8329a4343d1403852df52c611fbd385d6
p_path: redis/redis-console/src/main/java/com/ctrip/xpipe/redis/console/service/impl/KeeperContainerServiceImpl.java#updateKeeperContainerByInfoModel
t_path: redis/redis-console/src/test/java/com/ctrip/xpipe/redis/console/service/impl/KeeperContainerServiceImplTest.java#testUpdateKeeperContainerByInfoModel

```java:test_src

@Test
public void testUpdateKeeperContainerByInfoModel() {
    KeeperContainerInfoModel keeper = keeperContainerService.findKeeperContainerInfoModelById(30);
    Assert.assertEquals("fra", keeper.getDcName());
    Assert.assertEquals("127.0.1.2", keeper.getAddr().getHost());
    Assert.assertEquals(7033, keeper.getAddr().getPort());
    Assert.assertEquals(true, keeper.isActive());
    Assert.assertEquals(null, keeper.getOrgName());
    Assert.assertEquals("A", keeper.getAzName());
    keeper.setAzName("B");
    keeper.setOrgName("org-1");
    keeper.setActive(false);
    keeper.setDcName("jq");
    keeperContainerService.updateKeeperContainerByInfoModel(keeper);
    KeeperContainerInfoModel keeper1 = keeperContainerService.findKeeperContainerInfoModelById(30);
    Assert.assertEquals("fra", keeper1.getDcName());
    Assert.assertEquals("127.0.1.2", keeper1.getAddr().getHost());
    Assert.assertEquals(7033, keeper1.getAddr().getPort());
    Assert.assertEquals(false, keeper1.isActive());
    Assert.assertEquals("org-1", keeper1.getOrgName());
    Assert.assertEquals("B", keeper1.getAzName());
}

```java:test_tgt

@Test
public void testUpdateKeeperContainerByInfoModel() {
    KeeperContainerInfoModel keeper = keeperContainerService.findKeeperContainerInfoModelById(30);
    Assert.assertEquals("fra", keeper.getDcName());
    Assert.assertEquals("127.0.1.2", keeper.getAddr().getHost());
    Assert.assertEquals(7033, keeper.getAddr().getPort());
    Assert.assertEquals(true, keeper.isActive());
    Assert.assertEquals(null, keeper.getOrgName());
    Assert.assertEquals("A", keeper.getAzName());
    keeper.setAzName("B");
    keeper.setOrgName("org-1");
    keeper.setActive(false);
    keeper.setDcName("jq");
    keeper.setDiskType("DEFAULT");
    keeperContainerService.updateKeeperContainerByInfoModel(keeper);
    KeeperContainerInfoModel keeper1 = keeperContainerService.findKeeperContainerInfoModelById(30);
    Assert.assertEquals("fra", keeper1.getDcName());
    Assert.assertEquals("127.0.1.2", keeper1.getAddr().getHost());
    Assert.assertEquals(7033, keeper1.getAddr().getPort());
    Assert.assertEquals(false, keeper1.isActive());
    Assert.assertEquals("org-1", keeper1.getOrgName());
    Assert.assertEquals("B", keeper1.getAzName());
}

```java:llm_gen

@Test
public void testUpdateKeeperContainerByInfoModel() {
    KeeperContainerInfoModel keeper = keeperContainerService.findKeeperContainerInfoModelById(30);
    Assert.assertEquals("fra", keeper.getDcName());
    Assert.assertEquals("127.0.1.2", keeper.getAddr().getHost());
    Assert.assertEquals(7033, keeper.getAddr().getPort());
    Assert.assertEquals(true, keeper.isActive());
    Assert.assertEquals(null, keeper.getOrgName());
    Assert.assertEquals("A", keeper.getAzName());
    Assert.assertEquals("", keeper.getDiskType());
    keeper.setAzName("B");
    keeper.setOrgName("org-1");
    keeper.setActive(false);
    keeper.setDcName("jq");
    keeper.setDiskType("SSD");
    keeperContainerService.updateKeeperContainerByInfoModel(keeper);
    KeeperContainerInfoModel keeper1 = keeperContainerService.findKeeperContainerInfoModelById(30);
    Assert.assertEquals("fra", keeper1.getDcName());
    Assert.assertEquals("127.0.1.2", keeper1.getAddr().getHost());
    Assert.assertEquals(7033, keeper1.getAddr().getPort());
    Assert.assertEquals(false, keeper1.isActive());
    Assert.assertEquals("org-1", keeper1.getOrgName());
    Assert.assertEquals("B", keeper1.getAzName());
    Assert.assertEquals("SSD", keeper1.getDiskType());
}

### 55.Correct
link: https://github.com/google/tink/commit/b0c03e2304a0a0cc20f6ba8de4a6b85f8d1683be
p_path: java_src/src/main/java/com/google/crypto/tink/aead/AeadKeyTemplates.java#createKmsEnvelopeAeadKeyTemplate
t_path: java_src/src/test/java/com/google/crypto/tink/aead/AeadKeyTemplatesTest.java#testCreateKmsEnvelopeAeadKeyTemplate

```java:test_src

@Test
public void testCreateKmsEnvelopeAeadKeyTemplate() throws Exception {
    String kekUri = "some example KEK URI";
    KeyTemplate dekTemplate = AeadKeyTemplates.AES256_GCM;
    KeyTemplate template = AeadKeyTemplates.createKmsEnvelopeAeadKeyTemplate(kekUri, dekTemplate);
    assertEquals(new KmsEnvelopeAeadKeyManager().getKeyType(), template.getTypeUrl());
    assertEquals(OutputPrefixType.RAW, template.getOutputPrefixType());
    KmsEnvelopeAeadKeyFormat format = KmsEnvelopeAeadKeyFormat.parseFrom(template.getValue(), ExtensionRegistryLite.getEmptyRegistry());
    assertEquals(kekUri, format.getKekUri());
    assertEquals(dekTemplate.toString(), format.getDekTemplate().toString());
}

```java:test_tgt

@Test
public void testCreateKmsEnvelopeAeadKeyTemplate() throws Exception {
    String kekUri = "some example KEK URI";
    KeyTemplate dekTemplate = AeadKeyTemplates.AES256_GCM;
    KeyTemplate template = AeadKeyTemplates.createKmsEnvelopeAeadKeyTemplate(kekUri, dekTemplate);
    assertEquals(KmsEnvelopeAeadKeyManager.getKeyType(), template.getTypeUrl());
    assertEquals(OutputPrefixType.RAW, template.getOutputPrefixType());
    KmsEnvelopeAeadKeyFormat format = KmsEnvelopeAeadKeyFormat.parseFrom(template.getValue(), ExtensionRegistryLite.getEmptyRegistry());
    assertEquals(kekUri, format.getKekUri());
    assertEquals(dekTemplate.toString(), format.getDekTemplate().toString());
}

```java:llm_gen

@Test
public void testCreateKmsEnvelopeAeadKeyTemplate() throws Exception {
    String kekUri = "some example KEK URI";
    KeyTemplate dekTemplate = AeadKeyTemplates.AES256_GCM;
    KeyTemplate template = AeadKeyTemplates.createKmsEnvelopeAeadKeyTemplate(kekUri, dekTemplate);
    assertEquals(KmsEnvelopeAeadKeyManager.getKeyType(), template.getTypeUrl());
    assertEquals(OutputPrefixType.RAW, template.getOutputPrefixType());
    KmsEnvelopeAeadKeyFormat format = KmsEnvelopeAeadKeyFormat.parseFrom(template.getValue(), ExtensionRegistryLite.getEmptyRegistry());
    assertEquals(kekUri, format.getKekUri());
    assertEquals(dekTemplate.toString(), format.getDekTemplate().toString());
}

### 56.Field/Package Information Modification
link: https://github.com/apache/kafka/commit/bf88013a2812cab65bc70667e451e0a15d26b73c
p_path: group-coordinator/src/main/java/org/apache/kafka/coordinator/group/CoordinatorRecordSerde.java#serializeKey
t_path: group-coordinator/src/test/java/org/apache/kafka/coordinator/group/CoordinatorRecordSerdeTest.java#testSerializeKey

```java:test_src

@Test
public void testSerializeKey() {
    RecordSerde serializer = new RecordSerde();
    Record record = new Record(new ApiMessageAndVersion(new ConsumerGroupMetadataKey().setGroupId("group"), (short) 3), new ApiMessageAndVersion(new ConsumerGroupMetadataValue().setEpoch(10), (short) 0));
    assertArrayEquals(MessageUtil.toVersionPrefixedBytes(record.key().version(), record.key().message()), serializer.serializeKey(record));
}

```java:test_tgt

@Test
public void testSerializeKey() {
    CoordinatorRecordSerde serializer = new CoordinatorRecordSerde();
    CoordinatorRecord record = new CoordinatorRecord(new ApiMessageAndVersion(new ConsumerGroupMetadataKey().setGroupId("group"), (short) 3), new ApiMessageAndVersion(new ConsumerGroupMetadataValue().setEpoch(10), (short) 0));
    assertArrayEquals(MessageUtil.toVersionPrefixedBytes(record.key().version(), record.key().message()), serializer.serializeKey(record));
}

```java:llm_gen

@Test
public void testSerializeKey() {
    RecordSerde serializer = new RecordSerde();
    CoordinatorRecord record = new CoordinatorRecord(new ApiMessageAndVersion(new ConsumerGroupMetadataKey().setGroupId("group"), (short) 3), new ApiMessageAndVersion(new ConsumerGroupMetadataValue().setEpoch(10), (short) 0));
    assertArrayEquals(MessageUtil.toVersionPrefixedBytes(record.key().version(), record.key().message()), serializer.serializeKey(record));
}

### 57.Correct
link: https://github.com/alibaba/nacos/commit/5fcef225beca56954c7ce49c67a40aa0d62ce086
p_path: common/src/main/java/com/alibaba/nacos/common/utils/ConnLabelsUtils.java#parsePropertyValue2Map
t_path: common/src/test/java/com/alibaba/nacos/common/utils/ConnLabelsUtilsTest.java#testParsePropertyValue2Map

```java:test_src

@Test
public void testParsePropertyValue2Map() {
    Properties properties = new Properties();
    String property = "property";
    String rawValue = "k1 = v1, k2 = v2";
    properties.put(property, rawValue);
    String property1 = "property2";
    String rawValue1 = "k1, kk2";
    properties.put(property1, rawValue1);
    Map<String, String> m = ConnLabelsUtils.parsePropertyValue2Map(properties, property);
    assertEquals(2, m.size());
    assertEquals("v1", m.get("k1"));
    assertEquals("v2", m.get("k2"));
    Map<String, String> m1 = ConnLabelsUtils.parsePropertyValue2Map(properties, property1);
    assertEquals(2, m.size());
    assertEquals("k1", m1.get("k1"));
    assertEquals("kk2", m1.get("kk2"));
    m = ConnLabelsUtils.mergeMapByOrder(m, m1);
    assertEquals(3, m.size());
    assertEquals("v1", m.get("k1"));
    assertEquals("v2", m.get("k2"));
    assertEquals("kk2", m.get("kk2"));
    m = ConnLabelsUtils.addPrefixForEachKey(m, "test_prefix");
    assertEquals(3, m.size());
    m.forEach((k, v) -> {
        assertTrue(k.startsWith("test_prefix"));
    });
}

```java:test_tgt

@Test
public void testParsePropertyValue2Map() {
    Properties properties = new Properties();
    String property = "property";
    String rawValue = "k1 = v1, k2 = v2";
    properties.put(property, rawValue);
    String property1 = "property2";
    String rawValue1 = "k11=v11, kk2";
    properties.put(property1, rawValue1);
    Map<String, String> m = ConnLabelsUtils.parsePropertyValue2Map(properties, property);
    assertEquals(2, m.size());
    assertEquals("v1", m.get("k1"));
    assertEquals("v2", m.get("k2"));
    Map<String, String> m1 = ConnLabelsUtils.parsePropertyValue2Map(properties, property1);
    assertEquals(1, m1.size());
    assertEquals("v11", m1.get("k11"));
    assertEquals(null, m1.get("kk2"));
    m = ConnLabelsUtils.mergeMapByOrder(m, m1);
    assertEquals(3, m.size());
    assertEquals("v1", m.get("k1"));
    assertEquals("v2", m.get("k2"));
    assertEquals("v11", m.get("k11"));
    m = ConnLabelsUtils.addPrefixForEachKey(m, "test_prefix");
    assertEquals(3, m.size());
    m.forEach((k, v) -> {
        assertTrue(k.startsWith("test_prefix"));
    });
}

```java:llm_gen

@Test
public void testParsePropertyValue2Map() {
    Properties properties = new Properties();
    String property = "property";
    String rawValue = "k1 = v1, k2 = v2";
    properties.put(property, rawValue);
    String property1 = "property2";
    String rawValue1 = "k1, kk2";
    properties.put(property1, rawValue1);
    Map<String, String> m = ConnLabelsUtils.parsePropertyValue2Map(properties, property);
    assertEquals(2, m.size());
    assertEquals("v1", m.get("k1"));
    assertEquals("v2", m.get("k2"));
    Map<String, String> m1 = ConnLabelsUtils.parsePropertyValue2Map(properties, property1);
    assertEquals(2, m1.size());
    assertEquals("k1", m1.get("k1"));
    assertEquals("kk2", m1.get("kk2"));
    m = ConnLabelsUtils.mergeMapByOrder(m, m1);
    assertEquals(3, m.size());
    assertEquals("v1", m.get("k1"));
    assertEquals("v2", m.get("k2"));
    assertEquals("kk2", m.get("kk2"));
    m = ConnLabelsUtils.addPrefixForEachKey(m, "test_prefix");
    assertEquals(3, m.size());
    m.forEach((k, v) -> {
        assertTrue(k.startsWith("test_prefix"));
    });

    // Test case for empty or null property value
    Map<String, String> emptyMap = ConnLabelsUtils.parsePropertyValue2Map(properties, "non_existent_property");
    assertEquals(0, emptyMap.size());
}

### 58.Correct
link: https://github.com/microcks/microcks/commit/2b4bc2f9faf64896463257d37c12dba89cfb4179
p_path: webapp/src/main/java/io/github/microcks/util/GitLabReferenceURLBuilder.java#getFileName
t_path: webapp/src/test/java/io/github/microcks/util/GitLabReferenceURLBuilderTest.java#testGetFileName

```java:test_src

@Test
public void testGetFileName() {
    GitLabReferenceURLBuilder builder = new GitLabReferenceURLBuilder();
    assertEquals("API_Pastry_1.0.0-openapi.yaml", builder.getFileName(BASE_URL, null));
    Map<String, List<String>> headers = Map.of("X-Gitlab-File-Name", List.of("FooBar.yaml"));
    assertEquals("FooBar.yaml", builder.getFileName(BASE_URL, headers));
}

```java:test_tgt

@Test
public void testGetFileName() {
    GitLabReferenceURLBuilder builder = new GitLabReferenceURLBuilder();
    assertEquals("API_Pastry_1.0.0-openapi.yaml", builder.getFileName(BASE_URL, null));
    Map<String, List<String>> headers = Map.of("X-Gitlab-File-Name", List.of("FooBar.yaml"));
    assertEquals("FooBar.yaml", builder.getFileName(BASE_URL, headers));
    headers = Map.of("x-gitlab-file-name", List.of("FooBar.yaml"));
    assertEquals("FooBar.yaml", builder.getFileName(BASE_URL, headers));
}

```java:llm_gen

@Test
public void testGetFileName() {
    GitLabReferenceURLBuilder builder = new GitLabReferenceURLBuilder();
    assertEquals("API_Pastry_1.0.0-openapi.yaml", builder.getFileName(BASE_URL, null));
    Map<String, List<String>> headers = Map.of("X-Gitlab-File-Name", List.of("FooBar.yaml"));
    assertEquals("FooBar.yaml", builder.getFileName(BASE_URL, headers));
    Map<String, List<String>> caseInsensitiveHeaders = Map.of("x-gitlab-file-name", List.of("BarFoo.yaml"));
    assertEquals("BarFoo.yaml", builder.getFileName(BASE_URL, caseInsensitiveHeaders));
}

### 59.Additional Asserts
link: https://github.com/BentoBoxWorld/BentoBox/commit/52a280dc0b56a35ab7a46a773ff0288fdcd22ee5
p_path: src/main/java/world/bentobox/bentobox/managers/island/IslandCache.java#setOwner
t_path: src/test/java/world/bentobox/bentobox/managers/island/IslandCacheTest.java#testSetOwner

```java:test_src

@Test
public void testSetOwner() {
    ic.addIsland(island);
    UUID newOwnerUUID = UUID.randomUUID();
    ic.setOwner(island, newOwnerUUID);
    Mockito.verify(island).setOwner(newOwnerUUID);
    assertEquals(island, ic.get(world, newOwnerUUID));
    assertEquals(island, ic.get(island.getCenter()));
}

```java:test_tgt

@Test
public void testSetOwner() {
    ic.addIsland(island);
    UUID newOwnerUUID = UUID.randomUUID();
    ic.setOwner(island, newOwnerUUID);
    Mockito.verify(island).setOwner(newOwnerUUID);
    assertEquals(island, ic.get(world, newOwnerUUID));
}

```java:llm_gen

@Test
public void testSetOwner() {
    ic.addIsland(island);
    UUID newOwnerUUID = UUID.randomUUID();
    ic.setOwner(island, newOwnerUUID);
    Mockito.verify(island).setOwner(newOwnerUUID);
    Mockito.verify(island).setRank(newOwnerUUID, RanksManager.OWNER_RANK);
    assertEquals(island, ic.get(world, newOwnerUUID));
    assertEquals(island, ic.get(island.getCenter()));
    assertEquals(island, ic.get(island.getUniqueId()));
}

### 60.Correct
link: https://github.com/dhis2/dhis2-core/commit/3d8d7664022149fe0fe983d0da0ca95c51658ace
p_path: dhis-2/dhis-services/dhis-service-analytics/src/main/java/org/hisp/dhis/db/sql/PostgreSqlBuilder.java#singleQuote
t_path: dhis-2/dhis-services/dhis-service-analytics/src/test/java/org/hisp/dhis/db/sql/PostgreSqlBuilderTest.java#testSingleQuote

```java:test_src

@Test
void testSingleQuote() {
    assertEquals("'jkhYg65ThbF'", sqlBuilder.singleQuote("jkhYg65ThbF"));
    assertEquals("'Age ''<5'' years'", sqlBuilder.singleQuote("Age '<5' years"));
    assertEquals("'Status \"not checked\" found'", sqlBuilder.singleQuote("Status \"not checked\" found"));
}

```java:test_tgt

@Test
void testSingleQuote() {
    assertEquals("'jkhYg65ThbF'", sqlBuilder.singleQuote("jkhYg65ThbF"));
    assertEquals("'Age ''<5'' years'", sqlBuilder.singleQuote("Age '<5' years"));
    assertEquals("'Status \"not checked\"'", sqlBuilder.singleQuote("Status \"not checked\""));
}

```java:llm_gen

@Test
void testSingleQuote() {
    assertEquals("'jkhYg65ThbF'", sqlBuilder.singleQuote("jkhYg65ThbF"));
    assertEquals("'Age ''<5'' years'", sqlBuilder.singleQuote("Age '<5' years"));
    assertEquals("'Status \"not checked\" found'", sqlBuilder.singleQuote("Status \"not checked\" found"));
}

### 61.Correct
link: https://github.com/microcks/microcks/commit/bc25dc3af803655c2eb4c6715672a254be522d05
p_path: webapp/src/main/java/io/github/microcks/util/DispatchCriteriaHelper.java#buildFromParamsMap
t_path: webapp/src/test/java/io/github/microcks/util/DispatchCriteriaHelperTest.java#testBuildFromParamsMap

```java:test_src

@Test
public void testBuildFromParamsMap() {
    Map<String, String> paramsMap = new HashMap<>();
    paramsMap.put("page", "1");
    paramsMap.put("limit", "20");
    paramsMap.put("limitation", "20");
    paramsMap.put("status", "available");
    String dispatchCriteria = DispatchCriteriaHelper.buildFromParamsMap("page", paramsMap);
    assertEquals("?page=1", dispatchCriteria);
    dispatchCriteria = DispatchCriteriaHelper.buildFromParamsMap("page && limit", paramsMap);
    assertEquals("?limit=20?page=1", dispatchCriteria);
    dispatchCriteria = DispatchCriteriaHelper.buildFromParamsMap("page && limitation", paramsMap);
    assertEquals("?limitation=20?page=1", dispatchCriteria);
}

```java:test_tgt

@Test
public void testBuildFromParamsMap() {
    Multimap<String, String> paramsMap = ArrayListMultimap.create();
    paramsMap.put("page", "1");
    paramsMap.put("limit", "20");
    paramsMap.put("limitation", "20");
    paramsMap.put("status", "available");
    String dispatchCriteria = DispatchCriteriaHelper.buildFromParamsMap("page", paramsMap);
    assertEquals("?page=1", dispatchCriteria);
    dispatchCriteria = DispatchCriteriaHelper.buildFromParamsMap("page && limit", paramsMap);
    assertEquals("?limit=20?page=1", dispatchCriteria);
    dispatchCriteria = DispatchCriteriaHelper.buildFromParamsMap("page && limitation", paramsMap);
    assertEquals("?limitation=20?page=1", dispatchCriteria);
}

```java:llm_gen

@Test
public void testBuildFromParamsMap() {
    Multimap<String, String> paramsMap = ArrayListMultimap.create();
    paramsMap.put("page", "1");
    paramsMap.put("limit", "20");
    paramsMap.put("limitation", "20");
    paramsMap.put("status", "available");
    String dispatchCriteria = DispatchCriteriaHelper.buildFromParamsMap("page", paramsMap);
    assertEquals("?page=1", dispatchCriteria);
    dispatchCriteria = DispatchCriteriaHelper.buildFromParamsMap("page && limit", paramsMap);
    assertEquals("?limit=20?page=1", dispatchCriteria);
    dispatchCriteria = DispatchCriteriaHelper.buildFromParamsMap("page && limitation", paramsMap);
    assertEquals("?limitation=20?page=1", dispatchCriteria);
}

### 62.Correct
link: https://github.com/thingsboard/thingsboard/commit/b33d1f9c6911d338f6d11b2b54773c36b8f6a808
p_path: common/dao-api/src/main/java/org/thingsboard/server/dao/widget/WidgetsBundleService.java#findSystemWidgetsBundlesByPageLink
t_path: dao/src/test/java/org/thingsboard/server/dao/service/WidgetsBundleServiceTest.java#testFindSystemWidgetsBundlesByPageLink

```java:test_src

@Test
public void testFindSystemWidgetsBundlesByPageLink() {
    TenantId tenantId = TenantId.fromUUID(ModelConstants.NULL_UUID);
    List<WidgetsBundle> systemWidgetsBundles = widgetsBundleService.findSystemWidgetsBundles(tenantId);
    List<WidgetsBundle> createdWidgetsBundles = new ArrayList<>();
    for (int i = 0; i < 235; i++) {
        WidgetsBundle widgetsBundle = new WidgetsBundle();
        widgetsBundle.setTenantId(tenantId);
        widgetsBundle.setTitle("Widgets bundle " + i);
        createdWidgetsBundles.add(widgetsBundleService.saveWidgetsBundle(widgetsBundle));
    }
    List<WidgetsBundle> widgetsBundles = new ArrayList<>(createdWidgetsBundles);
    widgetsBundles.addAll(systemWidgetsBundles);
    List<WidgetsBundle> loadedWidgetsBundles = new ArrayList<>();
    PageLink pageLink = new PageLink(19);
    PageData<WidgetsBundle> pageData = null;
    do {
        pageData = widgetsBundleService.findSystemWidgetsBundlesByPageLink(tenantId, pageLink);
        loadedWidgetsBundles.addAll(pageData.getData());
        if (pageData.hasNext()) {
            pageLink = pageLink.nextPageLink();
        }
    } while (pageData.hasNext());
    Collections.sort(widgetsBundles, idComparator);
    Collections.sort(loadedWidgetsBundles, idComparator);
    Assert.assertEquals(widgetsBundles, loadedWidgetsBundles);
    for (WidgetsBundle widgetsBundle : createdWidgetsBundles) {
        widgetsBundleService.deleteWidgetsBundle(tenantId, widgetsBundle.getId());
    }
    loadedWidgetsBundles = widgetsBundleService.findSystemWidgetsBundles(tenantId);
    Collections.sort(systemWidgetsBundles, idComparator);
    Collections.sort(loadedWidgetsBundles, idComparator);
    Assert.assertEquals(systemWidgetsBundles, loadedWidgetsBundles);
}

```java:test_tgt

@Test
public void testFindSystemWidgetsBundlesByPageLink() {
    TenantId tenantId = TenantId.fromUUID(ModelConstants.NULL_UUID);
    List<WidgetsBundle> systemWidgetsBundles = widgetsBundleService.findSystemWidgetsBundles(tenantId);
    List<WidgetsBundle> createdWidgetsBundles = new ArrayList<>();
    for (int i = 0; i < 235; i++) {
        WidgetsBundle widgetsBundle = new WidgetsBundle();
        widgetsBundle.setTenantId(tenantId);
        widgetsBundle.setTitle("Widgets bundle " + i);
        createdWidgetsBundles.add(widgetsBundleService.saveWidgetsBundle(widgetsBundle));
    }
    List<WidgetsBundle> widgetsBundles = new ArrayList<>(createdWidgetsBundles);
    widgetsBundles.addAll(systemWidgetsBundles);
    List<WidgetsBundle> loadedWidgetsBundles = new ArrayList<>();
    PageLink pageLink = new PageLink(19);
    PageData<WidgetsBundle> pageData = null;
    do {
        pageData = widgetsBundleService.findSystemWidgetsBundlesByPageLink(tenantId, false, pageLink);
        loadedWidgetsBundles.addAll(pageData.getData());
        if (pageData.hasNext()) {
            pageLink = pageLink.nextPageLink();
        }
    } while (pageData.hasNext());
    Collections.sort(widgetsBundles, idComparator);
    Collections.sort(loadedWidgetsBundles, idComparator);
    Assert.assertEquals(widgetsBundles, loadedWidgetsBundles);
    for (WidgetsBundle widgetsBundle : createdWidgetsBundles) {
        widgetsBundleService.deleteWidgetsBundle(tenantId, widgetsBundle.getId());
    }
    loadedWidgetsBundles = widgetsBundleService.findSystemWidgetsBundles(tenantId);
    Collections.sort(systemWidgetsBundles, idComparator);
    Collections.sort(loadedWidgetsBundles, idComparator);
    Assert.assertEquals(systemWidgetsBundles, loadedWidgetsBundles);
}

```java:llm_gen

@Test
public void testFindSystemWidgetsBundlesByPageLink() {
    TenantId tenantId = TenantId.fromUUID(ModelConstants.NULL_UUID);
    List<WidgetsBundle> systemWidgetsBundles = widgetsBundleService.findSystemWidgetsBundles(tenantId);
    List<WidgetsBundle> createdWidgetsBundles = new ArrayList<>();
    for (int i = 0; i < 235; i++) {
        WidgetsBundle widgetsBundle = new WidgetsBundle();
        widgetsBundle.setTenantId(tenantId);
        widgetsBundle.setTitle("Widgets bundle " + i);
        createdWidgetsBundles.add(widgetsBundleService.saveWidgetsBundle(widgetsBundle));
    }
    List<WidgetsBundle> widgetsBundles = new ArrayList<>(createdWidgetsBundles);
    widgetsBundles.addAll(systemWidgetsBundles);
    List<WidgetsBundle> loadedWidgetsBundles = new ArrayList<>();
    PageLink pageLink = new PageLink(19);
    PageData<WidgetsBundle> pageData = null;
    do {
        pageData = widgetsBundleService.findSystemWidgetsBundlesByPageLink(tenantId, false, pageLink);
        loadedWidgetsBundles.addAll(pageData.getData());
        if (pageData.hasNext()) {
            pageLink = pageLink.nextPageLink();
        }
    } while (pageData.hasNext());
    Collections.sort(widgetsBundles, idComparator);
    Collections.sort(loadedWidgetsBundles, idComparator);
    Assert.assertEquals(widgetsBundles, loadedWidgetsBundles);
    for (WidgetsBundle widgetsBundle : createdWidgetsBundles) {
        widgetsBundleService.deleteWidgetsBundle(tenantId, widgetsBundle.getId());
    }
    loadedWidgetsBundles = widgetsBundleService.findSystemWidgetsBundles(tenantId);
    Collections.sort(systemWidgetsBundles, idComparator);
    Collections.sort(loadedWidgetsBundles, idComparator);
    Assert.assertEquals(systemWidgetsBundles, loadedWidgetsBundles);
}

### 63.Correct
link: https://github.com/apache/kylin/commit/085d7072167bf199094833ef73f0d9cc5741b075
p_path: src/tool/src/main/java/org/apache/kylin/tool/util/ProjectTemporaryTableCleanerHelper.java#getJobTransactionalTable
t_path: src/tool/src/test/java/org/apache/kylin/tool/util/ProjectTemporaryTableCleanerHelperTest.java#testGetJobTransactionalTable

```java:test_src

@Test
public void testGetJobTransactionalTable() throws IOException {
    String project = "default";
    String jobId = "job-5c5851ef8544";
    {
        Set<String> tables = tableCleanerHelper.getJobTransactionalTable(project, jobId);
        Assert.assertTrue(tables.isEmpty());
    }
    {
        createHDFSFile(project, jobId);
        Set<String> tables = tableCleanerHelper.getJobTransactionalTable(project, jobId);
        Assert.assertFalse(tables.isEmpty());
    }
}

```java:test_tgt

@Test
public void testGetJobTransactionalTable() throws IOException {
    String project = "default";
    String jobId = "job-5c5851ef8544";
    FileSystem fs = HadoopUtil.getWorkingFileSystem();
    {
        Set<String> tables = tableCleanerHelper.getJobTransactionalTable(project, jobId, fs);
        Assert.assertTrue(tables.isEmpty());
    }
    {
        createHDFSFile(project, jobId);
        Set<String> tables = tableCleanerHelper.getJobTransactionalTable(project, jobId, fs);
        Assert.assertFalse(tables.isEmpty());
    }
}

```java:llm_gen

@Test
public void testGetJobTransactionalTable() throws IOException {
    String project = "default";
    String jobId = "job-5c5851ef8544";
    FileSystem fs = HadoopUtil.getWorkingFileSystem();
    {
        Set<String> tables = tableCleanerHelper.getJobTransactionalTable(project, jobId, fs);
        Assert.assertTrue(tables.isEmpty());
    }
    {
        createHDFSFile(project, jobId);
        Set<String> tables = tableCleanerHelper.getJobTransactionalTable(project, jobId, fs);
        Assert.assertFalse(tables.isEmpty());
    }
}

### 64.Correct
link: https://github.com/dhis2/dhis2-core/commit/c0a2ee0b38a9edad4bfe6b82c2a8e17928b40f06
p_path: dhis-2/dhis-services/dhis-service-analytics/src/main/java/org/hisp/dhis/analytics/table/JdbcOwnershipAnalyticsTableManager.java#getPartitionChecks
t_path: dhis-2/dhis-services/dhis-service-analytics/src/test/java/org/hisp/dhis/analytics/table/JdbcOwnershipAnalyticsTableManagerTest.java#testGetPartitionChecks

```java:test_src

@Test
void testGetPartitionChecks() {
    assertEquals(emptyList(), target.getPartitionChecks(partitionA));
}

```java:test_tgt

@Test
void testGetPartitionChecks() {
    assertTrue(target.getPartitionChecks(1, new Date()).isEmpty());
}

```java:llm_gen

@Test
void testGetPartitionChecks() {
    assertEquals(List.of(), target.getPartitionChecks(2023, new Date()));
}

### 65.Correct
link: https://github.com/apache/flink/commit/a886339dbb36b11bc8bb96d35882223583ac3763
p_path: flink-runtime/src/main/java/org/apache/flink/runtime/io/network/partition/hybrid/tiered/tier/memory/MemoryTierProducerAgent.java#tryStartNewSegment
t_path: flink-runtime/src/test/java/org/apache/flink/runtime/io/network/partition/hybrid/tiered/tier/memory/MemoryTierProducerAgentTest.java#testTryStartNewSegment

```java:test_src

@Test
void testTryStartNewSegment() {
    try (MemoryTierProducerAgent memoryTierProducerAgent = createMemoryTierProducerAgent(false)) {
        assertThat(memoryTierProducerAgent.tryStartNewSegment(SUBPARTITION_ID, 0)).isFalse();
        memoryTierProducerAgent.connectionEstablished(SUBPARTITION_ID, new TestingNettyConnectionWriter.Builder().build());
        assertThat(memoryTierProducerAgent.tryStartNewSegment(SUBPARTITION_ID, 0)).isTrue();
    }
}

```java:test_tgt

@Test
void testTryStartNewSegment() {
    try (MemoryTierProducerAgent memoryTierProducerAgent = createMemoryTierProducerAgent(false)) {
        assertThat(memoryTierProducerAgent.tryStartNewSegment(SUBPARTITION_ID, 0, 0)).isFalse();
        memoryTierProducerAgent.connectionEstablished(SUBPARTITION_ID, new TestingNettyConnectionWriter.Builder().build());
        assertThat(memoryTierProducerAgent.tryStartNewSegment(SUBPARTITION_ID, 0, 0)).isTrue();
    }
}

```java:llm_gen

@Test
void testTryStartNewSegment() {
    try (MemoryTierProducerAgent memoryTierProducerAgent = createMemoryTierProducerAgent(false)) {
        assertThat(memoryTierProducerAgent.tryStartNewSegment(SUBPARTITION_ID, 0, 0)).isFalse();
        memoryTierProducerAgent.connectionEstablished(SUBPARTITION_ID, new TestingNettyConnectionWriter.Builder().build());
        assertThat(memoryTierProducerAgent.tryStartNewSegment(SUBPARTITION_ID, 0, 0)).isTrue();
    }
}

### 66.Field/Package Information Modification
link: https://github.com/relayrides/pushy/commit/c9f92fb90a24be73f2f1e7fbeedf4be86d75ebf0
p_path: micrometer-metrics-listener/src/main/java/com/eatthepath/pushy/apns/metrics/micrometer/MicrometerApnsClientMetricsListener.java#handleNotificationSent
t_path: micrometer-metrics-listener/src/test/java/com/eatthepath/pushy/apns/metrics/micrometer/MicrometerApnsClientMetricsListenerTest.java#testHandleNotificationSent

```java:test_src

@Test
public void testHandleNotificationSent() {
    final Counter sentNotifications = this.meterRegistry.get(MicrometerApnsClientMetricsListener.SENT_NOTIFICATIONS_COUNTER_NAME).counter();
    assertEquals(0, (int) sentNotifications.count());
    this.listener.handleNotificationSent(null, 1);
    assertEquals(1, (int) sentNotifications.count());
}

```java:test_tgt

@Test
public void testHandleNotificationSent() {
    this.listener.handleNotificationSent("com.example.topic");
    assertEquals(1, (int) this.meterRegistry.get(MicrometerApnsClientMetricsListener.SENT_NOTIFICATIONS_COUNTER_NAME).counter().count());
}

```java:llm_gen

@Test
public void testHandleNotificationSent() {
    final Counter sentNotifications = this.meterRegistry.get(MicrometerApnsClientMetricsListener.SENT_NOTIFICATIONS_COUNTER_NAME)
            .counter();
    assertEquals(0, (int) sentNotifications.count());
    this.listener.handleNotificationSent("testTopic");
    assertEquals(1, (int) sentNotifications.count());
}

### 67.Field/Package Information Modification
link: https://github.com/confluentinc/ksql/commit/08eb59f516a8a19c348516fa8f7a995c1d1820ea
p_path: ksqldb-engine/src/main/java/io/confluent/ksql/services/DefaultConnectClient.java#delete
t_path: ksqldb-engine/src/test/java/io/confluent/ksql/services/DefaultConnectClientTest.java#testDelete

```java:test_src

@Test
public void testDelete() throws JsonProcessingException {
    WireMock.stubFor(WireMock.delete(WireMock.urlEqualTo("/connectors/foo")).withHeader(AUTHORIZATION.toString(), new EqualToPattern(AUTH_HEADER)).willReturn(WireMock.aResponse().withStatus(HttpStatus.SC_NO_CONTENT)));
    final ConnectResponse<String> response = client.delete("foo");
    assertThat(response.datum(), OptionalMatchers.of(is("foo")));
    assertThat("Expected no error!", !response.error().isPresent());
}

```java:test_tgt

@Test
public void testDelete() throws JsonProcessingException {
    WireMock.stubFor(WireMock.delete(WireMock.urlEqualTo(pathPrefix + "/connectors/foo")).withHeader(AUTHORIZATION.toString(), new EqualToPattern(AUTH_HEADER)).withHeader(CUSTOM_HEADER_NAME, new EqualToPattern(CUSTOM_HEADER_VALUE)).willReturn(WireMock.aResponse().withStatus(HttpStatus.SC_NO_CONTENT)));
    final ConnectResponse<String> response = client.delete("foo");
    assertThat(response.datum(), OptionalMatchers.of(is("foo")));
    assertThat("Expected no error!", !response.error().isPresent());
}

```java:llm_gen

@Test
public void testDelete() throws JsonProcessingException {
    WireMock.stubFor(WireMock.delete(WireMock.urlEqualTo("/connectors/foo"))
        .withHeader(AUTHORIZATION.toString(), new EqualToPattern(AUTH_HEADER))
        .willReturn(WireMock.aResponse().withStatus(HttpStatus.SC_NO_CONTENT));
    final ConnectResponse<String> response = client.delete("foo");
    assertThat(response.datum(), OptionalMatchers.of(is("foo")));
    assertThat("Expected no error!", !response.error().isPresent());
}

### 68.External Class Modification
link: https://github.com/apache/kafka/commit/bf88013a2812cab65bc70667e451e0a15d26b73c
p_path: group-coordinator/src/main/java/org/apache/kafka/coordinator/group/CoordinatorRecordHelpers.java#newOffsetCommitRecord
t_path: group-coordinator/src/test/java/org/apache/kafka/coordinator/group/CoordinatorRecordHelpersTest.java#testNewOffsetCommitRecord

```java:test_src

@ParameterizedTest
@EnumSource(value = MetadataVersion.class)
public void testNewOffsetCommitRecord(MetadataVersion metadataVersion) {
    OffsetCommitKey key = new OffsetCommitKey().setGroup("group-id").setTopic("foo").setPartition(1);
    OffsetCommitValue value = new OffsetCommitValue().setOffset(100L).setLeaderEpoch(10).setMetadata("metadata").setCommitTimestamp(1234L).setExpireTimestamp(-1L);
    Record expectedRecord = new Record(new ApiMessageAndVersion(key, (short) 1), new ApiMessageAndVersion(value, metadataVersion.offsetCommitValueVersion(false)));
    assertEquals(expectedRecord, RecordHelpers.newOffsetCommitRecord("group-id", "foo", 1, new OffsetAndMetadata(100L, OptionalInt.of(10), "metadata", 1234L, OptionalLong.empty()), metadataVersion));
    value.setLeaderEpoch(-1);
    assertEquals(expectedRecord, RecordHelpers.newOffsetCommitRecord("group-id", "foo", 1, new OffsetAndMetadata(100L, OptionalInt.empty(), "metadata", 1234L, OptionalLong.empty()), metadataVersion));
}

```java:test_tgt

@ParameterizedTest
@EnumSource(value = MetadataVersion.class)
public void testNewOffsetCommitRecord(MetadataVersion metadataVersion) {
    OffsetCommitKey key = new OffsetCommitKey().setGroup("group-id").setTopic("foo").setPartition(1);
    OffsetCommitValue value = new OffsetCommitValue().setOffset(100L).setLeaderEpoch(10).setMetadata("metadata").setCommitTimestamp(1234L).setExpireTimestamp(-1L);
    CoordinatorRecord expectedRecord = new CoordinatorRecord(new ApiMessageAndVersion(key, (short) 1), new ApiMessageAndVersion(value, metadataVersion.offsetCommitValueVersion(false)));
    assertEquals(expectedRecord, CoordinatorRecordHelpers.newOffsetCommitRecord("group-id", "foo", 1, new OffsetAndMetadata(100L, OptionalInt.of(10), "metadata", 1234L, OptionalLong.empty()), metadataVersion));
    value.setLeaderEpoch(-1);
    assertEquals(expectedRecord, CoordinatorRecordHelpers.newOffsetCommitRecord("group-id", "foo", 1, new OffsetAndMetadata(100L, OptionalInt.empty(), "metadata", 1234L, OptionalLong.empty()), metadataVersion));
}

```java:llm_gen

@ParameterizedTest
@EnumSource(value = MetadataVersion.class)
public void testNewOffsetCommitRecord(MetadataVersion metadataVersion) {
    OffsetCommitKey key = new OffsetCommitKey().setGroup("group-id").setTopic("foo").setPartition(1);
    OffsetCommitValue value = new OffsetCommitValue().setOffset(100L).setLeaderEpoch(10).setMetadata("metadata").setCommitTimestamp(1234L).setExpireTimestamp(-1L);
    CoordinatorRecord expectedRecord = new CoordinatorRecord(new ApiMessageAndVersion(key, (short) 1), new ApiMessageAndVersion(value, metadataVersion.offsetCommitValueVersion(false)));
    assertEquals(expectedRecord, RecordHelpers.newOffsetCommitRecord("group-id", "foo", 1, new OffsetAndMetadata(100L, OptionalInt.of(10), "metadata", 1234L, OptionalLong.empty()), metadataVersion));
    value.setLeaderEpoch(-1);
    assertEquals(expectedRecord, RecordHelpers.newOffsetCommitRecord("group-id", "foo", 1, new OffsetAndMetadata(100L, OptionalInt.empty(), "metadata", 1234L, OptionalLong.empty()), metadataVersion));
}

### 69.Wrong Update Direction
link: https://github.com/linkedin/venice/commit/dde97f53a4e7629f707f2976c96a8b07c1b58dec
p_path: clients/da-vinci-client/src/main/java/com/linkedin/davinci/kafka/consumer/StoreIngestionTask.java#getOffsetToOnlineLagThresholdPerPartition
t_path: clients/da-vinci-client/src/test/java/com/linkedin/davinci/kafka/consumer/StoreIngestionTaskTest.java#testGetOffsetToOnlineLagThresholdPerPartition

```java:test_src

@Test
public void testGetOffsetToOnlineLagThresholdPerPartition() {
    ReadOnlyStoreRepository storeRepository = mock(ReadOnlyStoreRepository.class);
    String storeName = "test-store";
    int subPartitionCount = 10;
    assertThrows(VeniceException.class, () -> StoreIngestionTask.getOffsetToOnlineLagThresholdPerPartition(Optional.empty(), storeRepository, storeName, subPartitionCount));
    HybridStoreConfigImpl hybridStoreConfig1 = new HybridStoreConfigImpl(100l, -1l, 100l, DataReplicationPolicy.NON_AGGREGATE, BufferReplayPolicy.REWIND_FROM_SOP);
    assertEquals(StoreIngestionTask.getOffsetToOnlineLagThresholdPerPartition(Optional.of(hybridStoreConfig1), storeRepository, storeName, subPartitionCount), -1l);
    HybridStoreConfigImpl hybridStoreConfig2 = new HybridStoreConfigImpl(100l, 100l, 100l, DataReplicationPolicy.NON_AGGREGATE, BufferReplayPolicy.REWIND_FROM_SOP);
    Store store = mock(Store.class);
    doReturn(10).when(store).getCurrentVersion();
    doReturn(store).when(storeRepository).getStore(storeName);
    assertEquals(StoreIngestionTask.getOffsetToOnlineLagThresholdPerPartition(Optional.of(hybridStoreConfig2), storeRepository, storeName, subPartitionCount), 10l);
}

```java:test_tgt

@Test
public void testGetOffsetToOnlineLagThresholdPerPartition() {
    ReadOnlyStoreRepository storeRepository = mock(ReadOnlyStoreRepository.class);
    String storeName = "test-store";
    int subPartitionCount = 10;
    assertThrows(VeniceException.class, () -> StoreIngestionTask.getOffsetToOnlineLagThresholdPerPartition(Optional.empty(), storeName, subPartitionCount));
    HybridStoreConfigImpl hybridStoreConfig1 = new HybridStoreConfigImpl(100l, -1l, 100l, DataReplicationPolicy.NON_AGGREGATE, BufferReplayPolicy.REWIND_FROM_SOP);
    assertEquals(StoreIngestionTask.getOffsetToOnlineLagThresholdPerPartition(Optional.of(hybridStoreConfig1), storeName, subPartitionCount), -1l);
    HybridStoreConfigImpl hybridStoreConfig2 = new HybridStoreConfigImpl(100l, 100l, 100l, DataReplicationPolicy.NON_AGGREGATE, BufferReplayPolicy.REWIND_FROM_SOP);
    Store store = mock(Store.class);
    doReturn(10).when(store).getCurrentVersion();
    doReturn(store).when(storeRepository).getStore(storeName);
    assertEquals(StoreIngestionTask.getOffsetToOnlineLagThresholdPerPartition(Optional.of(hybridStoreConfig2), storeName, subPartitionCount), 10l);
}

```java:llm_gen

@Test
public void testGetOffsetToOnlineLagThresholdPerPartition() {
    ReadOnlyStoreRepository storeRepository = mock(ReadOnlyStoreRepository.class);
    String storeName = "test-store";
    int subPartitionCount = 10;
    HybridStoreConfigImpl hybridStoreConfig1 = new HybridStoreConfigImpl(100l, -1l, 100l, DataReplicationPolicy.NON_AGGREGATE, BufferReplayPolicy.REWIND_FROM_SOP);
    assertEquals(StoreIngestionTask.getOffsetToOnlineLagThresholdPerPartition(Optional.of(hybridStoreConfig1), storeRepository, storeName, subPartitionCount), -1l);
    HybridStoreConfigImpl hybridStoreConfig2 = new HybridStoreConfigImpl(100l, 100l, 100l, DataReplicationPolicy.NON_AGGREGATE, BufferReplayPolicy.REWIND_FROM_SOP);
    Store store = mock(Store.class);
    doReturn(10).when(store).getCurrentVersion();
    doReturn(store).when(storeRepository).getStore(storeName);
    assertEquals(StoreIngestionTask.getOffsetToOnlineLagThresholdPerPartition(Optional.of(hybridStoreConfig2), storeRepository, storeName, subPartitionCount), 10l);
}

### 70.Correct
link: https://github.com/apache/kafka/commit/bf88013a2812cab65bc70667e451e0a15d26b73c
p_path: group-coordinator/src/main/java/org/apache/kafka/coordinator/group/CoordinatorRecordHelpers.java#newGroupEpochRecord
t_path: group-coordinator/src/test/java/org/apache/kafka/coordinator/group/CoordinatorRecordHelpersTest.java#testNewGroupEpochRecord

```java:test_src

@Test
public void testNewGroupEpochRecord() {
    Record expectedRecord = new Record(new ApiMessageAndVersion(new ConsumerGroupMetadataKey().setGroupId("group-id"), (short) 3), new ApiMessageAndVersion(new ConsumerGroupMetadataValue().setEpoch(10), (short) 0));
    assertEquals(expectedRecord, newGroupEpochRecord("group-id", 10));
}

```java:test_tgt

@Test
public void testNewGroupEpochRecord() {
    CoordinatorRecord expectedRecord = new CoordinatorRecord(new ApiMessageAndVersion(new ConsumerGroupMetadataKey().setGroupId("group-id"), (short) 3), new ApiMessageAndVersion(new ConsumerGroupMetadataValue().setEpoch(10), (short) 0));
    assertEquals(expectedRecord, newGroupEpochRecord("group-id", 10));
}

```java:llm_gen

@Test
public void testNewGroupEpochRecord() {
    CoordinatorRecord expectedRecord = new CoordinatorRecord(new ApiMessageAndVersion(new ConsumerGroupMetadataKey().setGroupId("group-id"), (short) 3), new ApiMessageAndVersion(new ConsumerGroupMetadataValue().setEpoch(10), (short) 0));
    assertEquals(expectedRecord, newGroupEpochRecord("group-id", 10));
}

### 71.Assert Error
link: https://github.com/apache/dolphinscheduler/commit/e9d85914d78197314bee585500d94a6a90733789
p_path: dolphinscheduler-dao/src/main/java/org/apache/dolphinscheduler/dao/mapper/TriggerRelationMapper.java#queryByTypeAndJobId
t_path: dolphinscheduler-dao/src/test/java/org/apache/dolphinscheduler/dao/mapper/TriggerRelationMapperTest.java#testQueryByTypeAndJobId

```java:test_src

@Test
public void testQueryByTypeAndJobId() {
    TriggerRelation expectRelation = createTriggerRelation();
    TriggerRelation actualRelation = triggerRelationMapper.queryByTypeAndJobId(expectRelation.getTriggerType(), expectRelation.getJobId());
    Assertions.assertEquals(expectRelation, actualRelation);
}

```java:test_tgt

@Test
public void testQueryByTypeAndJobId() {
    TriggerRelation expectRelation = createTriggerRelation();
    assertThat(triggerRelationMapper.queryByTypeAndJobId(expectRelation.getTriggerType(), expectRelation.getJobId())).containsExactly(expectRelation);
}

```java:llm_gen

@Test
public void testQueryByTypeAndJobId() {
    List<TriggerRelation> expectRelations = Arrays.asList(createTriggerRelation());
    List<TriggerRelation> actualRelations = triggerRelationMapper.queryByTypeAndJobId(expectRelations.get(0).getTriggerType(), expectRelations.get(0).getJobId());
    Assertions.assertEquals(expectRelations, actualRelations);
}

### 72.Correct
link: https://github.com/dita-ot/dita-ot/commit/adb193a560b9373e539735aed4f8dab56085b66a
p_path: src/main/java/org/dita/dost/platform/PluginRequirement.java#getPlugins
t_path: src/test/java/org/dita/dost/platform/PluginRequirementTest.java#testGetPlugins

```java:test_src

@Test
public void testGetPlugins() {
    final PluginRequirement pr = new PluginRequirement();
    pr.addPlugins("foo | bar | baz");
    final List<String> act = new ArrayList<>();
    for (final Iterator<String> i = pr.getPlugins(); i.hasNext(); ) {
        act.add(i.next());
    }
    assertArrayEquals(new String[] { "foo ", " bar ", " baz" }, act.toArray(new String[0]));
}

```java:test_tgt

@Test
public void testGetPlugins() {
    final PluginRequirement pr = new PluginRequirement();
    pr.addPlugins("foo | bar | baz");
    final List<String> act = pr.getPlugins();
    assertArrayEquals(new String[] { "foo ", " bar ", " baz" }, act.toArray(new String[0]));
}

```java:llm_gen

@Test
public void testGetPlugins() {
    final PluginRequirement pr = new PluginRequirement();
    pr.addPlugins("foo | bar | baz");
    final List<String> act = pr.getPlugins();
    assertArrayEquals(new String[] { "foo ", " bar ", " baz" }, act.toArray(new String[0]));
}

### 73.Wrong Update Direction
link: https://github.com/BentoBoxWorld/BentoBox/commit/b1fe76c45d693b6bbd3f4d87e013041fcb341934
p_path: src/main/java/world/bentobox/bentobox/api/commands/island/team/IslandTeamCommand.java#addInvite
t_path: src/test/java/world/bentobox/bentobox/api/commands/island/team/IslandTeamCommandTest.java#testAddInvite

```java:test_src

@Test
public void testAddInvite() {
    tc.addInvite(Invite.Type.TEAM, uuid, invitee, island);
    assertTrue(tc.isInvited(invitee));
}

```java:test_tgt

@Test
public void testAddInvite() throws IllegalAccessException, InvocationTargetException, IntrospectionException {
    tc.addInvite(Type.TEAM, uuid, invitee, island);
    verify(h, atLeast(1)).saveObject(any());
}

```java:llm_gen

@Test
public void testAddInvite() {
    tc.addInvite(TeamInvite.Type.TEAM, uuid, invitee, island);
    assertTrue(tc.isInvited(invitee));
}

### 74.External Class Modification
link: https://github.com/dremio/dremio-oss/commit/12d7a954966ee5782921a4fbe32cc4568cbf631b
p_path: sabot/kernel/src/main/java/com/dremio/exec/planner/sql/handlers/direct/DescribeTableHandler.java#toResult
t_path: sabot/kernel/src/test/java/com/dremio/exec/planner/sql/handlers/direct/TestDescribeTableHandler.java#testToResult

```java:test_src

@Test
public void testToResult() throws Exception {
    SqlDescribeTable describeTable = new SqlDescribeTable(SqlParserPos.ZERO, new SqlIdentifier(TABLE, SqlParserPos.ZERO), null);
    final List<DescribeTableHandler.DescribeResult> actualResults = describeTableHandler.toResult("foo", describeTable);
    final List<DescribeTableHandler.DescribeResult> expectedResults = Lists.newArrayList(new DescribeTableHandler.DescribeResult("col1", "CHARACTER VARYING", null, null, "[]", "[]", null), new DescribeTableHandler.DescribeResult("col2", "BOOLEAN", null, null, "[{\"key\":\"one\",\"value\":\"foo\"}]", "[]", null), new DescribeTableHandler.DescribeResult("col3", "DECIMAL", 5, 2, "[{\"key\":\"two\",\"value\":\"bar\"},{\"key\":\"three\",\"value\":\"baz\"}]", "[]", null));
    assertEquals(expectedResults.size(), actualResults.size());
    for (int i = 0; i < expectedResults.size(); i++) {
        verifyDescribeResult(expectedResults.get(i), actualResults.get(i));
    }
}

```java:test_tgt

@Test
public void testToResult() throws Exception {
    SqlDescribeDremioTable describeTable = new SqlDescribeDremioTable(SqlParserPos.ZERO, new SqlIdentifier(TABLE, SqlParserPos.ZERO), SqlTableVersionSpec.NOT_SPECIFIED, null);
    final List<DescribeTableHandler.DescribeResult> actualResults = describeTableHandler.toResult("foo", describeTable);
    final List<DescribeTableHandler.DescribeResult> expectedResults = Lists.newArrayList(new DescribeTableHandler.DescribeResult("col1", "CHARACTER VARYING", null, null, "[]", "[]", null), new DescribeTableHandler.DescribeResult("col2", "BOOLEAN", null, null, "[{\"key\":\"one\",\"value\":\"foo\"}]", "[]", null), new DescribeTableHandler.DescribeResult("col3", "DECIMAL", 5, 2, "[{\"key\":\"two\",\"value\":\"bar\"},{\"key\":\"three\",\"value\":\"baz\"}]", "[]", null));
    assertEquals(expectedResults.size(), actualResults.size());
    for (int i = 0; i < expectedResults.size(); i++) {
        verifyDescribeResult(expectedResults.get(i), actualResults.get(i));
    }
}

```java:llm_gen

@Test
public void testToResult() throws Exception {
    SqlDescribeTable describeTable = new SqlDescribeTable(SqlParserPos.ZERO, new SqlIdentifier(TABLE, SqlParserPos.ZERO), null, null);
    final List<DescribeTableHandler.DescribeResult> actualResults = describeTableHandler.toResult("foo", describeTable);
    final List<DescribeTableHandler.DescribeResult> expectedResults = Lists.newArrayList(new DescribeTableHandler.DescribeResult("col1", "CHARACTER VARYING", null, null, "[]", "[]", null), new DescribeTableHandler.DescribeResult("col2", "BOOLEAN", null, null, "[{\"key\":\"one\",\"value\":\"foo\"}]", "[]", null), new DescribeTableHandler.DescribeResult("col3", "DECIMAL", 5, 2, "[{\"key\":\"two\",\"value\":\"bar\"},{\"key\":\"three\",\"value\":\"baz\"}]", "[]", null));
    assertEquals(expectedResults.size(), actualResults.size());
    for (int i = 0; i < expectedResults.size(); i++) {
        verifyDescribeResult(expectedResults.get(i), actualResults.get(i));
    }
}

### 75.External Function Modification
link: https://github.com/halo-dev/halo/commit/0e17d53ede66c57b12f2dec4c92874c7e69ed9ef
p_path: application/src/main/java/run/halo/app/content/comment/ReplyNotificationSubscriptionHelper.java#subscribeNewReplyReasonForComment
t_path: application/src/test/java/run/halo/app/content/comment/ReplyNotificationSubscriptionHelperTest.java#subscribeNewReplyReasonForCommentTest

````java:test_src

@Test
void subscribeNewReplyReasonForCommentTest() {
    var comment = createComment();
    var spyNotificationSubscriptionHelper = spy(notificationSubscriptionHelper);
    doNothing().when(spyNotificationSubscriptionHelper).subscribeReply(any(), any());
    spyNotificationSubscriptionHelper.subscribeNewReplyReasonForComment(comment);
    var reasonSubject = Subscription.ReasonSubject.builder().apiVersion(comment.getApiVersion()).kind(comment.getKind()).name(comment.getMetadata().getName()).build();
    verify(spyNotificationSubscriptionHelper).subscribeReply(eq(reasonSubject), eq(ReplyNotificationSubscriptionHelper.Identity.fromCommentOwner(comment.getSpec().getOwner())));
}

```java:test_tgt

@Test
void subscribeNewReplyReasonForCommentTest() {
    var comment = createComment();
    var spyNotificationSubscriptionHelper = spy(notificationSubscriptionHelper);
    doNothing().when(spyNotificationSubscriptionHelper).subscribeReply(any(UserIdentity.class));
    spyNotificationSubscriptionHelper.subscribeNewReplyReasonForComment(comment);
    verify(spyNotificationSubscriptionHelper).subscribeReply(eq(ReplyNotificationSubscriptionHelper.identityFrom(comment.getSpec().getOwner())));
}

```java:llm_gen

@Test
void subscribeNewReplyReasonForCommentTest() {
    var comment = createComment();
    var spyNotificationSubscriptionHelper = spy(notificationSubscriptionHelper);
    doNothing().when(spyNotificationSubscriptionHelper).subscribeReply(any(), any());
    spyNotificationSubscriptionHelper.subscribeNewReplyReasonForComment(comment);
    verify(spyNotificationSubscriptionHelper).subscribeReply(eq(ReplyNotificationSubscriptionHelper.identityFrom(comment.getSpec().getOwner())), any());
}

### 76.Correct
link: https://github.com/apache/flink/commit/c8f27c25e8726360bd09fd21fa8e908c40376881
p_path: flink-runtime/src/main/java/org/apache/flink/runtime/clusterframework/BootstrapTools.java#updateTmpDirectoriesInConfiguration
t_path: flink-runtime/src/test/java/org/apache/flink/runtime/clusterframework/BootstrapToolsTest.java#testUpdateTmpDirectoriesInConfiguration

```java:test_src

@Test
void testUpdateTmpDirectoriesInConfiguration() {
    Configuration config = new Configuration();
    BootstrapTools.updateTmpDirectoriesInConfiguration(config, "default/directory/path");
    assertThat(config.getString(CoreOptions.TMP_DIRS)).isEqualTo("default/directory/path");
    BootstrapTools.updateTmpDirectoriesInConfiguration(config, "not/default/directory/path");
    assertThat(config.getString(CoreOptions.TMP_DIRS)).isEqualTo("default/directory/path");
    config.setString(CoreOptions.TMP_DIRS, "");
    BootstrapTools.updateTmpDirectoriesInConfiguration(config, "some/new/path");
    assertThat(config.getString(CoreOptions.TMP_DIRS)).isEmpty();
}

```java:test_tgt

@Test
void testUpdateTmpDirectoriesInConfiguration() {
    Configuration config = new Configuration();
    BootstrapTools.updateTmpDirectoriesInConfiguration(config, "default/directory/path");
    assertThat(config.get(CoreOptions.TMP_DIRS)).isEqualTo("default/directory/path");
    BootstrapTools.updateTmpDirectoriesInConfiguration(config, "not/default/directory/path");
    assertThat(config.get(CoreOptions.TMP_DIRS)).isEqualTo("default/directory/path");
    config.set(CoreOptions.TMP_DIRS, "");
    BootstrapTools.updateTmpDirectoriesInConfiguration(config, "some/new/path");
    assertThat(config.get(CoreOptions.TMP_DIRS)).isEmpty();
}

```java:llm_gen

@Test
void testUpdateTmpDirectoriesInConfiguration() {
    Configuration config = new Configuration();
    BootstrapTools.updateTmpDirectoriesInConfiguration(config, "default/directory/path");
    assertThat(config.get(CoreOptions.TMP_DIRS)).isEqualTo("default/directory/path");
    BootstrapTools.updateTmpDirectoriesInConfiguration(config, "not/default/directory/path");
    assertThat(config.get(CoreOptions.TMP_DIRS)).isEqualTo("default/directory/path");
    config.set(CoreOptions.TMP_DIRS, "");
    BootstrapTools.updateTmpDirectoriesInConfiguration(config, "some/new/path");
    assertThat(config.get(CoreOptions.TMP_DIRS)).isEmpty();
}

### 77.Test Preparation Error
link: https://github.com/questdb/questdb/commit/e065400768734bde734149b1272b0f2f8968f779
p_path: core/src/main/java/io/questdb/std/str/Utf8s.java#utf8CharDecode
t_path: core/src/test/java/io/questdb/test/std/str/Utf8sTest.java#testUtf8CharDecode

```java:test_src

@Test
public void testUtf8CharDecode() {
    long p = Unsafe.malloc(8, MemoryTag.NATIVE_DEFAULT);
    try {
        testUtf8Char("A", p, false);
        testUtf8Char("Ч", p, false);
        testUtf8Char("∆", p, false);
        testUtf8Char("\uD83D\uDE00\"", p, true);
    } finally {
        Unsafe.free(p, 8, MemoryTag.NATIVE_DEFAULT);
    }
}

```java:test_tgt

@Test
public void testUtf8CharDecode() {
    try (DirectUtf8Sink sink = new DirectUtf8Sink(8)) {
        testUtf8Char("A", sink, false);
        testUtf8Char("Ч", sink, false);
        testUtf8Char("∆", sink, false);
        testUtf8Char("\uD83D\uDE00\"", sink, true);
    }
}

```java:llm_gen

@Test
public void testUtf8CharDecode() {
    Utf8Sequence seq = new Utf8Sequence() {
        @Override
        public int size() {
            return bytes.length;
        }

        @Override
        public byte byteAt(int index) {
            return bytes[index];
        }

        private byte[] bytes;

        private void setBytes(String s) {
            this.bytes = s.getBytes(StandardCharsets.UTF_8);
        }
    };

    testUtf8Char("A", seq, false);
    testUtf8Char("Ч", seq, false);
    testUtf8Char("∆", seq, false);
    testUtf8Char("\uD83D\uDE00\"", seq, true);
}

### 78.Test Preparation Error
link: https://github.com/halo-dev/halo/commit/0e17d53ede66c57b12f2dec4c92874c7e69ed9ef
p_path: application/src/main/java/run/halo/app/notification/DefaultNotificationCenter.java#notify
t_path: application/src/test/java/run/halo/app/notification/DefaultNotificationCenterTest.java#testNotify

````java:test_src

@Test
public void testNotify() {
    final Reason reason = new Reason();
    final Reason.Spec spec = new Reason.Spec();
    Reason.Subject subject = new Reason.Subject();
    subject.setApiVersion("content.halo.run/v1alpha1");
    subject.setKind("Comment");
    subject.setName("comment-a");
    spec.setSubject(subject);
    spec.setReasonType("new-reply-on-comment");
    spec.setAttributes(null);
    reason.setSpec(spec);
    reason.setMetadata(new Metadata());
    reason.getMetadata().setName("reason-a");
    var subscriptionReasonSubject = createNewReplyOnCommentSubject();
    var spyNotificationCenter = spy(notificationCenter);
    var subscriptions = createSubscriptions();
    doReturn(Flux.fromIterable(subscriptions)).when(spyNotificationCenter).listObservers(eq("new-reply-on-comment"), eq(subscriptionReasonSubject));
    doReturn(Mono.empty()).when(spyNotificationCenter).dispatchNotification(eq(reason), any());
    spyNotificationCenter.notify(reason).block();
    verify(spyNotificationCenter).dispatchNotification(eq(reason), any());
    verify(spyNotificationCenter).listObservers(eq("new-reply-on-comment"), eq(subscriptionReasonSubject));
}

```java:test_tgt

@Test
public void testNotify() {
    final Reason reason = new Reason();
    final Reason.Spec spec = new Reason.Spec();
    Reason.Subject subject = new Reason.Subject();
    subject.setApiVersion("content.halo.run/v1alpha1");
    subject.setKind("Comment");
    subject.setName("comment-a");
    spec.setSubject(subject);
    spec.setReasonType("new-reply-on-comment");
    spec.setAttributes(null);
    reason.setSpec(spec);
    reason.setMetadata(new Metadata());
    reason.getMetadata().setName("reason-a");
    var spyNotificationCenter = spy(notificationCenter);
    var subscriber = new Subscriber(UserIdentity.anonymousWithEmail("A"), "fake-name");
    when(recipientResolver.resolve(reason)).thenReturn(Flux.just(subscriber));
    doReturn(Mono.empty()).when(spyNotificationCenter).dispatchNotification(eq(reason), any());
    spyNotificationCenter.notify(reason).block();
    verify(spyNotificationCenter).dispatchNotification(eq(reason), any());
    verify(recipientResolver).resolve(eq(reason));
}

```java:llm_gen

@Test
public void testNotify() {
    final Reason reason = new Reason();
    final Reason.Spec spec = new Reason.Spec();
    Reason.Subject subject = new Reason.Subject();
    subject.setApiVersion("content.halo.run/v1alpha1");
    subject.setKind("Comment");
    subject.setName("comment-a");
    spec.setSubject(subject);
    spec.setReasonType("new-reply-on-comment");
    spec.setAttributes(null);
    reason.setSpec(spec);
    reason.setMetadata(new Metadata());
    reason.getMetadata().setName("reason-a");
    var spyNotificationCenter = spy(notificationCenter);
    var subscribers = createSubscribers();
    doReturn(Flux.fromIterable(subscribers)).when(spyNotificationCenter).recipientResolver.resolve(eq(reason));
    doReturn(Mono.empty()).when(spyNotificationCenter).dispatchNotification(eq(reason), any());
    spyNotificationCenter.notify(reason).block();
    verify(spyNotificationCenter).dispatchNotification(eq(reason), any());
    verify(spyNotificationCenter).recipientResolver.resolve(eq(reason));
}

### 79.Correct
link: https://github.com/alibaba/nacos/commit/849393c4a1eeaeee20dbbd7101cf60b36f91cf08
p_path: config/src/main/java/com/alibaba/nacos/config/server/service/repository/embedded/EmbeddedConfigInfoPersistServiceImpl.java#findChangeConfig
t_path: config/src/test/java/com/alibaba/nacos/config/server/service/repository/embedded/EmbeddedConfigInfoPersistServiceImplTest.java#testFindChangeConfig

```java:test_src

@Test
public void testFindChangeConfig() {
    List<ConfigInfoWrapper> result = new ArrayList<>();
    result.add(createMockConfigInfoWrapper(0));
    result.add(createMockConfigInfoWrapper(1));
    result.add(createMockConfigInfoWrapper(2));
    Timestamp startTime = new Timestamp(System.currentTimeMillis() - 1000L);
    long lastMaxId = 10000L;
    int pageSize = 30;
    when(databaseOperate.queryMany(anyString(), eq(new Object[] { startTime, lastMaxId, pageSize }), eq(CONFIG_INFO_WRAPPER_ROW_MAPPER))).thenReturn(result);
    List<ConfigInfoWrapper> configInfo4List = embeddedConfigInfoPersistService.findChangeConfig(startTime, lastMaxId, pageSize);
    Assert.assertEquals(result.size(), configInfo4List.size());
}

```java:test_tgt

@Test
public void testFindChangeConfig() {
    List<ConfigInfoStateWrapper> result = new ArrayList<>();
    result.add(createMockConfigInfoStateWrapper(0));
    result.add(createMockConfigInfoStateWrapper(1));
    result.add(createMockConfigInfoStateWrapper(2));
    Timestamp startTime = new Timestamp(System.currentTimeMillis() - 1000L);
    long lastMaxId = 10000L;
    int pageSize = 30;
    when(databaseOperate.queryMany(anyString(), eq(new Object[] { startTime, lastMaxId, pageSize }), eq(CONFIG_INFO_STATE_WRAPPER_ROW_MAPPER))).thenReturn(result);
    List<ConfigInfoStateWrapper> configInfo4List = embeddedConfigInfoPersistService.findChangeConfig(startTime, lastMaxId, pageSize);
    Assert.assertEquals(result.size(), configInfo4List.size());
}

```java:llm_gen

@Test
public void testFindChangeConfig() {
    List<ConfigInfoStateWrapper> result = new ArrayList<>();
    result.add(createMockConfigInfoStateWrapper(0));
    result.add(createMockConfigInfoStateWrapper(1));
    result.add(createMockConfigInfoStateWrapper(2));
    Timestamp startTime = new Timestamp(System.currentTimeMillis() - 1000L);
    long lastMaxId = 10000L;
    int pageSize = 30;
    when(databaseOperate.queryMany(anyString(), eq(new Object[] { startTime, lastMaxId, pageSize }), eq(CONFIG_INFO_STATE_WRAPPER_ROW_MAPPER))).thenReturn(result);
    List<ConfigInfoStateWrapper> configInfo4List = embeddedConfigInfoPersistService.findChangeConfig(startTime, lastMaxId, pageSize);
    Assert.assertEquals(result.size(), configInfo4List.size());
}

### 80.Field/Package Information Modification
link: https://github.com/apache/cayenne/commit/9c7f4187a8fcddd87a29c56daeed6c92bf619bff
p_path: cayenne/src/main/java/org/apache/cayenne/query/PrefetchTreeNode.java#getPath
t_path: cayenne/src/test/java/org/apache/cayenne/query/PrefetchTreeNodeTest.java#testGetPath

```java:test_src

@Test
public void testGetPath() {
    PrefetchTreeNode tree = new PrefetchTreeNode();
    tree.addPath("abc");
    tree.addPath("abc.def.mnk");
    tree.addPath("xyz");
    assertEquals("", tree.getPath());
    PrefetchTreeNode n1 = tree.getNode("abc");
    assertEquals("abc", n1.getPath());
    PrefetchTreeNode n2 = tree.getNode("abc.def");
    assertEquals("abc.def", n2.getPath());
    PrefetchTreeNode n3 = tree.getNode("abc.def.mnk");
    assertEquals("abc.def.mnk", n3.getPath());
    PrefetchTreeNode n4 = tree.getNode("xyz");
    assertEquals("xyz", n4.getPath());
}

```java:test_tgt

@Test
public void testGetPath() {
    PrefetchTreeNode tree = new PrefetchTreeNode();
    tree.addPath("abc");
    tree.addPath("abc.def.mnk");
    tree.addPath("xyz");
    assertEquals(CayennePath.of(""), tree.getPath());
    PrefetchTreeNode n1 = tree.getNode("abc");
    assertEquals(CayennePath.of("abc"), n1.getPath());
    PrefetchTreeNode n2 = tree.getNode("abc.def");
    assertEquals(CayennePath.of("abc.def"), n2.getPath());
    PrefetchTreeNode n3 = tree.getNode("abc.def.mnk");
    assertEquals(CayennePath.of("abc.def.mnk"), n3.getPath());
    PrefetchTreeNode n4 = tree.getNode("xyz");
    assertEquals(CayennePath.of("xyz"), n4.getPath());
}

```java:llm_gen

@Test
public void testGetPath() {
    PrefetchTreeNode tree = new PrefetchTreeNode();
    tree.addPath("abc");
    tree.addPath("abc.def.mnk");
    tree.addPath("xyz");
    assertEquals(CayennePath.EMPTY_PATH, tree.getPath());
    PrefetchTreeNode n1 = tree.getNode("abc");
    assertEquals(CayennePath.of("abc"), n1.getPath());
    PrefetchTreeNode n2 = tree.getNode("abc.def");
    assertEquals(CayennePath.of("abc.def"), n2.getPath());
    PrefetchTreeNode n3 = tree.getNode("abc.def.mnk");
    assertEquals(CayennePath.of("abc.def.mnk"), n3.getPath());
    PrefetchTreeNode n4 = tree.getNode("xyz");
    assertEquals(CayennePath.of("xyz"), n4.getPath());
}

### 81.Correct
link: https://github.com/apache/nifi/commit/ecea18f79655c0e34949d94609c8909aeb2d093e
p_path: nifi-nar-bundles/nifi-apicurio-bundle/nifi-apicurio-schema-registry-service/src/main/java/org/apache/nifi/apicurio/schemaregistry/util/SchemaUtils.java#createRecordSchema
t_path: nifi-nar-bundles/nifi-apicurio-bundle/nifi-apicurio-schema-registry-service/src/test/java/org/apache/nifi/apicurio/schemaregistry/util/SchemaUtilsTest.java#testCreateRecordSchema

```java:test_src

@Test
void testCreateRecordSchema() throws SchemaNotFoundException, IOException {
    final InputStream in = getResource("schema_response.json");
    final RecordSchema schema = SchemaUtils.createRecordSchema(in, "schema1", 3);
    assertEquals("schema1", schema.getSchemaName().orElseThrow(() -> new AssertionError("Schema Name is empty")));
    assertEquals("schema_namespace_1", schema.getSchemaNamespace().orElseThrow(() -> new AssertionError("Schema Namespace is empty")));
    assertEquals("avro", schema.getSchemaFormat().orElseThrow(() -> new AssertionError("Schema Format is empty")));
    final String expectedSchemaText = IOUtils.toString(getResource("schema_response.json"), Charset.defaultCharset()).replace("\n", "").replaceAll(" +", "");
    assertEquals(expectedSchemaText, schema.getSchemaText().orElseThrow(() -> new AssertionError("Schema Text is empty")));
}

```java:test_tgt

@Test
void testCreateRecordSchema() throws SchemaNotFoundException, IOException {
    final InputStream in = getResource("schema_response.json");
    final RecordSchema schema = SchemaUtils.createRecordSchema(in, "schema1", OptionalInt.of(3));
    assertEquals("schema1", schema.getSchemaName().orElseThrow(() -> new AssertionError("Schema Name is empty")));
    assertEquals("schema_namespace_1", schema.getSchemaNamespace().orElseThrow(() -> new AssertionError("Schema Namespace is empty")));
    assertEquals("avro", schema.getSchemaFormat().orElseThrow(() -> new AssertionError("Schema Format is empty")));
    final String expectedSchemaText = IOUtils.toString(getResource("schema_response.json"), Charset.defaultCharset()).replace("\n", "").replaceAll(" +", "");
    assertEquals(expectedSchemaText, schema.getSchemaText().orElseThrow(() -> new AssertionError("Schema Text is empty")));
}

```java:llm_gen

@Test
void testCreateRecordSchema() throws SchemaNotFoundException, IOException {
    final InputStream in = getResource("schema_response.json");
    final RecordSchema schema = SchemaUtils.createRecordSchema(in, "schema1", OptionalInt.of(3));
    assertEquals("schema1", schema.getSchemaName().orElseThrow(() -> new AssertionError("Schema Name is empty")));
    assertEquals("schema_namespace_1", schema.getSchemaNamespace().orElseThrow(() -> new AssertionError("Schema Namespace is empty")));
    assertEquals("avro", schema.getSchemaFormat().orElseThrow(() -> new AssertionError("Schema Format is empty")));
    final String expectedSchemaText = IOUtils.toString(getResource("schema_response.json"), Charset.defaultCharset()).replace("\n", "").replaceAll(" +", "");
    assertEquals(expectedSchemaText, schema.getSchemaText().orElseThrow(() -> new AssertionError("Schema Text is empty")));
}

### 82.Correct
link: https://github.com/apache/flink/commit/a886339dbb36b11bc8bb96d35882223583ac3763
p_path: flink-runtime/src/main/java/org/apache/flink/runtime/io/network/partition/hybrid/tiered/tier/memory/MemoryTierProducerAgent.java#tryWrite
t_path: flink-runtime/src/test/java/org/apache/flink/runtime/io/network/partition/hybrid/tiered/tier/memory/MemoryTierProducerAgentTest.java#testTryWrite

```java:test_src

@Test
void testTryWrite() {
    try (MemoryTierProducerAgent memoryTierProducerAgent = createMemoryTierProducerAgent(false, BUFFER_SIZE, new TieredStorageResourceRegistry())) {
        memoryTierProducerAgent.connectionEstablished(SUBPARTITION_ID, new TestingNettyConnectionWriter.Builder().build());
        assertThat(memoryTierProducerAgent.tryWrite(SUBPARTITION_ID, BufferBuilderTestUtils.buildSomeBuffer(), this)).isTrue();
        assertThat(memoryTierProducerAgent.tryWrite(SUBPARTITION_ID, BufferBuilderTestUtils.buildSomeBuffer(), this)).isFalse();
    }
}

```java:test_tgt

@Test
void testTryWrite() {
    try (MemoryTierProducerAgent memoryTierProducerAgent = createMemoryTierProducerAgent(false, BUFFER_SIZE, new TieredStorageResourceRegistry())) {
        memoryTierProducerAgent.connectionEstablished(SUBPARTITION_ID, new TestingNettyConnectionWriter.Builder().build());
        assertThat(memoryTierProducerAgent.tryWrite(SUBPARTITION_ID, BufferBuilderTestUtils.buildSomeBuffer(), this, 0)).isTrue();
        assertThat(memoryTierProducerAgent.tryWrite(SUBPARTITION_ID, BufferBuilderTestUtils.buildSomeBuffer(), this, 0)).isFalse();
    }
}

```java:llm_gen

@Test
void testTryWrite() {
    try (MemoryTierProducerAgent memoryTierProducerAgent = createMemoryTierProducerAgent(false, BUFFER_SIZE, new TieredStorageResourceRegistry())) {
        memoryTierProducerAgent.connectionEstablished(SUBPARTITION_ID, new TestingNettyConnectionWriter.Builder().build());
        assertThat(memoryTierProducerAgent.tryWrite(SUBPARTITION_ID, BufferBuilderTestUtils.buildSomeBuffer(), this, 0)).isTrue();
        assertThat(memoryTierProducerAgent.tryWrite(SUBPARTITION_ID, BufferBuilderTestUtils.buildSomeBuffer(), this, 0)).isFalse();
    }
}

### 83.Test Preparation Error
link: https://github.com/rsksmart/rskj/commit/fd13e7b59911e45d6040581f2fcc579927194369
p_path: rskj-core/src/main/java/co/rsk/peg/federation/PendingFederation.java#buildFederation
t_path: rskj-core/src/test/java/co/rsk/peg/federation/PendingFederationTest.java#testBuildFederation

```java:test_src

private void testBuildFederation(boolean isRskip201Active, boolean isRskip284Active, boolean isRskip353Active, String networkId, int federationMembersCount) {
    ActivationConfig.ForBlock activations = mock(ActivationConfig.ForBlock.class);
    when(activations.isActive(ConsensusRule.RSKIP201)).thenReturn(isRskip201Active);
    when(activations.isActive(ConsensusRule.RSKIP284)).thenReturn(isRskip284Active);
    when(activations.isActive(ConsensusRule.RSKIP353)).thenReturn(isRskip353Active);
    BridgeConstants bridgeConstants;
    if (networkId.equals(NetworkParameters.ID_MAINNET)) {
        bridgeConstants = BridgeMainNetConstants.getInstance();
    } else {
        bridgeConstants = BridgeTestNetConstants.getInstance();
    }
    Integer[] privateKeys = new Integer[federationMembersCount];
    for (int i = 0; i < federationMembersCount; i++) {
        privateKeys[i] = new Integer((i + 1) * 100);
    }
    Instant creationTime = Instant.ofEpochMilli(1234L);
    PendingFederation otherPendingFederation = new PendingFederation(FederationTestUtils.getFederationMembersFromPks(privateKeys));
    Federation builtFederation = otherPendingFederation.buildFederation(creationTime, 0L, bridgeConstants, activations);
    Federation expectedFederation;
    if (isRskip353Active) {
        expectedFederation = FederationFactory.buildP2shErpFederation(FederationTestUtils.getFederationMembersFromPks(privateKeys), creationTime, 0L, bridgeConstants.getBtcParams(), bridgeConstants.getErpFedPubKeysList(), bridgeConstants.getErpFedActivationDelay());
    } else if (isRskip201Active) {
        expectedFederation = FederationFactory.buildNonStandardErpFederation(FederationTestUtils.getFederationMembersFromPks(privateKeys), creationTime, 0L, bridgeConstants.getBtcParams(), bridgeConstants.getErpFedPubKeysList(), bridgeConstants.getErpFedActivationDelay(), activations);
    } else {
        expectedFederation = FederationFactory.buildStandardMultiSigFederation(FederationTestUtils.getFederationMembersFromPks(privateKeys), creationTime, 0L, bridgeConstants.getBtcParams());
    }
    assertEquals(expectedFederation, builtFederation);
    if (isRskip201Active && !isRskip284Active && networkId.equals(NetworkParameters.ID_TESTNET)) {
        assertEquals(TestConstants.ERP_TESTNET_REDEEM_SCRIPT, builtFederation.getRedeemScript());
    }
}

```java:test_tgt

private void testBuildFederation(boolean isRskip201Active, boolean isRskip284Active, boolean isRskip353Active, String networkId, int federationMembersCount) {
    ActivationConfig.ForBlock activations = mock(ActivationConfig.ForBlock.class);
    when(activations.isActive(ConsensusRule.RSKIP201)).thenReturn(isRskip201Active);
    when(activations.isActive(ConsensusRule.RSKIP284)).thenReturn(isRskip284Active);
    when(activations.isActive(ConsensusRule.RSKIP353)).thenReturn(isRskip353Active);
    BridgeConstants bridgeConstants;
    if (networkId.equals(NetworkParameters.ID_MAINNET)) {
        bridgeConstants = BridgeMainNetConstants.getInstance();
    } else {
        bridgeConstants = BridgeTestNetConstants.getInstance();
    }
    Integer[] privateKeys = new Integer[federationMembersCount];
    for (int i = 0; i < federationMembersCount; i++) {
        privateKeys[i] = new Integer((i + 1) * 100);
    }
    Instant creationTime = Instant.ofEpochMilli(1234L);
    PendingFederation otherPendingFederation = new PendingFederation(FederationTestUtils.getFederationMembersFromPks(privateKeys));
    Federation builtFederation = otherPendingFederation.buildFederation(creationTime, 0L, bridgeConstants, activations);
    Federation expectedFederation;
    List<FederationMember> fedMembers = FederationTestUtils.getFederationMembersFromPks(privateKeys);
    NetworkParameters btcParams = bridgeConstants.getBtcParams();
    FederationArgs federationArgs = new FederationArgs(fedMembers, creationTime, 0L, btcParams);
    List<BtcECKey> erpPubKeys = bridgeConstants.getErpFedPubKeysList();
    long activationDelay = bridgeConstants.getErpFedActivationDelay();
    ErpFederationArgs erpFederationArgs = new ErpFederationArgs(fedMembers, creationTime, 0L, btcParams, erpPubKeys, activationDelay);
    if (isRskip353Active) {
        expectedFederation = FederationFactory.buildP2shErpFederation(erpFederationArgs);
    } else if (isRskip201Active) {
        expectedFederation = FederationFactory.buildNonStandardErpFederation(erpFederationArgs, activations);
    } else {
        expectedFederation = FederationFactory.buildStandardMultiSigFederation(federationArgs);
    }
    assertEquals(expectedFederation, builtFederation);
    if (isRskip201Active && !isRskip284Active && networkId.equals(NetworkParameters.ID_TESTNET)) {
        assertEquals(TestConstants.ERP_TESTNET_REDEEM_SCRIPT, builtFederation.getRedeemScript());
    }
}

```java:llm_gen

private void testBuildFederation(boolean isRskip201Active, boolean isRskip284Active, boolean isRskip353Active, String networkId, int federationMembersCount) {
    ActivationConfig.ForBlock activations = mock(ActivationConfig.ForBlock.class);
    when(activations.isActive(ConsensusRule.RSKIP201)).thenReturn(isRskip201Active);
    when(activations.isActive(ConsensusRule.RSKIP284)).thenReturn(isRskip284Active);
    when(activations.isActive(ConsensusRule.RSKIP353)).thenReturn(isRskip353Active);
    BridgeConstants bridgeConstants;
    if (networkId.equals(NetworkParameters.ID_MAINNET)) {
        bridgeConstants = BridgeMainNetConstants.getInstance();
    } else {
        bridgeConstants = BridgeTestNetConstants.getInstance();
    }
    Integer[] privateKeys = new Integer[federationMembersCount];
    for (int i = 0; i < federationMembersCount; i++) {
        privateKeys[i] = new Integer((i + 1) * 100);
    }
    Instant creationTime = Instant.ofEpochMilli(1234L);
    PendingFederation otherPendingFederation = new PendingFederation(FederationTestUtils.getFederationMembersFromPks(privateKeys));
    Federation builtFederation = otherPendingFederation.buildFederation(creationTime, 0L, bridgeConstants, activations);
    Federation expectedFederation;
    NetworkParameters btcParams = bridgeConstants.getBtcParams();
    List<BtcECKey> erpPubKeys = bridgeConstants.getErpFedPubKeysList();
    long activationDelay = bridgeConstants.getErpFedActivationDelay();
    if (shouldBuildStandardMultisigFederation(activations)) {
        FederationArgs federationArgs = new FederationArgs(FederationTestUtils.getFederationMembersFromPks(privateKeys), creationTime, 0L, btcParams);
        expectedFederation = FederationFactory.buildStandardMultiSigFederation(federationArgs);
    } else if (shouldBuildNonStandardErpFederation(activations)) {
        ErpFederationArgs erpFederationArgs = new ErpFederationArgs(FederationTestUtils.getFederationMembersFromPks(privateKeys), creationTime, 0L, btcParams, erpPubKeys, activationDelay);
        expectedFederation = FederationFactory.buildNonStandardErpFederation(erpFederationArgs, activations);
    } else {
        ErpFederationArgs erpFederationArgs = new ErpFederationArgs(FederationTestUtils.getFederationMembersFromPks(privateKeys), creationTime, 0L, btcParams, erpPubKeys, activationDelay);
        expectedFederation = FederationFactory.buildP2shErpFederation(erpFederationArgs);
    }
    assertEquals(expectedFederation, builtFederation);
    if (isRskip201Active && !isRskip284Active && networkId.equals(NetworkParameters.ID_TESTNET)) {
        assertEquals(TestConstants.ERP_TESTNET_REDEEM_SCRIPT, builtFederation.getRedeemScript());
    }
}

### 84.Assert Error
link: https://github.com/apache/kafka/commit/e164d4d4264b6d663952c6a65f2fda46a4cc9e04
p_path: group-coordinator/src/main/java/org/apache/kafka/coordinator/group/RecordHelpers.java#newCurrentAssignmentRecord
t_path: group-coordinator/src/test/java/org/apache/kafka/coordinator/group/RecordHelpersTest.java#testNewCurrentAssignmentRecord

```java:test_src

@Test
public void testNewCurrentAssignmentRecord() {
    Uuid topicId1 = Uuid.randomUuid();
    Uuid topicId2 = Uuid.randomUuid();
    Map<Uuid, Set<Integer>> assigned = mkSortedAssignment(mkSortedTopicAssignment(topicId1, 11, 12, 13), mkSortedTopicAssignment(topicId2, 21, 22, 23));
    Map<Uuid, Set<Integer>> revoking = mkSortedAssignment(mkSortedTopicAssignment(topicId1, 14, 15, 16), mkSortedTopicAssignment(topicId2, 24, 25, 26));
    Map<Uuid, Set<Integer>> assigning = mkSortedAssignment(mkSortedTopicAssignment(topicId1, 17, 18, 19), mkSortedTopicAssignment(topicId2, 27, 28, 29));
    Record expectedRecord = new Record(new ApiMessageAndVersion(new ConsumerGroupCurrentMemberAssignmentKey().setGroupId("group-id").setMemberId("member-id"), (short) 8), new ApiMessageAndVersion(new ConsumerGroupCurrentMemberAssignmentValue().setMemberEpoch(22).setPreviousMemberEpoch(21).setTargetMemberEpoch(23).setAssignedPartitions(Arrays.asList(new ConsumerGroupCurrentMemberAssignmentValue.TopicPartitions().setTopicId(topicId1).setPartitions(Arrays.asList(11, 12, 13)), new ConsumerGroupCurrentMemberAssignmentValue.TopicPartitions().setTopicId(topicId2).setPartitions(Arrays.asList(21, 22, 23)))).setPartitionsPendingRevocation(Arrays.asList(new ConsumerGroupCurrentMemberAssignmentValue.TopicPartitions().setTopicId(topicId1).setPartitions(Arrays.asList(14, 15, 16)), new ConsumerGroupCurrentMemberAssignmentValue.TopicPartitions().setTopicId(topicId2).setPartitions(Arrays.asList(24, 25, 26)))).setPartitionsPendingAssignment(Arrays.asList(new ConsumerGroupCurrentMemberAssignmentValue.TopicPartitions().setTopicId(topicId1).setPartitions(Arrays.asList(17, 18, 19)), new ConsumerGroupCurrentMemberAssignmentValue.TopicPartitions().setTopicId(topicId2).setPartitions(Arrays.asList(27, 28, 29)))), (short) 0));
    assertEquals(expectedRecord, newCurrentAssignmentRecord("group-id", new ConsumerGroupMember.Builder("member-id").setMemberEpoch(22).setPreviousMemberEpoch(21).setTargetMemberEpoch(23).setAssignedPartitions(assigned).setPartitionsPendingRevocation(revoking).setPartitionsPendingAssignment(assigning).build()));
}

```java:test_tgt

@Test
public void testNewCurrentAssignmentRecord() {
    Uuid topicId1 = Uuid.randomUuid();
    Uuid topicId2 = Uuid.randomUuid();
    Map<Uuid, Set<Integer>> assigned = mkSortedAssignment(mkSortedTopicAssignment(topicId1, 11, 12, 13), mkSortedTopicAssignment(topicId2, 21, 22, 23));
    Map<Uuid, Set<Integer>> revoking = mkSortedAssignment(mkSortedTopicAssignment(topicId1, 14, 15, 16), mkSortedTopicAssignment(topicId2, 24, 25, 26));
    Record expectedRecord = new Record(new ApiMessageAndVersion(new ConsumerGroupCurrentMemberAssignmentKey().setGroupId("group-id").setMemberId("member-id"), (short) 8), new ApiMessageAndVersion(new ConsumerGroupCurrentMemberAssignmentValue().setState(MemberState.UNREVOKED_PARTITIONS.value()).setMemberEpoch(22).setPreviousMemberEpoch(21).setAssignedPartitions(Arrays.asList(new ConsumerGroupCurrentMemberAssignmentValue.TopicPartitions().setTopicId(topicId1).setPartitions(Arrays.asList(11, 12, 13)), new ConsumerGroupCurrentMemberAssignmentValue.TopicPartitions().setTopicId(topicId2).setPartitions(Arrays.asList(21, 22, 23)))).setPartitionsPendingRevocation(Arrays.asList(new ConsumerGroupCurrentMemberAssignmentValue.TopicPartitions().setTopicId(topicId1).setPartitions(Arrays.asList(14, 15, 16)), new ConsumerGroupCurrentMemberAssignmentValue.TopicPartitions().setTopicId(topicId2).setPartitions(Arrays.asList(24, 25, 26)))), (short) 0));
    assertEquals(expectedRecord, newCurrentAssignmentRecord("group-id", new ConsumerGroupMember.Builder("member-id").setState(MemberState.UNREVOKED_PARTITIONS).setMemberEpoch(22).setPreviousMemberEpoch(21).setAssignedPartitions(assigned).setPartitionsPendingRevocation(revoking).build()));
}

```java:llm_gen

@Test
public void testNewCurrentAssignmentRecord() {
    Uuid topicId1 = Uuid.randomUuid();
    Uuid topicId2 = Uuid.randomUuid();
    Map<Uuid, Set<Integer>> assigned = mkSortedAssignment(mkSortedTopicAssignment(topicId1, 11, 12, 13), mkSortedTopicAssignment(topicId2, 21, 22, 23));
    Map<Uuid, Set<Integer>> revoking = mkSortedAssignment(mkSortedTopicAssignment(topicId1, 14, 15, 16), mkSortedTopicAssignment(topicId2, 24, 25, 26));
    Record expectedRecord = new Record(new ApiMessageAndVersion(new ConsumerGroupCurrentMemberAssignmentKey().setGroupId("group-id").setMemberId("member-id"), (short) 8), new ApiMessageAndVersion(new ConsumerGroupCurrentMemberAssignmentValue().setMemberEpoch(22).setPreviousMemberEpoch(21).setState(0).setAssignedPartitions(Arrays.asList(new ConsumerGroupCurrentMemberAssignmentValue.TopicPartitions().setTopicId(topicId1).setPartitions(Arrays.asList(11, 12, 13)), new ConsumerGroupCurrentMemberAssignmentValue.TopicPartitions().setTopicId(topicId2).setPartitions(Arrays.asList(21, 22, 23)))).setPartitionsPendingRevocation(Arrays.asList(new ConsumerGroupCurrentMemberAssignmentValue.TopicPartitions().setTopicId(topicId1).setPartitions(Arrays.asList(14, 15, 16)), new ConsumerGroupCurrentMemberAssignmentValue.TopicPartitions().setTopicId(topicId2).setPartitions(Arrays.asList(24, 25, 26)))), (short) 0));
    assertEquals(expectedRecord, newCurrentAssignmentRecord("group-id", new ConsumerGroupMember.Builder("member-id").setMemberEpoch(22).setPreviousMemberEpoch(21).setState(ConsumerGroupMember.MemberState.STABLE.value()).setAssignedPartitions(assigned).setPartitionsPendingRevocation(revoking).build()));
}

### 85.Correct
link: https://github.com/HTTP-RPC/Kilo/commit/5d4daed54ec30876a3a7a6571e165afd57ba8f64
p_path: kilo-client/src/main/java/org/httprpc/kilo/sql/QueryBuilder.java#delete
t_path: kilo-client/src/test/java/org/httprpc/kilo/sql/QueryBuilderTest.java#testDelete

```java:test_src

@Test
public void testDelete() {
    var queryBuilder = QueryBuilder.delete(A.class).filterByPrimaryKey("a");
    assertEquals("delete from A\nwhere A.a = ?\n", queryBuilder.toString());
    assertEquals(listOf("a"), queryBuilder.getParameters());
}

```java:test_tgt

@Test
public void testDelete() {
    var queryBuilder = QueryBuilder.delete(A.class).filterByPrimaryKey("a");
    assertEquals("delete from A where A.a = ?", queryBuilder.toString());
    assertEquals(listOf("a"), queryBuilder.getParameters());
}

```java:llm_gen

@Test
public void testDelete() {
    var queryBuilder = QueryBuilder.delete(A.class).filterByPrimaryKey("a");
    assertEquals("delete from A where A.a = ?", queryBuilder.toString());
    assertEquals(listOf("a"), queryBuilder.getParameters());
}

### 86.Correct
link: https://github.com/google/tink/commit/b0c03e2304a0a0cc20f6ba8de4a6b85f8d1683be
p_path: java_src/src/main/java/com/google/crypto/tink/aead/AeadKeyTemplates.java#createAesGcmKeyTemplate
t_path: java_src/src/test/java/com/google/crypto/tink/aead/AeadKeyTemplatesTest.java#testCreateAesGcmKeyTemplate

```java:test_src

@Test
public void testCreateAesGcmKeyTemplate() throws Exception {
    int keySize = 42;
    KeyTemplate template = AeadKeyTemplates.createAesGcmKeyTemplate(keySize);
    assertEquals(new AesGcmKeyManager().getKeyType(), template.getTypeUrl());
    assertEquals(OutputPrefixType.TINK, template.getOutputPrefixType());
    AesGcmKeyFormat format = AesGcmKeyFormat.parseFrom(template.getValue(), ExtensionRegistryLite.getEmptyRegistry());
    assertEquals(keySize, format.getKeySize());
}

```java:test_tgt

@Test
public void testCreateAesGcmKeyTemplate() throws Exception {
    int keySize = 42;
    KeyTemplate template = AeadKeyTemplates.createAesGcmKeyTemplate(keySize);
    assertEquals(AesGcmKeyManager.getKeyType(), template.getTypeUrl());
    assertEquals(OutputPrefixType.TINK, template.getOutputPrefixType());
    AesGcmKeyFormat format = AesGcmKeyFormat.parseFrom(template.getValue(), ExtensionRegistryLite.getEmptyRegistry());
    assertEquals(keySize, format.getKeySize());
}

```java:llm_gen

@Test
public void testCreateAesGcmKeyTemplate() throws Exception {
    int keySize = 42;
    KeyTemplate template = AeadKeyTemplates.createAesGcmKeyTemplate(keySize);
    assertEquals(AesGcmKeyManager.getKeyType(), template.getTypeUrl());
    assertEquals(OutputPrefixType.TINK, template.getOutputPrefixType());
    AesGcmKeyFormat format = AesGcmKeyFormat.parseFrom(template.getValue(), ExtensionRegistryLite.getEmptyRegistry());
    assertEquals(keySize, format.getKeySize());
}

### 87.Field/Package Information Modification
link: https://github.com/confluentinc/ksql/commit/08eb59f516a8a19c348516fa8f7a995c1d1820ea
p_path: ksqldb-engine/src/main/java/io/confluent/ksql/services/DefaultConnectClient.java#topics
t_path: ksqldb-engine/src/test/java/io/confluent/ksql/services/DefaultConnectClientTest.java#testTopics

```java:test_src

@Test
public void testTopics() throws JsonProcessingException {
    WireMock.stubFor(WireMock.get(WireMock.urlEqualTo("/connectors/foo/topics")).withHeader(AUTHORIZATION.toString(), new EqualToPattern(AUTH_HEADER)).willReturn(WireMock.aResponse().withStatus(HttpStatus.SC_OK).withBody(MAPPER.writeValueAsString(SAMPLE_TOPICS))));
    final ConnectResponse<Map<String, Map<String, List<String>>>> response = client.topics("foo");
    final Map<String, Map<String, List<String>>> activeTopics = response.datum().orElseThrow(AssertionError::new);
    assertThat(activeTopics.keySet(), is(ImmutableSet.of("foo")));
    assertThat(activeTopics.get("foo").get("topics"), is(ImmutableList.of("topicA", "topicB")));
    assertThat("Expected no error!", !response.error().isPresent());
}

```java:test_tgt

@Test
public void testTopics() throws JsonProcessingException {
    WireMock.stubFor(WireMock.get(WireMock.urlEqualTo(pathPrefix + "/connectors/foo/topics")).withHeader(AUTHORIZATION.toString(), new EqualToPattern(AUTH_HEADER)).withHeader(CUSTOM_HEADER_NAME, new EqualToPattern(CUSTOM_HEADER_VALUE)).willReturn(WireMock.aResponse().withStatus(HttpStatus.SC_OK).withBody(MAPPER.writeValueAsString(SAMPLE_TOPICS))));
    final ConnectResponse<Map<String, Map<String, List<String>>>> response = client.topics("foo");
    final Map<String, Map<String, List<String>>> activeTopics = response.datum().orElseThrow(AssertionError::new);
    assertThat(activeTopics.keySet(), is(ImmutableSet.of("foo")));
    assertThat(activeTopics.get("foo").get("topics"), is(ImmutableList.of("topicA", "topicB")));
    assertThat("Expected no error!", !response.error().isPresent());
}

```java:llm_gen

@Test
public void testTopics() throws JsonProcessingException {
    WireMock.stubFor(WireMock.get(WireMock.urlEqualTo("/connectors/foo/topics"))
            .withHeader(AUTHORIZATION.toString(), new EqualToPattern(AUTH_HEADER))
            .willReturn(WireMock.aResponse()
                    .withStatus(HttpStatus.SC_OK)
                    .withBody(MAPPER.writeValueAsString(SAMPLE_TOPICS)));
    final ConnectResponse<Map<String, Map<String, List<String>>>> response = client.topics("foo");
    final Map<String, Map<String, List<String>>> activeTopics = response.datum().orElseThrow(AssertionError::new);
    assertThat(activeTopics.keySet(), is(ImmutableSet.of("foo")));
    assertThat(activeTopics.get("foo").get("topics"), is(ImmutableList.of("topicA", "topicB")));
    assertThat("Expected no error!", !response.error().isPresent());
}

### 88.Correct
link: https://github.com/BentoBoxWorld/BentoBox/commit/ec60991aeb922bd7bca7b1c946b483ca5654529a
p_path: src/main/java/world/bentobox/bentobox/panels/customizable/IslandCreationPanel.java#openPanel
t_path: src/test/java/world/bentobox/bentobox/panels/customizable/IslandCreationPanelTest.java#testOpenPanel

```java:test_src

@Test
public void testOpenPanel() {
    IslandCreationPanel.openPanel(ic, user, "");
    verify(inv).setItem(eq(0), any());
    verify(inv).setItem(eq(1), any());
    verify(meta).setDisplayName(eq("test"));
    verify(meta).setLocalizedName(eq("test"));
    verify(meta).setLore(eq(List.of("A description", "", "panels.tips.click-to-choose")));
}

```java:test_tgt

@Test
public void testOpenPanel() {
    IslandCreationPanel.openPanel(ic, user, "", false);
    verify(inv).setItem(eq(0), any());
    verify(inv).setItem(eq(1), any());
    verify(meta).setDisplayName(eq("test"));
    verify(meta).setLocalizedName(eq("test"));
    verify(meta).setLore(eq(List.of("A description", "", "panels.tips.click-to-choose")));
}

```java:llm_gen

@Test
public void testOpenPanel() {
    IslandCreationPanel.openPanel(ic, user, "", false);
    verify(inv).setItem(eq(0), any());
    verify(inv).setItem(eq(1), any());
    verify(meta).setDisplayName(eq("test"));
    verify(meta).setLocalizedName(eq("test"));
    verify(meta).setLore(eq(List.of("A description", "", "panels.tips.click-to-choose")));
}

### 89.Wrong Update Direction
link: https://github.com/StarRocks/starrocks/commit/6e9cdcd1dafc0332601527cb2ebf4e5ad1c65684
p_path: fe/fe-core/src/main/java/com/starrocks/connector/hive/HiveMetastoreApiConverter.java#toFullSchemasForHudiTable
t_path: fe/fe-core/src/test/java/com/starrocks/connector/HiveMetastoreApiConverterTest.java#testToFullSchemasForHudiTable

```java:test_src

@Test
public void testToFullSchemasForHudiTable() {
    List<Column> columns = HiveMetastoreApiConverter.toFullSchemasForHudiTable(hudiSchema);
    Assert.assertEquals(7, columns.size());
}

```java:test_tgt

@Test
public void testToFullSchemasForHudiTable(@Mocked Table table, @Mocked HoodieTableMetaClient metaClient) {
    List<FieldSchema> partKeys = Lists.newArrayList(new FieldSchema("col1", "bigint", ""));
    List<FieldSchema> unPartKeys = Lists.newArrayList();
    unPartKeys.add(new FieldSchema("_hoodie_commit_time", "string", ""));
    unPartKeys.add(new FieldSchema("_hoodie_commit_seqno", "string", ""));
    unPartKeys.add(new FieldSchema("_hoodie_record_key", "string", ""));
    unPartKeys.add(new FieldSchema("_hoodie_partition_path", "string", ""));
    unPartKeys.add(new FieldSchema("_hoodie_file_name", "string", ""));
    unPartKeys.add(new FieldSchema("col2", "int", ""));
    new Expectations() {
        {
            table.getSd().getCols();
            result = unPartKeys;
            table.getPartitionKeys();
            result = partKeys;
        }
    };
    List<Column> columns = HiveMetastoreApiConverter.toFullSchemasForHudiTable(table, hudiSchema);
    Assert.assertEquals(7, columns.size());
}

```java:llm_gen

@Test
public void testToFullSchemasForHudiTable() {
    List<Column> columns = HiveMetastoreApiConverter.toFullSchemasForHudiTable(table, hudiSchema);
    Assert.assertEquals(7, columns.size());
    for (Column column : columns) {
        Assert.assertNotNull(column.getComment());
    }
}

### 90.External Class Modification
link: https://github.com/linkedin/venice/commit/314c8dc4d05346476d3de42a2e12640a443f5f75
p_path: internal/venice-client-common/src/main/java/com/linkedin/venice/stats/AbstractVeniceStats.java#registerSensorAttributeGauge
t_path: internal/venice-client-common/src/test/java/com/linkedin/venice/stats/AbstractVeniceStatsTest.java#testRegisterSensorAttributeGauge

```java:test_src

@Test
public void testRegisterSensorAttributeGauge() {
    MetricsRepository metricsRepository = new MetricsRepository();
    AbstractVeniceStats stats = new AbstractVeniceStats(metricsRepository, "myMetric");
    stats.registerSensorAttributeGauge("foo", "bar", new Gauge(() -> 1.0));
    stats.registerSensorAttributeGauge("foo", "bar2", new Gauge(() -> 2.0));
    stats.registerSensorAttributeGauge("foo", "bar2", new Gauge(() -> 3.0));
    Assert.assertEquals(metricsRepository.metrics().size(), 2);
    Assert.assertEquals(metricsRepository.getMetric(".myMetric--foo.bar").value(), 1.0);
    Assert.assertEquals(metricsRepository.getMetric(".myMetric--foo.bar2").value(), 2.0);
}

```java:test_tgt

@Test
public void testRegisterSensorAttributeGauge() {
    MetricsRepository metricsRepository = new MetricsRepository();
    AbstractVeniceStats stats = new AbstractVeniceStats(metricsRepository, "myMetric");
    stats.registerSensorAttributeGauge("foo", "bar", new AsyncGauge((ignored, ignored2) -> 1.0, "foo"));
    stats.registerSensorAttributeGauge("foo", "bar2", new AsyncGauge((ignored, ignored2) -> 2.0, "foo"));
    stats.registerSensorAttributeGauge("foo", "bar2", new AsyncGauge((ignored, ignored2) -> 3.0, "foo"));
    Assert.assertEquals(metricsRepository.metrics().size(), 2);
    Assert.assertEquals(metricsRepository.getMetric(".myMetric--foo.bar").value(), 1.0);
    Assert.assertEquals(metricsRepository.getMetric(".myMetric--foo.bar2").value(), 2.0);
}

```java:llm_gen

@Test
public void testRegisterSensorAttributeGauge() {
    MetricsRepository metricsRepository = new MetricsRepository();
    AbstractVeniceStats stats = new AbstractVeniceStats(metricsRepository, "myMetric");
    stats.registerSensorAttributeGauge("foo", "bar", new AsyncGauge(() -> 1.0));
    stats.registerSensorAttributeGauge("foo", "bar2", new AsyncGauge(() -> 2.0));
    stats.registerSensorAttributeGauge("foo", "bar2", new AsyncGauge(() -> 3.0));
    Assert.assertEquals(metricsRepository.metrics().size(), 2);
    Assert.assertEquals(metricsRepository.getMetric(".myMetric--foo.bar").value(), 1.0);
    Assert.assertEquals(metricsRepository.getMetric(".myMetric--foo.bar2").value(), 2.0);
}

### 91.Correct
link: https://github.com/StarRocks/starrocks/commit/952bc956276f35b51e239eaceda8659a2eded4b1
p_path: fe/fe-core/src/main/java/com/starrocks/service/FrontendServiceImpl.java#getLoadTxnStatus
t_path: fe/fe-core/src/test/java/com/starrocks/service/FrontendServiceImplTest.java#testGetLoadTxnStatus

```java:test_src

@Test
public void testGetLoadTxnStatus() throws Exception {
    Database db = GlobalStateMgr.getCurrentState().getDb("test");
    Table table = db.getTable("site_access_day");
    UUID uuid = UUID.randomUUID();
    TUniqueId requestId = new TUniqueId(uuid.getMostSignificantBits(), uuid.getLeastSignificantBits());
    long transactionId = GlobalStateMgr.getCurrentGlobalTransactionMgr().beginTransaction(db.getId(), Lists.newArrayList(table.getId()), "1jdc689-xd232", requestId, new TxnCoordinator(TxnSourceType.BE, "1.1.1.1"), TransactionState.LoadJobSourceType.BACKEND_STREAMING, -1, 600);
    FrontendServiceImpl impl = new FrontendServiceImpl(exeEnv);
    TGetLoadTxnStatusRequest request = new TGetLoadTxnStatusRequest();
    request.setDb("non-exist-db");
    request.setTbl("non-site_access_day-tbl");
    request.setTxnId(100);
    TGetLoadTxnStatusResult result1 = impl.getLoadTxnStatus(request);
    Assert.assertEquals(TTransactionStatus.UNKNOWN, result1.getStatus());
    request.setDb("test");
    TGetLoadTxnStatusResult result2 = impl.getLoadTxnStatus(request);
    Assert.assertEquals(TTransactionStatus.UNKNOWN, result2.getStatus());
    request.setTxnId(transactionId);
    GlobalStateMgr.getCurrentState().setFrontendNodeType(FrontendNodeType.FOLLOWER);
    TGetLoadTxnStatusResult result3 = impl.getLoadTxnStatus(request);
    Assert.assertEquals(TTransactionStatus.UNKNOWN, result3.getStatus());
    GlobalStateMgr.getCurrentState().setFrontendNodeType(FrontendNodeType.LEADER);
    TGetLoadTxnStatusResult result4 = impl.getLoadTxnStatus(request);
    Assert.assertEquals(TTransactionStatus.PREPARE, result4.getStatus());
}

```java:test_tgt

@Test
public void testGetLoadTxnStatus() throws Exception {
    Database db = GlobalStateMgr.getCurrentState().getDb("test");
    Table table = db.getTable("site_access_day");
    UUID uuid = UUID.randomUUID();
    TUniqueId requestId = new TUniqueId(uuid.getMostSignificantBits(), uuid.getLeastSignificantBits());
    long transactionId = GlobalStateMgr.getCurrentState().getGlobalTransactionMgr().beginTransaction(db.getId(), Lists.newArrayList(table.getId()), "1jdc689-xd232", requestId, new TxnCoordinator(TxnSourceType.BE, "1.1.1.1"), TransactionState.LoadJobSourceType.BACKEND_STREAMING, -1, 600);
    FrontendServiceImpl impl = new FrontendServiceImpl(exeEnv);
    TGetLoadTxnStatusRequest request = new TGetLoadTxnStatusRequest();
    request.setDb("non-exist-db");
    request.setTbl("non-site_access_day-tbl");
    request.setTxnId(100);
    TGetLoadTxnStatusResult result1 = impl.getLoadTxnStatus(request);
    Assert.assertEquals(TTransactionStatus.UNKNOWN, result1.getStatus());
    request.setDb("test");
    TGetLoadTxnStatusResult result2 = impl.getLoadTxnStatus(request);
    Assert.assertEquals(TTransactionStatus.UNKNOWN, result2.getStatus());
    request.setTxnId(transactionId);
    GlobalStateMgr.getCurrentState().setFrontendNodeType(FrontendNodeType.FOLLOWER);
    TGetLoadTxnStatusResult result3 = impl.getLoadTxnStatus(request);
    Assert.assertEquals(TTransactionStatus.UNKNOWN, result3.getStatus());
    GlobalStateMgr.getCurrentState().setFrontendNodeType(FrontendNodeType.LEADER);
    TGetLoadTxnStatusResult result4 = impl.getLoadTxnStatus(request);
    Assert.assertEquals(TTransactionStatus.PREPARE, result4.getStatus());
}

```java:llm_gen

@Test
public void testGetLoadTxnStatus() throws Exception {
    Database db = GlobalStateMgr.getCurrentState().getDb("test");
    Table table = db.getTable("site_access_day");
    UUID uuid = UUID.randomUUID();
    TUniqueId requestId = new TUniqueId(uuid.getMostSignificantBits(), uuid.getLeastSignificantBits());
    long transactionId = GlobalStateMgr.getCurrentState().getGlobalTransactionMgr().beginTransaction(db.getId(), Lists.newArrayList(table.getId()), "1jdc689-xd232", requestId, new TxnCoordinator(TxnSourceType.BE, "1.1.1.1"), TransactionState.LoadJobSourceType.BACKEND_STREAMING, -1, 600);
    FrontendServiceImpl impl = new FrontendServiceImpl(exeEnv);
    TGetLoadTxnStatusRequest request = new TGetLoadTxnStatusRequest();
    request.setDb("non-exist-db");
    request.setTbl("non-site_access_day-tbl");
    request.setTxnId(100);
    TGetLoadTxnStatusResult result1 = impl.getLoadTxnStatus(request);
    Assert.assertEquals(TTransactionStatus.UNKNOWN, result1.getStatus());
    request.setDb("test");
    TGetLoadTxnStatusResult result2 = impl.getLoadTxnStatus(request);
    Assert.assertEquals(TTransactionStatus.UNKNOWN, result2.getStatus());
    request.setTxnId(transactionId);
    GlobalStateMgr.getCurrentState().setFrontendNodeType(FrontendNodeType.FOLLOWER);
    TGetLoadTxnStatusResult result3 = impl.getLoadTxnStatus(request);
    Assert.assertEquals(TTransactionStatus.UNKNOWN, result3.getStatus());
    GlobalStateMgr.getCurrentState().setFrontendNodeType(FrontendNodeType.LEADER);
    TGetLoadTxnStatusResult result4 = impl.getLoadTxnStatus(request);
    Assert.assertEquals(TTransactionStatus.PREPARE, result4.getStatus());
}

### 92.Partial Updates
link: https://github.com/apache/hudi/commit/8a0ce61b2fd187243e89254cdef528b3b1cb49e8
p_path: hudi-client/hudi-client-common/src/main/java/org/apache/hudi/table/action/rollback/RollbackUtils.java#mergeRollbackStat
t_path: hudi-client/hudi-spark-client/src/test/java/org/apache/hudi/table/action/rollback/TestRollbackUtils.java#testMergeRollbackStat

```java:test_src

@Test
public void testMergeRollbackStat() {
    String partitionPath1 = "/partitionPath1/";
    String partitionPath2 = "/partitionPath2/";
    Map<FileStatus, Boolean> dataFilesOnlyStat1Files = new HashMap<>();
    dataFilesOnlyStat1Files.put(generateFileStatus(partitionPath1 + "dataFile1" + BASE_FILE_EXTENSION), true);
    dataFilesOnlyStat1Files.put(generateFileStatus(partitionPath1 + "dataFile2" + BASE_FILE_EXTENSION), true);
    HoodieRollbackStat dataFilesOnlyStat1 = HoodieRollbackStat.newBuilder().withPartitionPath(partitionPath1).withDeletedFileResults(dataFilesOnlyStat1Files).build();
    Map<FileStatus, Boolean> dataFilesOnlyStat2Files = new HashMap<>();
    dataFilesOnlyStat2Files.put(generateFileStatus(partitionPath2 + "dataFile1" + BASE_FILE_EXTENSION), true);
    dataFilesOnlyStat2Files.put(generateFileStatus(partitionPath2 + "dataFile2" + BASE_FILE_EXTENSION), true);
    HoodieRollbackStat dataFilesOnlyStat2 = HoodieRollbackStat.newBuilder().withPartitionPath(partitionPath2).withDeletedFileResults(dataFilesOnlyStat1Files).build();
    assertThrows(IllegalArgumentException.class, () -> {
        RollbackUtils.mergeRollbackStat(dataFilesOnlyStat1, dataFilesOnlyStat2);
    }, "different partition rollbackstat merge will failed");
    Map<FileStatus, Boolean> dataFilesOnlyStat3Files = new HashMap<>();
    dataFilesOnlyStat3Files.put(generateFileStatus(partitionPath1 + "dataFile1.log"), true);
    dataFilesOnlyStat3Files.put(generateFileStatus(partitionPath1 + "dataFile3" + BASE_FILE_EXTENSION), false);
    HoodieRollbackStat dataFilesOnlyStat3 = HoodieRollbackStat.newBuilder().withPartitionPath(partitionPath1).withDeletedFileResults(dataFilesOnlyStat3Files).build();
    Map<FileStatus, Long> dataFilesOnlyStat4Files = new HashMap<>();
    dataFilesOnlyStat4Files.put(generateFileStatus(partitionPath1 + "dataFile1.log"), 10L);
    HoodieRollbackStat dataFilesOnlyStat4 = HoodieRollbackStat.newBuilder().withPartitionPath(partitionPath1).withRollbackBlockAppendResults(dataFilesOnlyStat4Files).build();
    HoodieRollbackStat dataFilesOnlyStatMerge1 = RollbackUtils.mergeRollbackStat(dataFilesOnlyStat1, dataFilesOnlyStat3);
    assertEquals(partitionPath1, dataFilesOnlyStatMerge1.getPartitionPath());
    assertIterableEquals(CollectionUtils.createImmutableList(partitionPath1 + "dataFile3" + BASE_FILE_EXTENSION), dataFilesOnlyStatMerge1.getFailedDeleteFiles());
    assertIterableEquals(CollectionUtils.createImmutableList(partitionPath1 + "dataFile1" + BASE_FILE_EXTENSION, partitionPath1 + "dataFile2" + BASE_FILE_EXTENSION, partitionPath1 + "dataFile1.log").stream().sorted().collect(Collectors.toList()), dataFilesOnlyStatMerge1.getSuccessDeleteFiles().stream().sorted().collect(Collectors.toList()));
    assertEquals(0, dataFilesOnlyStatMerge1.getCommandBlocksCount().size());
    HoodieRollbackStat dataFilesOnlyStatMerge2 = RollbackUtils.mergeRollbackStat(dataFilesOnlyStatMerge1, dataFilesOnlyStat4);
    assertEquals(partitionPath1, dataFilesOnlyStatMerge1.getPartitionPath());
    assertIterableEquals(CollectionUtils.createImmutableList(partitionPath1 + "dataFile3" + BASE_FILE_EXTENSION).stream().sorted().collect(Collectors.toList()), dataFilesOnlyStatMerge2.getFailedDeleteFiles().stream().sorted().collect(Collectors.toList()));
    assertIterableEquals(CollectionUtils.createImmutableList(partitionPath1 + "dataFile1" + BASE_FILE_EXTENSION, partitionPath1 + "dataFile2" + BASE_FILE_EXTENSION, partitionPath1 + "dataFile1.log").stream().sorted().collect(Collectors.toList()), dataFilesOnlyStatMerge2.getSuccessDeleteFiles().stream().sorted().collect(Collectors.toList()));
    assertEquals(Collections.singletonMap(generateFileStatus(partitionPath1 + "dataFile1.log"), 10L), dataFilesOnlyStatMerge2.getCommandBlocksCount());
}

```java:test_tgt

@Test
public void testMergeRollbackStat() {
    String partitionPath1 = "/partitionPath1/";
    String partitionPath2 = "/partitionPath2/";
    Map<StoragePathInfo, Boolean> dataFilesOnlyStat1Files = new HashMap<>();
    dataFilesOnlyStat1Files.put(generateFileStatus(partitionPath1 + "dataFile1" + BASE_FILE_EXTENSION), true);
    dataFilesOnlyStat1Files.put(generateFileStatus(partitionPath1 + "dataFile2" + BASE_FILE_EXTENSION), true);
    HoodieRollbackStat dataFilesOnlyStat1 = HoodieRollbackStat.newBuilder().withPartitionPath(partitionPath1).withDeletedFileResults(dataFilesOnlyStat1Files).build();
    Map<StoragePathInfo, Boolean> dataFilesOnlyStat2Files = new HashMap<>();
    dataFilesOnlyStat2Files.put(generateFileStatus(partitionPath2 + "dataFile1" + BASE_FILE_EXTENSION), true);
    dataFilesOnlyStat2Files.put(generateFileStatus(partitionPath2 + "dataFile2" + BASE_FILE_EXTENSION), true);
    HoodieRollbackStat dataFilesOnlyStat2 = HoodieRollbackStat.newBuilder().withPartitionPath(partitionPath2).withDeletedFileResults(dataFilesOnlyStat1Files).build();
    assertThrows(IllegalArgumentException.class, () -> {
        RollbackUtils.mergeRollbackStat(dataFilesOnlyStat1, dataFilesOnlyStat2);
    }, "different partition rollbackstat merge will failed");
    Map<StoragePathInfo, Boolean> dataFilesOnlyStat3Files = new HashMap<>();
    dataFilesOnlyStat3Files.put(generateFileStatus(partitionPath1 + "dataFile1.log"), true);
    dataFilesOnlyStat3Files.put(generateFileStatus(partitionPath1 + "dataFile3" + BASE_FILE_EXTENSION), false);
    HoodieRollbackStat dataFilesOnlyStat3 = HoodieRollbackStat.newBuilder().withPartitionPath(partitionPath1).withDeletedFileResults(dataFilesOnlyStat3Files).build();
    Map<StoragePathInfo, Long> dataFilesOnlyStat4Files = new HashMap<>();
    dataFilesOnlyStat4Files.put(generateFileStatus(partitionPath1 + "dataFile1.log"), 10L);
    HoodieRollbackStat dataFilesOnlyStat4 = HoodieRollbackStat.newBuilder().withPartitionPath(partitionPath1).withRollbackBlockAppendResults(dataFilesOnlyStat4Files).build();
    HoodieRollbackStat dataFilesOnlyStatMerge1 = RollbackUtils.mergeRollbackStat(dataFilesOnlyStat1, dataFilesOnlyStat3);
    assertEquals(partitionPath1, dataFilesOnlyStatMerge1.getPartitionPath());
    assertIterableEquals(CollectionUtils.createImmutableList(partitionPath1 + "dataFile3" + BASE_FILE_EXTENSION), dataFilesOnlyStatMerge1.getFailedDeleteFiles());
    assertIterableEquals(CollectionUtils.createImmutableList(partitionPath1 + "dataFile1" + BASE_FILE_EXTENSION, partitionPath1 + "dataFile2" + BASE_FILE_EXTENSION, partitionPath1 + "dataFile1.log").stream().sorted().collect(Collectors.toList()), dataFilesOnlyStatMerge1.getSuccessDeleteFiles().stream().sorted().collect(Collectors.toList()));
    assertEquals(0, dataFilesOnlyStatMerge1.getCommandBlocksCount().size());
    HoodieRollbackStat dataFilesOnlyStatMerge2 = RollbackUtils.mergeRollbackStat(dataFilesOnlyStatMerge1, dataFilesOnlyStat4);
    assertEquals(partitionPath1, dataFilesOnlyStatMerge1.getPartitionPath());
    assertIterableEquals(CollectionUtils.createImmutableList(partitionPath1 + "dataFile3" + BASE_FILE_EXTENSION).stream().sorted().collect(Collectors.toList()), dataFilesOnlyStatMerge2.getFailedDeleteFiles().stream().sorted().collect(Collectors.toList()));
    assertIterableEquals(CollectionUtils.createImmutableList(partitionPath1 + "dataFile1" + BASE_FILE_EXTENSION, partitionPath1 + "dataFile2" + BASE_FILE_EXTENSION, partitionPath1 + "dataFile1.log").stream().sorted().collect(Collectors.toList()), dataFilesOnlyStatMerge2.getSuccessDeleteFiles().stream().sorted().collect(Collectors.toList()));
    assertEquals(Collections.singletonMap(generateFileStatus(partitionPath1 + "dataFile1.log"), 10L), dataFilesOnlyStatMerge2.getCommandBlocksCount());
}

```java:llm_gen

@Test
public void testMergeRollbackStat() {
    String partitionPath1 = "/partitionPath1/";
    String partitionPath2 = "/partitionPath2/";
    Map<FileStatus, Boolean> dataFilesOnlyStat1Files = new HashMap<>();
    dataFilesOnlyStat1Files.put(generateFileStatus(partitionPath1 + "dataFile1" + BASE_FILE_EXTENSION), true);
    dataFilesOnlyStat1Files.put(generateFileStatus(partitionPath1 + "dataFile2" + BASE_FILE_EXTENSION), true);
    HoodieRollbackStat dataFilesOnlyStat1 = HoodieRollbackStat.newBuilder().withPartitionPath(partitionPath1).withDeletedFileResults(dataFilesOnlyStat1Files).build();
    Map<FileStatus, Boolean> dataFilesOnlyStat2Files = new HashMap<>();
    dataFilesOnlyStat2Files.put(generateFileStatus(partitionPath2 + "dataFile1" + BASE_FILE_EXTENSION), true);
    dataFilesOnlyStat2Files.put(generateFileStatus(partitionPath2 + "dataFile2" + BASE_FILE_EXTENSION), true);
    HoodieRollbackStat dataFilesOnlyStat2 = HoodieRollbackStat.newBuilder().withPartitionPath(partitionPath2).withDeletedFileResults(dataFilesOnlyStat1Files).build();
    assertThrows(IllegalArgumentException.class, () -> {
        RollbackUtils.mergeRollbackStat(dataFilesOnlyStat1, dataFilesOnlyStat2);
    }, "different partition rollbackstat merge will failed");
    Map<FileStatus, Boolean> dataFilesOnlyStat3Files = new HashMap<>();
    dataFilesOnlyStat3Files.put(generateFileStatus(partitionPath1 + "dataFile1.log"), true);
    dataFilesOnlyStat3Files.put(generateFileStatus(partitionPath1 + "dataFile3" + BASE_FILE_EXTENSION), false);
    HoodieRollbackStat dataFilesOnlyStat3 = HoodieRollbackStat.newBuilder().withPartitionPath(partitionPath1).withDeletedFileResults(dataFilesOnlyStat3Files).build();
    Map<StoragePathInfo, Long> dataFilesOnlyStat4Files = new HashMap<>();
    dataFilesOnlyStat4Files.put(generateStoragePathInfo(partitionPath1 + "dataFile1.log"), 10L);
    HoodieRollbackStat dataFilesOnlyStat4 = HoodieRollbackStat.newBuilder().withPartitionPath(partitionPath1).withRollbackBlockAppendResults(dataFilesOnlyStat4Files).build();
    HoodieRollbackStat dataFilesOnlyStatMerge1 = RollbackUtils.mergeRollbackStat(dataFilesOnlyStat1, dataFilesOnlyStat3);
    assertEquals(partitionPath1, dataFilesOnlyStatMerge1.getPartitionPath());
    assertIterableEquals(CollectionUtils.createImmutableList(partitionPath1 + "dataFile3" + BASE_FILE_EXTENSION), dataFilesOnlyStatMerge1.getFailedDeleteFiles());
    assertIterableEquals(CollectionUtils.createImmutableList(partitionPath1 + "dataFile1" + BASE_FILE_EXTENSION, partitionPath1 + "dataFile2" + BASE_FILE_EXTENSION, partitionPath1 + "dataFile1.log").stream().sorted().collect(Collectors.toList()), dataFilesOnlyStatMerge1.getSuccessDeleteFiles().stream().sorted().collect(Collectors.toList()));
    assertEquals(0, dataFilesOnlyStatMerge1.getCommandBlocksCount().size());
    HoodieRollbackStat dataFilesOnlyStatMerge2 = RollbackUtils.mergeRollbackStat(dataFilesOnlyStatMerge1, dataFilesOnlyStat4);
    assertEquals(partitionPath1, dataFilesOnlyStatMerge1.getPartitionPath());
    assertIterableEquals(CollectionUtils.createImmutableList(partitionPath1 + "dataFile3" + BASE_FILE_EXTENSION).stream().sorted().collect(Collectors.toList()), dataFilesOnlyStatMerge2.getFailedDeleteFiles().stream().sorted().collect(Collectors.toList()));
    assertIterableEquals(CollectionUtils.createImmutableList(partitionPath1 + "dataFile1" + BASE_FILE_EXTENSION, partitionPath1 + "dataFile2" + BASE_FILE_EXTENSION, partitionPath1 + "dataFile1.log").stream().sorted().collect(Collectors.toList()), dataFilesOnlyStatMerge2.getSuccessDeleteFiles().stream().sorted().collect(Collectors.toList()));
    assertEquals(Collections.singletonMap(generateStoragePathInfo(partitionPath1 + "dataFile1.log"), 10L), dataFilesOnlyStatMerge2.getCommandBlocksCount());
}

### 93.Missing Asserts
link: https://github.com/BentoBoxWorld/BentoBox/commit/b1fe76c45d693b6bbd3f4d87e013041fcb341934
p_path: src/main/java/world/bentobox/bentobox/managers/PlayersManager.java#isKnown
t_path: src/test/java/world/bentobox/bentobox/managers/PlayersManagerTest.java#testIsKnown

```java:test_src

@Test
public void testIsKnown() {
    pm.addPlayer(uuid);
    pm.addPlayer(notUUID);
    assertFalse(pm.isKnown(null));
    assertTrue(pm.isKnown(uuid));
    assertTrue(pm.isKnown(notUUID));
}

```java:test_tgt

@Test
public void testIsKnown() {
    pm.getPlayer(uuid);
    pm.getPlayer(notUUID);
    assertFalse(pm.isKnown(null));
    assertTrue(pm.isKnown(uuid));
    assertTrue(pm.isKnown(notUUID));
}

```java:llm_gen

@Test
public void testIsKnown() {
    pm.addPlayer(uuid);
    assertFalse(pm.isKnown(null));
    assertTrue(pm.isKnown(uuid));
}

### 94.External File Modification
link: https://github.com/langchain4j/langchain4j/commit/7d32c1491998b20e2410d6c7334d999583fdc9ca
p_path: langchain4j-core/src/main/java/dev/langchain4j/data/image/Image.java#toString
t_path: langchain4j-core/src/test/java/dev/langchain4j/data/image/ImageTest.java#test_toString

```java:test_src

@Test
public void test_toString() {
    Image image = Image.builder().url(URI.create("https://example.com/image.png")).base64Data("base64Data").revisedPrompt("revisedPrompt").build();
    assertThat(image).hasToString("Image{ url=\"https://example.com/image.png\", base64Data=\"base64Data\", revisedPrompt=\"revisedPrompt\"}");
}

```java:test_tgt

@Test
public void test_toString() {
    Image image = Image.builder().url(URI.create("https://example.com/image.png")).base64Data("base64Data").mimeType("image/png").revisedPrompt("revisedPrompt").build();
    assertThat(image).hasToString("Image { url = \"https://example.com/image.png\", base64Data = \"base64Data\", mimeType = \"image/png\", revisedPrompt = \"revisedPrompt\" }");
}

```java:llm_gen

@Test
public void test_toString() {
    Image image = Image.builder().url(URI.create("https://example.com/image.png")).base64Data("base64Data").mimeType("mimeType").revisedPrompt("revisedPrompt").build();
    assertThat(image).hasToString("Image { url = \"https://example.com/image.png\", base64Data = \"base64Data\", mimeType = \"mimeType\", revisedPrompt = \"revisedPrompt\" }");
}

### 95.Field/Package Information Modification
link: https://github.com/GoogleCloudPlatform/java-docs-samples/commit/c54658b27240c10ce74d279cd44198bec6aa8474
p_path: aiplatform/src/main/java/aiplatform/PredictTextEmbeddingsSample.java#predictTextEmbeddings
t_path: aiplatform/src/test/java/aiplatform/PredictTextEmbeddingsSampleTest.java#testPredictTextEmbeddings

```java:test_src

@Test
public void testPredictTextEmbeddings() throws IOException {
    PredictTextEmbeddingsSample.predictTextEmbeddings(INSTANCE, PROJECT, LOCATION, PUBLISHER, MODEL);
    String got = bout.toString();
    assertThat(got).contains("Predict Response");
}

```java:test_tgt

@Test
public void testPredictTextEmbeddings() throws IOException {
    List<String> texts = List.of("banana bread?", "banana muffin?", "banana?", "recipe?", "muffin recipe?");
    PredictTextEmbeddingsSample.predictTextEmbeddings(APIS_ENDPOINT, PROJECT, "textembedding-gecko@003", texts, "RETRIEVAL_DOCUMENT");
    assertThat(bout.toString()).contains("Got predict response");
}

```java:llm_gen

@Test
public void testPredictTextEmbeddings() throws IOException {
    List<String> texts = List.of("test text");
    PredictTextEmbeddingsSample.predictTextEmbeddings(ENDPOINT, PROJECT, MODEL, texts, "TASK");
    String got = bout.toString();
    assertThat(got).contains("Got predict response:");
}

### 96.Assert Error
link: https://github.com/StarRocks/starrocks/commit/34aaff5df924f672782017d26e2683762289ec61
p_path: fe/fe-core/src/main/java/com/starrocks/connector/iceberg/IcebergApiConverter.java#toIcebergApiSchema
t_path: fe/fe-core/src/test/java/com/starrocks/connector/iceberg/IcebergApiConverterTest.java#testToIcebergApiSchema

```java:test_src

@Test
public void testToIcebergApiSchema() {
    List<Column> columns = Lists.newArrayList();
    columns.add(new Column("c1", Type.BOOLEAN));
    columns.add(new Column("c2", Type.INT));
    columns.add(new Column("c3", Type.BIGINT));
    columns.add(new Column("c4", Type.FLOAT));
    columns.add(new Column("c5", Type.DOUBLE));
    columns.add(new Column("c6", Type.DATE));
    columns.add(new Column("c7", Type.DATETIME));
    columns.add(new Column("c8", Type.VARCHAR));
    columns.add(new Column("c9", Type.CHAR));
    columns.add(new Column("c10", Type.DECIMAL32));
    columns.add(new Column("c11", Type.DECIMAL64));
    columns.add(new Column("c12", Type.DECIMAL128));
    columns.add(new Column("c13", new ArrayType(Type.INT)));
    columns.add(new Column("c14", new MapType(Type.INT, Type.INT)));
    columns.add(new Column("c15", new StructType(ImmutableList.of(Type.INT))));
    columns.add(new Column("c16", Type.TIME));
    Schema schema = IcebergApiConverter.toIcebergApiSchema(columns);
    Assert.assertEquals("table {\n" + "  1: c1: required boolean ()\n" + "  2: c2: required int ()\n" + "  3: c3: required long ()\n" + "  4: c4: required float ()\n" + "  5: c5: required double ()\n" + "  6: c6: required date ()\n" + "  7: c7: required timestamp ()\n" + "  8: c8: required string ()\n" + "  9: c9: required string ()\n" + "  10: c10: required decimal(-1, -1) ()\n" + "  11: c11: required decimal(-1, -1) ()\n" + "  12: c12: required decimal(-1, -1) ()\n" + "  13: c13: required list<int> ()\n" + "  14: c14: required map<int, int> ()\n" + "  15: c15: required struct<20: col1: optional int> ()\n" + "  16: c16: required time ()\n" + "}", schema.toString());
    PartitionSpec spec = IcebergApiConverter.parsePartitionFields(schema, Lists.newArrayList("c1"));
    Assert.assertTrue(spec.isPartitioned());
    Assert.assertEquals(1, spec.fields().size());
}

```java:test_tgt

@Test
public void testToIcebergApiSchema() {
    List<Column> columns = Lists.newArrayList();
    columns.add(new Column("c1", Type.BOOLEAN));
    columns.add(new Column("c2", Type.INT));
    columns.add(new Column("c3", Type.BIGINT));
    columns.add(new Column("c4", Type.FLOAT));
    columns.add(new Column("c5", Type.DOUBLE));
    columns.add(new Column("c6", Type.DATE));
    columns.add(new Column("c7", Type.DATETIME));
    columns.add(new Column("c8", Type.VARCHAR));
    columns.add(new Column("c9", Type.CHAR));
    columns.add(new Column("c10", Type.DECIMAL32));
    columns.add(new Column("c11", Type.DECIMAL64));
    columns.add(new Column("c12", Type.DECIMAL128));
    columns.add(new Column("c13", new ArrayType(Type.INT)));
    columns.add(new Column("c14", new MapType(Type.INT, Type.INT)));
    columns.add(new Column("c15", new StructType(ImmutableList.of(Type.INT))));
    columns.add(new Column("c16", Type.TIME));
    Schema schema = IcebergApiConverter.toIcebergApiSchema(columns);
    Assert.assertEquals("table {\n" + "  1: c1: required boolean\n" + "  2: c2: required int\n" + "  3: c3: required long\n" + "  4: c4: required float\n" + "  5: c5: required double\n" + "  6: c6: required date\n" + "  7: c7: required timestamp\n" + "  8: c8: required string\n" + "  9: c9: required string\n" + "  10: c10: required decimal(-1, -1)\n" + "  11: c11: required decimal(-1, -1)\n" + "  12: c12: required decimal(-1, -1)\n" + "  13: c13: required list<int>\n" + "  14: c14: required map<int, int>\n" + "  15: c15: required struct<20: col1: optional int>\n" + "  16: c16: required time\n" + "}", schema.toString());
    PartitionSpec spec = IcebergApiConverter.parsePartitionFields(schema, Lists.newArrayList("c1"));
    Assert.assertTrue(spec.isPartitioned());
    Assert.assertEquals(1, spec.fields().size());
}

```java:llm_gen

@Test
public void testToIcebergApiSchema() {
    List<Column> columns = Lists.newArrayList();
    columns.add(new Column("c1", Type.BOOLEAN));
    columns.add(new Column("c2", Type.INT));
    columns.add(new Column("c3", Type.BIGINT));
    columns.add(new Column("c4", Type.FLOAT));
    columns.add(new Column("c5", Type.DOUBLE));
    columns.add(new Column("c6", Type.DATE));
    columns.add(new Column("c7", Type.DATETIME));
    columns.add(new Column("c8", Type.VARCHAR));
    columns.add(new Column("c9", Type.CHAR));
    columns.add(new Column("c10", Type.DECIMAL32));
    columns.add(new Column("c11", Type.DECIMAL64));
    columns.add(new Column("c12", Type.DECIMAL128));
    columns.add(new Column("c13", new ArrayType(Type.INT)));
    columns.add(new Column("c14", new MapType(Type.INT, Type.INT)));
    columns.add(new Column("c15", new StructType(ImmutableList.of(Type.INT))));
    columns.add(new Column("c16", Type.TIME));
    Schema schema = IcebergApiConverter.toIcebergApiSchema(columns);
    Assert.assertEquals("table {\n" + "  1: c1: required boolean ()\n" + "  2: c2: required int ()\n" + "  3: c3: required long ()\n" + "  4: c4: required float ()\n" + "  5: c5: required double ()\n" + "  6: c6: required date ()\n" + "  7: c7: required timestamp ()\n" + "  8: c8: required string ()\n" + "  9: c9: required string ()\n" + "  10: c10: required decimal(-1, -1) ()\n" + "  11: c11: required decimal(-1, -1) ()\n" + "  12: c12: required decimal(-1, -1) ()\n" + "  13: c13: required list<int> ()\n" + "  14: c14: required map<int, int> ()\n" + "  15: c15: required struct<20: col1: optional int> ()\n" + "  16: c16: required time ()\n" + "}", schema.toString());
    PartitionSpec spec = IcebergApiConverter.parsePartitionFields(schema, Lists.newArrayList("c1"));
    Assert.assertTrue(spec.isPartitioned());
    Assert.assertEquals(1, spec.fields().size());
}

### 97.Additional Asserts
link: https://github.com/thingsboard/thingsboard/commit/cc85e0e6243754d77d44170994ddbd3b49ef54af
p_path: application/src/main/java/org/thingsboard/server/controller/ImageController.java#updateImage
t_path: application/src/test/java/org/thingsboard/server/controller/ImageControllerTest.java#testUpdateImage

```java:test_src

@Test
public void testUpdateImage() throws Exception {
    String filename = "my_png_image.png";
    TbResourceInfo imageInfo = uploadImage(HttpMethod.POST, "/api/image", filename, "image/png", PNG_IMAGE);
    checkPngImageDescriptor(imageInfo.getDescriptor(ImageDescriptor.class));
    String newFilename = "my_jpeg_image.png";
    imageInfo = uploadImage(HttpMethod.PUT, "/api/images/tenant/" + filename, newFilename, "image/jpeg", JPEG_IMAGE);
    assertThat(imageInfo.getTitle()).isEqualTo(filename);
    assertThat(imageInfo.getResourceKey()).isEqualTo(filename);
    assertThat(imageInfo.getFileName()).isEqualTo(newFilename);
    ImageDescriptor imageDescriptor = imageInfo.getDescriptor(ImageDescriptor.class);
    checkJpegImageDescriptor(imageDescriptor);
    assertThat(downloadImage("tenant", filename)).containsExactly(JPEG_IMAGE);
    assertThat(downloadImagePreview("tenant", filename)).hasSize((int) imageDescriptor.getPreviewDescriptor().getSize());
}

```java:test_tgt

@Test
public void testUpdateImage() throws Exception {
    String filename = "my_png_image.png";
    TbResourceInfo imageInfo = uploadImage(HttpMethod.POST, "/api/image", filename, "image/png", PNG_IMAGE);
    checkPngImageDescriptor(imageInfo.getDescriptor(ImageDescriptor.class));
    String newFilename = "my_jpeg_image.png";
    TbResourceInfo newImageInfo = uploadImage(HttpMethod.PUT, "/api/images/tenant/" + filename, newFilename, "image/jpeg", JPEG_IMAGE);
    assertThat(newImageInfo.getTitle()).isEqualTo(filename);
    assertThat(newImageInfo.getResourceKey()).isEqualTo(filename);
    assertThat(newImageInfo.getFileName()).isEqualTo(newFilename);
    assertThat(newImageInfo.getPublicResourceKey()).isEqualTo(imageInfo.getPublicResourceKey());
    ImageDescriptor imageDescriptor = newImageInfo.getDescriptor(ImageDescriptor.class);
    checkJpegImageDescriptor(imageDescriptor);
    assertThat(downloadImage("tenant", filename)).containsExactly(JPEG_IMAGE);
    assertThat(downloadImagePreview("tenant", filename)).hasSize((int) imageDescriptor.getPreviewDescriptor().getSize());
}

```java:llm_gen

@Test
public void testUpdateImage() throws Exception {
    String filename = "my_png_image.png";
    TbResourceInfo imageInfo = uploadImage(HttpMethod.POST, "/api/image", filename, "image/png", PNG_IMAGE);
    checkPngImageDescriptor(imageInfo.getDescriptor(ImageDescriptor.class));
    String newFilename = "my_jpeg_image.png";
    imageInfo = uploadImage(HttpMethod.PUT, "/api/images/tenant/" + filename, newFilename, "image/jpeg", JPEG_IMAGE);
    assertThat(imageInfo.getTitle()).isEqualTo(filename);
    assertThat(imageInfo.getResourceKey()).isEqualTo(filename);
    assertThat(imageInfo.getFileName()).isEqualTo(newFilename);
    ImageDescriptor imageDescriptor = imageInfo.getDescriptor(ImageDescriptor.class);
    checkJpegImageDescriptor(imageDescriptor);
    assertThat(downloadImage("tenant", filename)).containsExactly(JPEG_IMAGE);
    assertThat(downloadImagePreview("tenant", filename)).hasSize((int) imageDescriptor.getPreviewDescriptor().getSize());

    // Test resource size validation
    MultipartFile mockFile = mock(MultipartFile.class);
    when(mockFile.getSize()).thenReturn(1000L);
    when(mockFile.getOriginalFilename()).thenReturn(newFilename);
    when(mockFile.getBytes()).thenReturn(JPEG_IMAGE);
    TbResourceInfo mockImageInfo = mock(TbResourceInfo.class);
    when(mockImageInfo.getId()).thenReturn(imageInfo.getId());
    when(mockImageInfo.getDescriptor(ImageDescriptor.class)).thenReturn(imageDescriptor);
    doNothing().when(resourceValidator).validateResourceSize(any(), any(), anyLong());

    TbResourceInfo updatedImageInfo = resourceController.updateImage("tenant", filename, mockFile);
    verify(resourceValidator).validateResourceSize(any(), eq(imageInfo.getId()), eq(1000L));
    assertThat(updatedImageInfo.getFileName()).isEqualTo(newFilename);
}

### 98.Correct
link: https://github.com/apache/kafka/commit/459eaec666c54020fc859174004806ff4ee5cef3
p_path: group-coordinator/src/main/java/org/apache/kafka/coordinator/group/GroupCoordinatorService.java#joinGroup
t_path: group-coordinator/src/test/java/org/apache/kafka/coordinator/group/GroupCoordinatorServiceTest.java#testJoinGroup

```java:test_src

@Test
public void testJoinGroup() {
    CoordinatorRuntime<GroupCoordinatorShard, Record> runtime = mockRuntime();
    GroupCoordinatorService service = new GroupCoordinatorService(new LogContext(), createConfig(), runtime, new GroupCoordinatorMetrics());
    JoinGroupRequestData request = new JoinGroupRequestData().setGroupId("foo");
    service.startup(() -> 1);
    when(runtime.scheduleWriteOperation(ArgumentMatchers.eq("classic-group-join"), ArgumentMatchers.eq(new TopicPartition("__consumer_offsets", 0)), ArgumentMatchers.eq(Duration.ofMillis(5000)), ArgumentMatchers.any())).thenReturn(CompletableFuture.completedFuture(new JoinGroupResponseData()));
    CompletableFuture<JoinGroupResponseData> responseFuture = service.joinGroup(requestContext(ApiKeys.JOIN_GROUP), request, BufferSupplier.NO_CACHING);
    assertFalse(responseFuture.isDone());
}

```java:test_tgt

@Test
public void testJoinGroup() {
    CoordinatorRuntime<GroupCoordinatorShard, Record> runtime = mockRuntime();
    GroupCoordinatorService service = new GroupCoordinatorService(new LogContext(), createConfig(), runtime, new GroupCoordinatorMetrics());
    JoinGroupRequestData request = new JoinGroupRequestData().setGroupId("foo").setSessionTimeoutMs(1000);
    service.startup(() -> 1);
    when(runtime.scheduleWriteOperation(ArgumentMatchers.eq("classic-group-join"), ArgumentMatchers.eq(new TopicPartition("__consumer_offsets", 0)), ArgumentMatchers.eq(Duration.ofMillis(5000)), ArgumentMatchers.any())).thenReturn(CompletableFuture.completedFuture(new JoinGroupResponseData()));
    CompletableFuture<JoinGroupResponseData> responseFuture = service.joinGroup(requestContext(ApiKeys.JOIN_GROUP), request, BufferSupplier.NO_CACHING);
    assertFalse(responseFuture.isDone());
}

```java:llm_gen

@Test
public void testJoinGroup() {
    CoordinatorRuntime<GroupCoordinatorShard, Record> runtime = mockRuntime();
    GroupCoordinatorService service = new GroupCoordinatorService(new LogContext(), createConfig(), runtime, new GroupCoordinatorMetrics());
    JoinGroupRequestData request = new JoinGroupRequestData()
        .setGroupId("foo")
        .setSessionTimeoutMs(60000);
    service.startup(() -> 1);
    when(runtime.scheduleWriteOperation(ArgumentMatchers.eq("classic-group-join"), ArgumentMatchers.eq(new TopicPartition("__consumer_offsets", 0)), ArgumentMatchers.eq(Duration.ofMillis(5000)), ArgumentMatchers.any())).thenReturn(CompletableFuture.completedFuture(new JoinGroupResponseData()));
    CompletableFuture<JoinGroupResponseData> responseFuture = service.joinGroup(requestContext(ApiKeys.JOIN_GROUP), request, BufferSupplier.NO_CACHING);
    assertFalse(responseFuture.isDone());
}

### 99.Correct
link: https://github.com/iluwatar/java-design-patterns/commit/3d48f069802a9bbfc2fc80fc236287fc8abc2177
p_path: guarded-suspension/src/main/java/com/iluwatar/guarded/suspension/GuardedQueue.java#get
t_path: guarded-suspension/src/test/java/com/iluwatar/guarded/suspension/GuardedQueueTest.java#testGet

```java:test_src

@Test
void testGet() {
    var g = new GuardedQueue();
    var executorService = Executors.newFixedThreadPool(2);
    executorService.submit(() -> value = g.get());
    executorService.submit(() -> g.put(10));
    executorService.shutdown();
    try {
        executorService.awaitTermination(30, TimeUnit.SECONDS);
    } catch (InterruptedException e) {
        e.printStackTrace();
    }
    assertEquals(Integer.valueOf(10), value);
}

```java:test_tgt

@Test
void testGet() {
    var g = new GuardedQueue();
    var executorService = Executors.newFixedThreadPool(2);
    executorService.submit(() -> value = g.get());
    executorService.submit(() -> g.put(10));
    executorService.shutdown();
    try {
        executorService.awaitTermination(30, TimeUnit.SECONDS);
    } catch (InterruptedException e) {
        LOGGER.error("Error occurred: ", e);
    }
    assertEquals(Integer.valueOf(10), value);
}

```java:llm_gen

@Test
void testGet() {
    var g = new GuardedQueue();
    var executorService = Executors.newFixedThreadPool(2);
    executorService.submit(() -> value = g.get());
    executorService.submit(() -> g.put(10));
    executorService.shutdown();
    try {
        executorService.awaitTermination(30, TimeUnit.SECONDS);
    } catch (InterruptedException e) {
        LOGGER.error("Error occurred: ", e);
    }
    assertEquals(Integer.valueOf(10), value);
}

### 100.Missing Asserts
link: https://github.com/hibernate/hibernate-tools/commit/faf434e6c71a2f51d86792b358f492a8888e5537
p_path: jbt/src/main/java/org/hibernate/tool/orm/jbt/internal/util/TypeRegistry.java#getType
t_path: jbt/src/test/java/org/hibernate/tool/orm/jbt/internal/util/TypeRegistryTest.java#testGetType

```java:test_src

@Test
public void testGetType() {
    assertEquals("boolean", TypeRegistry.getType("boolean").getName());
    assertEquals("byte", TypeRegistry.getType("byte").getName());
    assertEquals("big_integer", TypeRegistry.getType("big_integer").getName());
    assertEquals("short", TypeRegistry.getType("short").getName());
    assertEquals("calendar", TypeRegistry.getType("calendar").getName());
    assertEquals("calendar_date", TypeRegistry.getType("calendar_date").getName());
    assertEquals("integer", TypeRegistry.getType("integer").getName());
    assertEquals("big_decimal", TypeRegistry.getType("big_decimal").getName());
    assertEquals("character", TypeRegistry.getType("character").getName());
    assertEquals("class", TypeRegistry.getType("class").getName());
    assertEquals("currency", TypeRegistry.getType("currency").getName());
    assertEquals("date", TypeRegistry.getType("date").getName());
    assertEquals("double", TypeRegistry.getType("double").getName());
    assertEquals("float", TypeRegistry.getType("float").getName());
    assertEquals("locale", TypeRegistry.getType("locale").getName());
    assertEquals("long", TypeRegistry.getType("long").getName());
    assertEquals("string", TypeRegistry.getType("string").getName());
    assertEquals("text", TypeRegistry.getType("text").getName());
    assertEquals("time", TypeRegistry.getType("time").getName());
    assertEquals("timestamp", TypeRegistry.getType("timestamp").getName());
    assertEquals("timezone", TypeRegistry.getType("timezone").getName());
    assertEquals("true_false", TypeRegistry.getType("true_false").getName());
    assertEquals("yes_no", TypeRegistry.getType("yes_no").getName());
}

```java:test_tgt

@Test
public void testGetType() {
    assertEquals("boolean", TypeRegistry.getType("boolean").getName());
    assertEquals("byte", TypeRegistry.getType("byte").getName());
    assertEquals("big_integer", TypeRegistry.getType("big_integer").getName());
    assertEquals("short", TypeRegistry.getType("short").getName());
    assertEquals("calendar", TypeRegistry.getType("calendar").getName());
    assertEquals("calendar_date", TypeRegistry.getType("calendar_date").getName());
    assertEquals("integer", TypeRegistry.getType("integer").getName());
    assertEquals("big_decimal", TypeRegistry.getType("big_decimal").getName());
    assertEquals("character", TypeRegistry.getType("character").getName());
    assertEquals("class", TypeRegistry.getType("class").getName());
    assertEquals("currency", TypeRegistry.getType("currency").getName());
    assertEquals("date", TypeRegistry.getType("date").getName());
    assertEquals("double", TypeRegistry.getType("double").getName());
    assertEquals("float", TypeRegistry.getType("float").getName());
    assertEquals("locale", TypeRegistry.getType("locale").getName());
    assertEquals("long", TypeRegistry.getType("long").getName());
    assertEquals("string", TypeRegistry.getType("string").getName());
    assertEquals("text", TypeRegistry.getType("text").getName());
    assertEquals("time", TypeRegistry.getType("time").getName());
    assertEquals("timestamp", TypeRegistry.getType("timestamp").getName());
    assertEquals("timezone", TypeRegistry.getType("timezone").getName());
    assertEquals("true_false", TypeRegistry.getType("true_false").getName());
    assertEquals("yes_no", TypeRegistry.getType("yes_no").getName());
    assertNull(TypeRegistry.TYPE_REGISTRY.get(String.class.getName()));
    TypeWrapper stringWrapper = TypeRegistry.getType(String.class.getName());
    assertNotNull(stringWrapper);
    assertSame(TypeRegistry.TYPE_REGISTRY.get(String.class.getName()), stringWrapper);
    assertNull(TypeRegistry.TYPE_REGISTRY.get(Foo.class.getName()));
    TypeWrapper fooWrapper = TypeRegistry.getType(Foo.class.getName());
    assertNull(fooWrapper);
    assertNull(TypeRegistry.TYPE_REGISTRY.get(Foo.class.getName()));
}

```java:llm_gen

@Test
public void testGetType() {
    assertEquals("boolean", TypeRegistry.getType("boolean").getName());
    assertEquals("byte", TypeRegistry.getType("byte").getName());
    assertEquals("big_integer", TypeRegistry.getType("big_integer").getName());
    assertEquals("short", TypeRegistry.getType("short").getName());
    assertEquals("calendar", TypeRegistry.getType("calendar").getName());
    assertEquals("calendar_date", TypeRegistry.getType("calendar_date").getName());
    assertEquals("integer", TypeRegistry.getType("integer").getName());
    assertEquals("big_decimal", TypeRegistry.getType("big_decimal").getName());
    assertEquals("character", TypeRegistry.getType("character").getName());
    assertEquals("class", TypeRegistry.getType("class").getName());
    assertEquals("currency", TypeRegistry.getType("currency").getName());
    assertEquals("date", TypeRegistry.getType("date").getName());
    assertEquals("double", TypeRegistry.getType("double").getName());
    assertEquals("float", TypeRegistry.getType("float").getName());
    assertEquals("locale", TypeRegistry.getType("locale").getName());
    assertEquals("long", TypeRegistry.getType("long").getName());
    assertEquals("string", TypeRegistry.getType("string").getName());
    assertEquals("text", TypeRegistry.getType("text").getName());
    assertEquals("time", TypeRegistry.getType("time").getName());
    assertEquals("timestamp", TypeRegistry.getType("timestamp").getName());
    assertEquals("timezone", TypeRegistry.getType("timezone").getName());
    assertEquals("true_false", TypeRegistry.getType("true_false").getName());
    assertEquals("yes_no", TypeRegistry.getType("yes_no").getName());
    assertNull(TypeRegistry.getType("non_existent_type"));
}

### 101.Correct
link: https://github.com/apache/kafka/commit/2df8c1ca3de0bf428e90e3fbff311a24062a27bc
p_path: clients/src/main/java/org/apache/kafka/common/telemetry/internals/ClientTelemetryUtils.java#preferredCompressionType
t_path: clients/src/test/java/org/apache/kafka/common/telemetry/internals/ClientTelemetryUtilsTest.java#testPreferredCompressionType

```java:test_src

@Test
public void testPreferredCompressionType() {
    assertEquals(CompressionType.NONE, ClientTelemetryUtils.preferredCompressionType(Collections.emptyList()));
    assertEquals(CompressionType.NONE, ClientTelemetryUtils.preferredCompressionType(null));
}

```java:test_tgt

@Test
public void testPreferredCompressionType() {
    assertEquals(CompressionType.NONE, ClientTelemetryUtils.preferredCompressionType(Collections.emptyList()));
    assertEquals(CompressionType.NONE, ClientTelemetryUtils.preferredCompressionType(null));
    assertEquals(CompressionType.NONE, ClientTelemetryUtils.preferredCompressionType(Arrays.asList(CompressionType.NONE, CompressionType.GZIP)));
    assertEquals(CompressionType.GZIP, ClientTelemetryUtils.preferredCompressionType(Arrays.asList(CompressionType.GZIP, CompressionType.NONE)));
}

```java:llm_gen

@Test
public void testPreferredCompressionType() {
    assertEquals(CompressionType.NONE, ClientTelemetryUtils.preferredCompressionType(Collections.emptyList()));
    assertEquals(CompressionType.NONE, ClientTelemetryUtils.preferredCompressionType(null));
    assertEquals(CompressionType.GZIP, ClientTelemetryUtils.preferredCompressionType(Arrays.asList(CompressionType.GZIP)));
    assertEquals(CompressionType.SNAPPY, ClientTelemetryUtils.preferredCompressionType(Arrays.asList(CompressionType.SNAPPY, CompressionType.GZIP)));
}



### 102.Correct
link: https://github.com/cdk/cdk/commit/3c3ab2b678589c5c6aac953c40a12e49982b09b3
p_path: tool/builder3d/src/main/java/org/openscience/cdk/modeling/builder3d/AtomPlacer3D.java#isUnplacedHeavyAtom
t_path: tool/builder3d/src/test/java/org/openscience/cdk/modeling/builder3d/AtomPlacer3DTest.java#testIsUnplacedHeavyAtom

```java:test_src

@Test
void testIsUnplacedHeavyAtom() {
    IAtomContainer ac = makeMethaneWithExplicitHydrogens();
    IAtom carbon = ac.getAtom(0);
    IAtom hydrogen = ac.getAtom(1);
    AtomPlacer3D placer = new AtomPlacer3D();
    boolean result;
    result = placer.isUnplacedHeavyAtom(carbon);
    Assertions.assertTrue(result);
    result = placer.isUnplacedHeavyAtom(hydrogen);
    Assertions.assertFalse(result);
    carbon.setFlag(CDKConstants.ISPLACED, true);
    result = placer.isUnplacedHeavyAtom(carbon);
    Assertions.assertFalse(result);
    hydrogen.setFlag(CDKConstants.ISPLACED, true);
    result = placer.isUnplacedHeavyAtom(hydrogen);
    Assertions.assertFalse(result);
}

```java:test_tgt

@Test
void testIsUnplacedHeavyAtom() {
    IAtomContainer ac = makeMethaneWithExplicitHydrogens();
    IAtom carbon = ac.getAtom(0);
    IAtom hydrogen = ac.getAtom(1);
    AtomPlacer3D placer = new AtomPlacer3D();
    boolean result;
    result = placer.isUnplacedHeavyAtom(carbon);
    Assertions.assertTrue(result);
    result = placer.isUnplacedHeavyAtom(hydrogen);
    Assertions.assertFalse(result);
    carbon.setFlag(IChemObject.PLACED, true);
    result = placer.isUnplacedHeavyAtom(carbon);
    Assertions.assertFalse(result);
    hydrogen.setFlag(IChemObject.PLACED, true);
    result = placer.isUnplacedHeavyAtom(hydrogen);
    Assertions.assertFalse(result);
}

```java:llm_gen

@Test
void testIsUnplacedHeavyAtom() {
    IAtomContainer ac = makeMethaneWithExplicitHydrogens();
    IAtom carbon = ac.getAtom(0);
    IAtom hydrogen = ac.getAtom(1);
    AtomPlacer3D placer = new AtomPlacer3D();
    boolean result;
    result = placer.isUnplacedHeavyAtom(carbon);
    Assertions.assertTrue(result);
    result = placer.isUnplacedHeavyAtom(hydrogen);
    Assertions.assertFalse(result);
    carbon.setFlag(IChemObject.PLACED, true);
    result = placer.isUnplacedHeavyAtom(carbon);
    Assertions.assertFalse(result);
    hydrogen.setFlag(IChemObject.PLACED, true);
    result = placer.isUnplacedHeavyAtom(hydrogen);
    Assertions.assertFalse(result);
}

### 103.Test Preparation Error
link: https://github.com/apache/kylin/commit/4d3418c237d4a839a85573712d0111d81086a477
p_path: src/spark-project/engine-spark/src/main/java/org/apache/kylin/engine/spark/source/NSparkMetadataExplorer.java#listTables
t_path: src/spark-project/engine-spark/src/test/java/org/apache/kylin/engine/spark/source/NSparkMetadataExplorerTest.java#testListTables

```java:test_src

@Test
public void testListTables() throws Exception {
    NSparkMetadataExplorer sparkMetadataExplorer = new NSparkMetadataExplorer();
    List<String> tables = sparkMetadataExplorer.listTables("");
    Assert.assertTrue(tables != null && tables.size() > 0);
}

```java:test_tgt

@Test
public void testListTables() throws Exception {
    String testProject = "default";
    String testTableName = "DEFAULT.TEST_KYLIN_FACT";
    NSparkMetadataExplorer sparkMetadataExplorer = new NSparkMetadataExplorer();
    NTableMetadataManager tableMgr = NTableMetadataManager.getInstance(getTestConfig(), testProject);
    TableDesc fact = tableMgr.getTableDesc(testTableName);
    sparkMetadataExplorer.createSampleTable(fact);
    List<String> tables = sparkMetadataExplorer.listTables(testProject);
    Assert.assertTrue(tables != null && tables.size() > 0);
    boolean access = sparkMetadataExplorer.checkTableWithCache(false, "testUser", testTableName);
    boolean cacheAccess = sparkMetadataExplorer.checkTableWithCache(true, "testUser", testTableName);
    Assert.assertEquals(access, cacheAccess);
}

```java:llm_gen

@Test
public void testListTables() throws Exception {
    NSparkMetadataExplorer sparkMetadataExplorer = new NSparkMetadataExplorer();
    List<String> tables = sparkMetadataExplorer.listTables("");
    Assert.assertTrue(tables != null && tables.size() > 0);

    KylinConfig config = KylinConfig.getInstanceFromEnv();
    if (config.getTableAccessFilterEnable() && config.getKerberosProjectLevelEnable() && UserGroupInformation.isSecurityEnabled()) {
        boolean cacheEnabled = config.getTableAccessCacheEnable();
        UserGroupInformation ugi = UserGroupInformation.getCurrentUser();
        for (String table : tables) {
            String tableName = "" + "." + table;
            Assert.assertTrue(sparkMetadataExplorer.checkTableWithCache(cacheEnabled, ugi.getUserName(), tableName));
        }
    }
}

### 104.External File Modification
link: https://github.com/huanghongxun/HMCL/commit/95afaa51122907835e1790eb265b184a79f895c7
p_path: HMCLCore/src/main/java/org/jackhuang/hmcl/util/versioning/VersionRange.java#intersectionWith
t_path: HMCLCore/src/test/java/org/jackhuang/hmcl/util/versioning/VersionRangeTest.java#testIntersectionWith

```java:test_src

@Test
public void testIntersectionWith() {
    assertIntersectionWith(all(), all(), all());
    assertIntersectionWith(all(), empty(), empty());
    assertIntersectionWith(all(), between("10", "20"), between("10", "20"));
    assertIntersectionWith(all(), atLeast("10"), atLeast("10"));
    assertIntersectionWith(all(), atMost("10"), atMost("10"));
    assertIntersectionWith(empty(), empty(), empty());
    assertIntersectionWith(empty(), between("10", "20"), empty());
    assertIntersectionWith(empty(), atLeast("10"), empty());
    assertIntersectionWith(empty(), atMost("10"), empty());
    assertIntersectionWith(between("10", "20"), between("10", "20"), between("10", "20"));
    assertIntersectionWith(between("10", "20"), between("5", "20"), between("10", "20"));
    assertIntersectionWith(between("10", "20"), between("10", "25"), between("10", "20"));
    assertIntersectionWith(between("10", "20"), between("5", "25"), between("10", "20"));
    assertIntersectionWith(between("10", "20"), between("15", "20"), between("15", "20"));
    assertIntersectionWith(between("10", "20"), between("10", "15"), between("10", "15"));
    assertIntersectionWith(between("10", "20"), between("14", "16"), between("14", "16"));
    assertIntersectionWith(between("10", "20"), atLeast("5"), between("10", "20"));
    assertIntersectionWith(between("10", "20"), atLeast("10"), between("10", "20"));
    assertIntersectionWith(between("10", "20"), atLeast("15"), between("15", "20"));
    assertIntersectionWith(between("10", "20"), atLeast("20"), between("20", "20"));
    assertIntersectionWith(between("10", "20"), atLeast("25"), empty());
    assertIntersectionWith(between("10", "20"), atMost("25"), between("10", "20"));
    assertIntersectionWith(between("10", "20"), atMost("20"), between("10", "20"));
    assertIntersectionWith(between("10", "20"), atMost("15"), between("10", "15"));
    assertIntersectionWith(between("10", "20"), atMost("10"), between("10", "10"));
    assertIntersectionWith(between("10", "20"), atMost("5"), empty());
    assertIntersectionWith(atLeast("10"), atMost("10"), between("10", "10"));
    assertIntersectionWith(atLeast("10"), atMost("20"), between("10", "20"));
    assertIntersectionWith(atLeast("10"), atMost("5"), empty());
}

```java:test_tgt

@Test
public void testIntersectionWith() {
    assertIntersectionWith(all(), all(), all());
    assertIntersectionWith(all(), empty(), empty());
    assertIntersectionWith(all(), VersionNumber.between("10", "20"), VersionNumber.between("10", "20"));
    assertIntersectionWith(all(), VersionNumber.atLeast("10"), VersionNumber.atLeast("10"));
    assertIntersectionWith(all(), VersionNumber.atMost("10"), VersionNumber.atMost("10"));
    assertIntersectionWith(empty(), empty(), empty());
    assertIntersectionWith(empty(), VersionNumber.between("10", "20"), empty());
    assertIntersectionWith(empty(), VersionNumber.atLeast("10"), empty());
    assertIntersectionWith(empty(), VersionNumber.atMost("10"), empty());
    assertIntersectionWith(VersionNumber.between("10", "20"), VersionNumber.between("10", "20"), VersionNumber.between("10", "20"));
    assertIntersectionWith(VersionNumber.between("10", "20"), VersionNumber.between("5", "20"), VersionNumber.between("10", "20"));
    assertIntersectionWith(VersionNumber.between("10", "20"), VersionNumber.between("10", "25"), VersionNumber.between("10", "20"));
    assertIntersectionWith(VersionNumber.between("10", "20"), VersionNumber.between("5", "25"), VersionNumber.between("10", "20"));
    assertIntersectionWith(VersionNumber.between("10", "20"), VersionNumber.between("15", "20"), VersionNumber.between("15", "20"));
    assertIntersectionWith(VersionNumber.between("10", "20"), VersionNumber.between("10", "15"), VersionNumber.between("10", "15"));
    assertIntersectionWith(VersionNumber.between("10", "20"), VersionNumber.between("14", "16"), VersionNumber.between("14", "16"));
    assertIntersectionWith(VersionNumber.between("10", "20"), VersionNumber.atLeast("5"), VersionNumber.between("10", "20"));
    assertIntersectionWith(VersionNumber.between("10", "20"), VersionNumber.atLeast("10"), VersionNumber.between("10", "20"));
    assertIntersectionWith(VersionNumber.between("10", "20"), VersionNumber.atLeast("15"), VersionNumber.between("15", "20"));
    assertIntersectionWith(VersionNumber.between("10", "20"), VersionNumber.atLeast("20"), VersionNumber.between("20", "20"));
    assertIntersectionWith(VersionNumber.between("10", "20"), VersionNumber.atLeast("25"), empty());
    assertIntersectionWith(VersionNumber.between("10", "20"), VersionNumber.atMost("25"), VersionNumber.between("10", "20"));
    assertIntersectionWith(VersionNumber.between("10", "20"), VersionNumber.atMost("20"), VersionNumber.between("10", "20"));
    assertIntersectionWith(VersionNumber.between("10", "20"), VersionNumber.atMost("15"), VersionNumber.between("10", "15"));
    assertIntersectionWith(VersionNumber.between("10", "20"), VersionNumber.atMost("10"), VersionNumber.between("10", "10"));
    assertIntersectionWith(VersionNumber.between("10", "20"), VersionNumber.atMost("5"), empty());
    assertIntersectionWith(VersionNumber.atLeast("10"), VersionNumber.atMost("10"), VersionNumber.between("10", "10"));
    assertIntersectionWith(VersionNumber.atLeast("10"), VersionNumber.atMost("20"), VersionNumber.between("10", "20"));
    assertIntersectionWith(VersionNumber.atLeast("10"), VersionNumber.atMost("5"), empty());
}

```java:llm_gen

@Test
public void testIntersectionWith() {
    assertIntersectionWith(all(), all(), all());
    assertIntersectionWith(all(), empty(), empty());
    assertIntersectionWith(all(), between("10", "20"), between("10", "20"));
    assertIntersectionWith(all(), atLeast("10"), atLeast("10"));
    assertIntersectionWith(all(), atMost("10"), atMost("10"));
    assertIntersectionWith(empty(), empty(), empty());
    assertIntersectionWith(empty(), between("10", "20"), empty());
    assertIntersectionWith(empty(), atLeast("10"), empty());
    assertIntersectionWith(empty(), atMost("10"), empty());
    assertIntersectionWith(between("10", "20"), between("10", "20"), between("10", "20"));
    assertIntersectionWith(between("10", "20"), between("5", "20"), between("10", "20"));
    assertIntersectionWith(between("10", "20"), between("10", "25"), between("10", "20"));
    assertIntersectionWith(between("10", "20"), between("5", "25"), between("10", "20"));
    assertIntersectionWith(between("10", "20"), between("15", "20"), between("15", "20"));
    assertIntersectionWith(between("10", "20"), between("10", "15"), between("10", "15"));
    assertIntersectionWith(between("10", "20"), between("14", "16"), between("14", "16"));
    assertIntersectionWith(between("10", "20"), atLeast("5"), between("10", "20"));
    assertIntersectionWith(between("10", "20"), atLeast("10"), between("10", "20"));
    assertIntersectionWith(between("10", "20"), atLeast("15"), between("15", "20"));
    assertIntersectionWith(between("10", "20"), atLeast("20"), between("20", "20"));
    assertIntersectionWith(between("10", "20"), atLeast("25"), empty());
    assertIntersectionWith(between("10", "20"), atMost("25"), between("10", "20"));
    assertIntersectionWith(between("10", "20"), atMost("20"), between("10", "20"));
    assertIntersectionWith(between("10", "20"), atMost("15"), between("10", "15"));
    assertIntersectionWith(between("10", "20"), atMost("10"), between("10", "10"));
    assertIntersectionWith(between("10", "20"), atMost("5"), empty());
    assertIntersectionWith(atLeast("10"), atMost("10"), between("10", "10"));
    assertIntersectionWith(atLeast("10"), atMost("20"), between("10", "20"));
    assertIntersectionWith(atLeast("10"), atMost("5"), empty());
}

### 105.Correct
link: https://github.com/apache/kafka/commit/4c6f975ab3deba517c6621c4a051e9beb1240bbc
p_path: server-common/src/main/java/org/apache/kafka/common/DirectoryId.java#isOnline
t_path: server-common/src/test/java/org/apache/kafka/common/DirectoryIdTest.java#testIsOnline

```java:test_src

@Test
void testIsOnline() {
    List<Uuid> sortedDirs = Arrays.asList(Uuid.fromString("imQKg2cXTVe8OUFNa3R9bg"), Uuid.fromString("Mwy5wxTDQxmsZwGzjsaX7w"), Uuid.fromString("s8rHMluuSDCnxt3FmKwiyw"));
    sortedDirs.sort(Uuid::compareTo);
    assertTrue(DirectoryId.isOnline(Uuid.fromString("imQKg2cXTVe8OUFNa3R9bg"), sortedDirs));
    assertTrue(DirectoryId.isOnline(Uuid.fromString("Mwy5wxTDQxmsZwGzjsaX7w"), sortedDirs));
    assertTrue(DirectoryId.isOnline(Uuid.fromString("s8rHMluuSDCnxt3FmKwiyw"), sortedDirs));
    assertTrue(DirectoryId.isOnline(DirectoryId.MIGRATING, sortedDirs));
    assertTrue(DirectoryId.isOnline(DirectoryId.UNASSIGNED, sortedDirs));
    assertFalse(DirectoryId.isOnline(DirectoryId.LOST, sortedDirs));
    assertFalse(DirectoryId.isOnline(Uuid.fromString("AMYchbMtS6yhtsXbca7DQg"), sortedDirs));
}

```java:test_tgt

@Test
void testIsOnline() {
    List<Uuid> sortedDirs = Arrays.asList(Uuid.fromString("imQKg2cXTVe8OUFNa3R9bg"), Uuid.fromString("Mwy5wxTDQxmsZwGzjsaX7w"), Uuid.fromString("s8rHMluuSDCnxt3FmKwiyw"));
    sortedDirs.sort(Uuid::compareTo);
    List<Uuid> emptySortedDirs = Collections.emptyList();
    assertTrue(DirectoryId.isOnline(Uuid.fromString("imQKg2cXTVe8OUFNa3R9bg"), sortedDirs));
    assertTrue(DirectoryId.isOnline(Uuid.fromString("Mwy5wxTDQxmsZwGzjsaX7w"), sortedDirs));
    assertTrue(DirectoryId.isOnline(Uuid.fromString("s8rHMluuSDCnxt3FmKwiyw"), sortedDirs));
    assertTrue(DirectoryId.isOnline(DirectoryId.MIGRATING, sortedDirs));
    assertTrue(DirectoryId.isOnline(DirectoryId.UNASSIGNED, sortedDirs));
    assertFalse(DirectoryId.isOnline(DirectoryId.LOST, sortedDirs));
    assertFalse(DirectoryId.isOnline(Uuid.fromString("AMYchbMtS6yhtsXbca7DQg"), sortedDirs));
    assertTrue(DirectoryId.isOnline(Uuid.randomUuid(), emptySortedDirs));
}

```java:llm_gen

@Test
void testIsOnline() {
    List<Uuid> sortedDirs = Arrays.asList(Uuid.fromString("imQKg2cXTVe8OUFNa3R9bg"), Uuid.fromString("Mwy5wxTDQxmsZwGzjsaX7w"), Uuid.fromString("s8rHMluuSDCnxt3FmKwiyw"));
    sortedDirs.sort(Uuid::compareTo);
    assertTrue(DirectoryId.isOnline(Uuid.fromString("imQKg2cXTVe8OUFNa3R9bg"), sortedDirs));
    assertTrue(DirectoryId.isOnline(Uuid.fromString("Mwy5wxTDQxmsZwGzjsaX7w"), sortedDirs));
    assertTrue(DirectoryId.isOnline(Uuid.fromString("s8rHMluuSDCnxt3FmKwiyw"), sortedDirs));
    assertTrue(DirectoryId.isOnline(DirectoryId.MIGRATING, sortedDirs));
    assertTrue(DirectoryId.isOnline(DirectoryId.UNASSIGNED, sortedDirs));
    assertFalse(DirectoryId.isOnline(DirectoryId.LOST, sortedDirs));
    assertFalse(DirectoryId.isOnline(Uuid.fromString("AMYchbMtS6yhtsXbca7DQg"), sortedDirs));
    assertTrue(DirectoryId.isOnline(Uuid.fromString("imQKg2cXTVe8OUFNa3R9bg"), Collections.emptyList()));
}


### 106.Field/Package Information Modification
link: https://github.com/dhis2/dhis2-core/commit/95dda3c85212248a0ef9334f0aa358a5f7064416
p_path: dhis-2/dhis-services/dhis-service-analytics/src/main/java/org/hisp/dhis/analytics/util/AnalyticsIndexHelper.java#getIndexes
t_path: dhis-2/dhis-services/dhis-service-analytics/src/test/java/org/hisp/dhis/analytics/util/AnalyticsIndexHelperTest.java#testGetIndexes

```java:test_src

@Test
void testGetIndexes() {
    List<AnalyticsTablePartition> stubPartitions = List.of(stubAnalyticsTablePartition());
    List<AnalyticsIndex> indexes = getIndexes(stubPartitions);
    assertThat(indexes, hasSize(1));
    assertThat(indexes.get(0).getTable(), is(equalTo("analytics_event_temp_2022")));
    assertThat(indexes.get(0).getColumns(), hasSize(1));
    assertThat(indexes.get(0).getIndexType(), is(equalTo(BTREE)));
}

```java:test_tgt

@Test
void testGetIndexes() {
    List<AnalyticsTablePartition> stubPartitions = List.of(stubAnalyticsTablePartition());
    List<AnalyticsIndex> indexes = getIndexes(stubPartitions);
    assertThat(indexes, hasSize(1));
    assertThat(indexes.get(0).getTableName(), is(equalTo("analytics_event_temp_2022")));
    assertThat(indexes.get(0).getColumns(), hasSize(1));
    assertThat(indexes.get(0).getIndexType(), is(equalTo(BTREE)));
}

```java:llm_gen

@Test
void testGetIndexes() {
    List<AnalyticsTablePartition> stubPartitions = List.of(stubAnalyticsTablePartition());
    List<AnalyticsIndex> indexes = getIndexes(stubPartitions);
    assertThat(indexes, hasSize(1));
    assertThat(indexes.get(0).getTable(), is(equalTo("analytics_event_temp_2022")));
    assertThat(indexes.get(0).getColumns(), hasSize(1));
    assertThat(indexes.get(0).getIndexType(), is(equalTo(BTREE)));
}

### 107.Correct
link: https://github.com/relayrides/pushy/commit/c9f92fb90a24be73f2f1e7fbeedf4be86d75ebf0
p_path: dropwizard-metrics-listener/src/main/java/com/eatthepath/pushy/apns/metrics/dropwizard/DropwizardApnsClientMetricsListener.java#handleConnectionCreationFailed
t_path: dropwizard-metrics-listener/src/test/java/com/eatthepath/pushy/apns/metrics/dropwizard/DropwizardApnsClientMetricsListenerTest.java#testHandleConnectionCreationFailed

```java:test_src

@Test
public void testHandleConnectionCreationFailed() {
    final Meter connectionFailures = (Meter) this.listener.getMetrics().get(DropwizardApnsClientMetricsListener.CONNECTION_FAILURES_METER_NAME);
    assertEquals(0, connectionFailures.getCount());
    this.listener.handleConnectionCreationFailed(null);
    assertEquals(1, connectionFailures.getCount());
}

```java:test_tgt

@Test
public void testHandleConnectionCreationFailed() {
    final Meter connectionFailures = (Meter) this.listener.getMetrics().get(DropwizardApnsClientMetricsListener.CONNECTION_FAILURES_METER_NAME);
    assertEquals(0, connectionFailures.getCount());
    this.listener.handleConnectionCreationFailed();
    assertEquals(1, connectionFailures.getCount());
}

```java:llm_gen

@Test
public void testHandleConnectionCreationFailed() {
    final Meter connectionFailures = (Meter) this.listener.getMetrics().get(DropwizardApnsClientMetricsListener.CONNECTION_FAILURES_METER_NAME);
    assertEquals(0, connectionFailures.getCount());
    this.listener.handleConnectionCreationFailed();
    assertEquals(1, connectionFailures.getCount());
}

### 108.Correct
link: https://github.com/apache/logging-log4j2/commit/f27f6bce68f4c5e42b100366d5cf1b4018525e2a
p_path: log4j-api/src/main/java/org/apache/logging/log4j/spi/DefaultThreadContextMap.java#putAll
t_path: log4j-api-test/src/test/java/org/apache/logging/log4j/spi/DefaultThreadContextMapTest.java#testPutAll

```java:test_src

@Test
public void testPutAll() {
    final DefaultThreadContextMap map = new DefaultThreadContextMap(true);
    assertTrue(map.isEmpty());
    assertFalse(map.containsKey("key"));
    final int mapSize = 10;
    final Map<String, String> newMap = new HashMap<>(mapSize);
    for (int i = 1; i <= mapSize; i++) {
        newMap.put("key" + i, "value" + i);
    }
    map.putAll(newMap);
    assertFalse(map.isEmpty());
    for (int i = 1; i <= mapSize; i++) {
        assertTrue(map.containsKey("key" + i));
        assertEquals("value" + i, map.get("key" + i));
    }
}

```java:test_tgt

@Test
void testPutAll() {
    final DefaultThreadContextMap map = new DefaultThreadContextMap();
    assertTrue(map.isEmpty());
    assertFalse(map.containsKey("key"));
    final int mapSize = 10;
    final Map<String, String> newMap = new HashMap<>(mapSize);
    for (int i = 1; i <= mapSize; i++) {
        newMap.put("key" + i, "value" + i);
    }
    map.putAll(newMap);
    assertFalse(map.isEmpty());
    for (int i = 1; i <= mapSize; i++) {
        assertTrue(map.containsKey("key" + i));
        assertEquals("value" + i, map.get("key" + i));
    }
}

```java:llm_gen

@Test
public void testPutAll() {
    final DefaultThreadContextMap map = new DefaultThreadContextMap(true);
    assertTrue(map.isEmpty());
    assertFalse(map.containsKey("key"));
    final int mapSize = 10;
    final Map<String, String> newMap = new HashMap<>(mapSize);
    for (int i = 1; i <= mapSize; i++) {
        newMap.put("key" + i, "value" + i);
    }
    map.putAll(newMap);
    assertFalse(map.isEmpty());
    for (int i = 1; i <= mapSize; i++) {
        assertTrue(map.containsKey("key" + i));
        assertEquals("value" + i, map.get("key" + i));
    }
}

### 109.Correct
link: https://github.com/apache/hudi/commit/b99bf709e1927ccbc05a24b9b5609da4b140f5c0
p_path: hudi-common/src/main/java/org/apache/hudi/common/fs/FSUtils.java#makeQualified
t_path: hudi-common/src/test/java/org/apache/hudi/common/fs/TestFSUtils.java#testMakeQualified

```java:test_src

@Test
public void testMakeQualified() {
    FileSystem fs = HadoopFSUtils.getFs("file:///a/b/c", new Configuration());
    FileSystem wrapperFs = new HoodieWrapperFileSystem(fs, new NoOpConsistencyGuard());
    HoodieStorage storage = new HoodieHadoopStorage(fs);
    HoodieStorage wrapperStorage = new HoodieHadoopStorage(wrapperFs);
    assertEquals(new HoodieLocation("file:///x/y"), FSUtils.makeQualified(storage, new HoodieLocation("/x/y")));
    assertEquals(new HoodieLocation("file:///x/y"), FSUtils.makeQualified(wrapperStorage, new HoodieLocation("/x/y")));
    assertEquals(new HoodieLocation("s3://x/y"), FSUtils.makeQualified(storage, new HoodieLocation("s3://x/y")));
    assertEquals(new HoodieLocation("s3://x/y"), FSUtils.makeQualified(wrapperStorage, new HoodieLocation("s3://x/y")));
}

```java:test_tgt

@Test
public void testMakeQualified() {
    FileSystem fs = HadoopFSUtils.getFs("file:///a/b/c", new Configuration());
    FileSystem wrapperFs = new HoodieWrapperFileSystem(fs, new NoOpConsistencyGuard());
    HoodieStorage storage = new HoodieHadoopStorage(fs);
    HoodieStorage wrapperStorage = new HoodieHadoopStorage(wrapperFs);
    assertEquals(new StoragePath("file:///x/y"), FSUtils.makeQualified(storage, new StoragePath("/x/y")));
    assertEquals(new StoragePath("file:///x/y"), FSUtils.makeQualified(wrapperStorage, new StoragePath("/x/y")));
    assertEquals(new StoragePath("s3://x/y"), FSUtils.makeQualified(storage, new StoragePath("s3://x/y")));
    assertEquals(new StoragePath("s3://x/y"), FSUtils.makeQualified(wrapperStorage, new StoragePath("s3://x/y")));
}

```java:llm_gen

@Test
public void testMakeQualified() {
    FileSystem fs = HadoopFSUtils.getFs("file:///a/b/c", new Configuration());
    FileSystem wrapperFs = new HoodieWrapperFileSystem(fs, new NoOpConsistencyGuard());
    HoodieStorage storage = new HoodieHadoopStorage(fs);
    HoodieStorage wrapperStorage = new HoodieHadoopStorage(wrapperFs);
    assertEquals(new StoragePath("file:///x/y"), FSUtils.makeQualified(storage, new StoragePath("/x/y")));
    assertEquals(new StoragePath("file:///x/y"), FSUtils.makeQualified(wrapperStorage, new StoragePath("/x/y")));
    assertEquals(new StoragePath("s3://x/y"), FSUtils.makeQualified(storage, new StoragePath("s3://x/y")));
    assertEquals(new StoragePath("s3://x/y"), FSUtils.makeQualified(wrapperStorage, new StoragePath("s3://x/y")));
}


### 110.Field/Package Information Modification
link: https://github.com/openhab/openhab-core/commit/1b503afdbbc654e0d845dce7c713813cf652ead5
p_path: bundles/org.openhab.core.persistence/src/main/java/org/openhab/core/persistence/extensions/PersistenceExtensions.java#lastUpdate
t_path: bundles/org.openhab.core.persistence/src/test/java/org/openhab/core/persistence/extensions/PersistenceExtensionsTest.java#testLastUpdate

```java:test_src

@Test
public void testLastUpdate() {
    numberItem.setState(new DecimalType(2005));
    ZonedDateTime lastUpdate = PersistenceExtensions.lastUpdate(numberItem, TestPersistenceService.ID);
    assertNotNull(lastUpdate);
    assertEquals(ZonedDateTime.of(2012, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), lastUpdate);
    lastUpdate = PersistenceExtensions.lastUpdate(numberItem);
    assertNull(lastUpdate);
}

```java:test_tgt

@Test
public void testLastUpdate() {
    ZonedDateTime lastUpdate = PersistenceExtensions.lastUpdate(numberItem, SERVICE_ID);
    assertNotNull(lastUpdate);
    assertEquals(ZonedDateTime.of(HISTORIC_END, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), lastUpdate);
    lastUpdate = PersistenceExtensions.lastUpdate(numberItem);
    assertNull(lastUpdate);
}

```java:llm_gen

@Test
public void testLastUpdate() {
    numberItem.setState(new DecimalType(2005));
    ZonedDateTime lastUpdate = PersistenceExtensions.lastUpdate(numberItem, TestPersistenceService.ID);
    assertNotNull(lastUpdate);
    assertEquals(ZonedDateTime.of(2012, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), lastUpdate);
    lastUpdate = PersistenceExtensions.lastUpdate(numberItem, null);
    assertNull(lastUpdate);
}


### 111.Additional Asserts
link: https://github.com/apache/incubator-pinot/commit/283363af87a63af692b30fcf4ac67fd837003304
p_path: pinot-plugins/pinot-minion-tasks/pinot-minion-builtin-tasks/src/main/java/org/apache/pinot/plugin/minion/tasks/MinionTaskUtils.java#extractMinionAllowDownloadFromServer
t_path: pinot-plugins/pinot-minion-tasks/pinot-minion-builtin-tasks/src/test/java/org/apache/pinot/plugin/minion/tasks/MinionTaskUtilsTest.java#testExtractMinionAllowDownloadFromServer

```java:test_src

@Test
public void testExtractMinionAllowDownloadFromServer() {
    Map<String, String> configs = new HashMap<>();
    TableTaskConfig tableTaskConfig = new TableTaskConfig(Collections.singletonMap(MinionConstants.MergeRollupTask.TASK_TYPE, configs));
    TableConfig tableConfig = new TableConfigBuilder(TableType.OFFLINE).setTableName("sampleTable").setTaskConfig(tableTaskConfig).build();
    assertFalse(MinionTaskUtils.extractMinionAllowDownloadFromServer(tableConfig, MinionConstants.MergeRollupTask.TASK_TYPE));
    configs.put(TableTaskConfig.MINION_ALLOW_DOWNLOAD_FROM_SERVER, "true");
    tableTaskConfig = new TableTaskConfig(Collections.singletonMap(MinionConstants.MergeRollupTask.TASK_TYPE, configs));
    tableConfig = new TableConfigBuilder(TableType.OFFLINE).setTableName("sampleTable").setTaskConfig(tableTaskConfig).build();
    assertTrue(MinionTaskUtils.extractMinionAllowDownloadFromServer(tableConfig, MinionConstants.MergeRollupTask.TASK_TYPE));
    configs.put(TableTaskConfig.MINION_ALLOW_DOWNLOAD_FROM_SERVER, "false");
    tableTaskConfig = new TableTaskConfig(Collections.singletonMap(MinionConstants.MergeRollupTask.TASK_TYPE, configs));
    tableConfig = new TableConfigBuilder(TableType.OFFLINE).setTableName("sampleTable").setTaskConfig(tableTaskConfig).build();
    assertFalse(MinionTaskUtils.extractMinionAllowDownloadFromServer(tableConfig, MinionConstants.MergeRollupTask.TASK_TYPE));
}

```java:test_tgt

@Test
public void testExtractMinionAllowDownloadFromServer() {
    Map<String, String> configs = new HashMap<>();
    TableTaskConfig tableTaskConfig = new TableTaskConfig(Collections.singletonMap(MinionConstants.MergeRollupTask.TASK_TYPE, configs));
    TableConfig tableConfig = new TableConfigBuilder(TableType.OFFLINE).setTableName("sampleTable").setTaskConfig(tableTaskConfig).build();
    assertFalse(MinionTaskUtils.extractMinionAllowDownloadFromServer(tableConfig, MinionConstants.MergeRollupTask.TASK_TYPE, false));
    configs.put(TableTaskConfig.MINION_ALLOW_DOWNLOAD_FROM_SERVER, "true");
    tableTaskConfig = new TableTaskConfig(Collections.singletonMap(MinionConstants.MergeRollupTask.TASK_TYPE, configs));
    tableConfig = new TableConfigBuilder(TableType.OFFLINE).setTableName("sampleTable").setTaskConfig(tableTaskConfig).build();
    assertTrue(MinionTaskUtils.extractMinionAllowDownloadFromServer(tableConfig, MinionConstants.MergeRollupTask.TASK_TYPE, false));
    configs.put(TableTaskConfig.MINION_ALLOW_DOWNLOAD_FROM_SERVER, "false");
    tableTaskConfig = new TableTaskConfig(Collections.singletonMap(MinionConstants.MergeRollupTask.TASK_TYPE, configs));
    tableConfig = new TableConfigBuilder(TableType.OFFLINE).setTableName("sampleTable").setTaskConfig(tableTaskConfig).build();
    assertFalse(MinionTaskUtils.extractMinionAllowDownloadFromServer(tableConfig, MinionConstants.MergeRollupTask.TASK_TYPE, false));
}

```java:llm_gen

@Test
public void testExtractMinionAllowDownloadFromServer() {
    Map<String, String> configs = new HashMap<>();
    TableTaskConfig tableTaskConfig = new TableTaskConfig(Collections.singletonMap(MinionConstants.MergeRollupTask.TASK_TYPE, configs));
    TableConfig tableConfig = new TableConfigBuilder(TableType.OFFLINE).setTableName("sampleTable").setTaskConfig(tableTaskConfig).build();
    assertFalse(MinionTaskUtils.extractMinionAllowDownloadFromServer(tableConfig, MinionConstants.MergeRollupTask.TASK_TYPE, false));
    configs.put(TableTaskConfig.MINION_ALLOW_DOWNLOAD_FROM_SERVER, "true");
    tableTaskConfig = new TableTaskConfig(Collections.singletonMap(MinionConstants.MergeRollupTask.TASK_TYPE, configs));
    tableConfi.setTableNg = new TableConfigBuilder(TableType.OFFLINE)ame("sampleTable").setTaskConfig(tableTaskConfig).build();
    assertTrue(MinionTaskUtils.extractMinionAllowDownloadFromServer(tableConfig, MinionConstants.MergeRollupTask.TASK_TYPE, false));
    configs.put(TableTaskConfig.MINION_ALLOW_DOWNLOAD_FROM_SERVER, "false");
    tableTaskConfig = new TableTaskConfig(Collections.singletonMap(MinionConstants.MergeRollupTask.TASK_TYPE, configs));
    tableConfig = new TableConfigBuilder(TableType.OFFLINE).setTableName("sampleTable").setTaskConfig(tableTaskConfig).build();
    assertFalse(MinionTaskUtils.extractMinionAllowDownloadFromServer(tableConfig, MinionConstants.MergeRollupTask.TASK_TYPE, false));
    assertTrue(MinionTaskUtils.extractMinionAllowDownloadFromServer(tableConfig, MinionConstants.MergeRollupTask.TASK_TYPE, true));
}

### 112.Correct
link: https://github.com/halo-dev/halo/commit/0e17d53ede66c57b12f2dec4c92874c7e69ed9ef
p_path: application/src/main/java/run/halo/app/core/extension/reconciler/PostReconciler.java#subscribeNewCommentNotification
t_path: application/src/test/java/run/halo/app/core/extension/reconciler/PostReconcilerTest.java#subscribeNewCommentNotificationTest

````java:test_src

@Test
void subscribeNewCommentNotificationTest() {
    Post post = TestPost.postV1();
    postReconciler.subscribeNewCommentNotification(post);
    verify(notificationCenter).subscribe(assertArg(subscriber -> assertThat(subscriber.getName()).isEqualTo(post.getSpec().getOwner())), assertArg(argReason -> {
        var interestReason = new Subscription.InterestReason();
        interestReason.setReasonType(NotificationReasonConst.NEW_COMMENT_ON_POST);
        interestReason.setSubject(Subscription.ReasonSubject.builder().apiVersion(post.getApiVersion()).kind(post.getKind()).name(post.getMetadata().getName()).build());
        assertThat(argReason).isEqualTo(interestReason);
    }));
}

```java:test_tgt

@Test
void subscribeNewCommentNotificationTest() {
    Post post = TestPost.postV1();
    postReconciler.subscribeNewCommentNotification(post);
    verify(notificationCenter).subscribe(assertArg(subscriber -> assertThat(subscriber.getName()).isEqualTo(post.getSpec().getOwner())), assertArg(argReason -> {
        var interestReason = new Subscription.InterestReason();
        interestReason.setReasonType(NotificationReasonConst.NEW_COMMENT_ON_POST);
        interestReason.setExpression("props.postOwner == 'null'");
        assertThat(argReason).isEqualTo(interestReason);
    }));
}

```java:llm_gen

@Test
void subscribeNewCommentNotificationTest() {
    Post post = TestPost.postV1();
    postReconciler.subscribeNewCommentNotification(post);
    verify(notificationCenter).subscribe(assertArg(subscriber -> assertThat(subscriber.getName()).isEqualTo(post.getSpec().getOwner())), assertArg(argReason -> {
        var interestReason = new Subscription.InterestReason();
        interestReason.setReasonType(NotificationReasonConst.NEW_COMMENT_ON_POST);
        interestReason.setExpression("props.postOwner == '%s'".formatted(post.getSpec().getOwner()));
        assertThat(argReason).isEqualTo(interestReason);
    }));
}


### 113.Correct
link: https://github.com/apache/hudi/commit/8a0ce61b2fd187243e89254cdef528b3b1cb49e8
p_path: hudi-client/hudi-client-common/src/main/java/org/apache/hudi/table/repair/RepairUtils.java#tagInstantsOfBaseAndLogFiles
t_path: hudi-client/hudi-client-common/src/test/java/org/apache/hudi/table/repair/TestRepairUtils.java#testTagInstantsOfBaseAndLogFiles

```java:test_src

@Test
public void testTagInstantsOfBaseAndLogFiles() {
    Map<String, List<String>> expectedResult = new HashMap<>();
    List<Path> inputPathList = new ArrayList<>();
    for (Map.Entry<String, List<Pair<String, String>>> entry : BASE_FILE_INFO.entrySet()) {
        String instantTime = entry.getKey();
        List<String> fileNameList = entry.getValue().stream().map(e -> {
            String partitionPath = e.getKey();
            String fileId = e.getValue();
            return new Path(new Path(partitionPath), getBaseFilename(instantTime, fileId)).toString();
        }).collect(Collectors.toList());
        List<String> expectedList = expectedResult.computeIfAbsent(instantTime, k -> new ArrayList<>());
        expectedList.addAll(fileNameList);
        inputPathList.addAll(fileNameList.stream().map(path -> new Path(basePath, path)).collect(Collectors.toList()));
    }
    for (Map.Entry<String, List<Pair<String, String>>> entry : LOG_FILE_INFO.entrySet()) {
        String instantTime = entry.getKey();
        List<String> fileNameList = entry.getValue().stream().map(e -> {
            String partitionPath = e.getKey();
            String fileId = e.getValue();
            return new Path(new Path(partitionPath), getLogFilename(instantTime, fileId)).toString();
        }).collect(Collectors.toList());
        List<String> expectedList = expectedResult.computeIfAbsent(instantTime, k -> new ArrayList<>());
        expectedList.addAll(fileNameList);
        inputPathList.addAll(fileNameList.stream().map(path -> new Path(basePath, path)).collect(Collectors.toList()));
    }
    assertEquals(expectedResult, RepairUtils.tagInstantsOfBaseAndLogFiles(basePath, inputPathList));
}

```java:test_tgt

@Test
public void testTagInstantsOfBaseAndLogFiles() {
    Map<String, List<String>> expectedResult = new HashMap<>();
    List<StoragePath> inputPathList = new ArrayList<>();
    for (Map.Entry<String, List<Pair<String, String>>> entry : BASE_FILE_INFO.entrySet()) {
        String instantTime = entry.getKey();
        List<String> fileNameList = entry.getValue().stream().map(e -> {
            String partitionPath = e.getKey();
            String fileId = e.getValue();
            return new StoragePath(new StoragePath(partitionPath), getBaseFilename(instantTime, fileId)).toString();
        }).collect(Collectors.toList());
        List<String> expectedList = expectedResult.computeIfAbsent(instantTime, k -> new ArrayList<>());
        expectedList.addAll(fileNameList);
        inputPathList.addAll(fileNameList.stream().map(path -> new StoragePath(basePath, path)).collect(Collectors.toList()));
    }
    for (Map.Entry<String, List<Pair<String, String>>> entry : LOG_FILE_INFO.entrySet()) {
        String instantTime = entry.getKey();
        List<String> fileNameList = entry.getValue().stream().map(e -> {
            String partitionPath = e.getKey();
            String fileId = e.getValue();
            return new StoragePath(new StoragePath(partitionPath), getLogFilename(instantTime, fileId)).toString();
        }).collect(Collectors.toList());
        List<String> expectedList = expectedResult.computeIfAbsent(instantTime, k -> new ArrayList<>());
        expectedList.addAll(fileNameList);
        inputPathList.addAll(fileNameList.stream().map(path -> new StoragePath(basePath, path)).collect(Collectors.toList()));
    }
    assertEquals(expectedResult, RepairUtils.tagInstantsOfBaseAndLogFiles(basePath, inputPathList));
}

```java:llm_gen

@Test
public void testTagInstantsOfBaseAndLogFiles() {
    Map<String, List<String>> expectedResult = new HashMap<>();
    List<StoragePath> inputPathList = new ArrayList<>();
    for (Map.Entry<String, List<Pair<String, String>>> entry : BASE_FILE_INFO.entrySet()) {
        String instantTime = entry.getKey();
        List<String> fileNameList = entry.getValue().stream().map(e -> {
            String partitionPath = e.getKey();
            String fileId = e.getValue();
            return new StoragePath(new StoragePath(partitionPath), getBaseFilename(instantTime, fileId)).toString();
        }).collect(Collectors.toList());
        List<String> expectedList = expectedResult.computeIfAbsent(instantTime, k -> new ArrayList<>());
        expectedList.addAll(fileNameList);
        inputPathList.addAll(fileNameList.stream().map(path -> new StoragePath(basePath, path)).collect(Collectors.toList()));
    }
    for (Map.Entry<String, List<Pair<String, String>>> entry : LOG_FILE_INFO.entrySet()) {
        String instantTime = entry.getKey();
        List<String> fileNameList = entry.getValue().stream().map(e -> {
            String partitionPath = e.getKey();
            String fileId = e.getValue();
            return new StoragePath(new StoragePath(partitionPath), getLogFilename(instantTime, fileId)).toString();
        }).collect(Collectors.toList());
        List<String> expectedList = expectedResult.computeIfAbsent(instantTime, k -> new ArrayList<>());
        expectedList.addAll(fileNameList);
        inputPathList.addAll(fileNameList.stream().map(path -> new StoragePath(basePath, path)).collect(Collectors.toList()));
    }
    assertEquals(expectedResult, RepairUtils.tagInstantsOfBaseAndLogFiles(basePath, inputPathList));
}

### 114.Wrong Update Direction
link: https://github.com/datageartech/datagear/commit/e67700aaedf7dac47e709f99b51c732a01a99a39
p_path: datagear-meta/src/main/java/org/datagear/meta/resolver/DefaultTableTypeResolver.java#isDataTable
t_path: datagear-meta/src/test/java/org/datagear/meta/DefaultTableTypeResolverTest.java#isDataTableTest

```java:test_src

@Test
public void isDataTableTest() throws Exception {
    {
        DefaultTableTypeResolver resolver = new DefaultTableTypeResolver();
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "table")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "TABLE")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "view")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "VIEW")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "alias")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "AliAs")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "synonym")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "SYnonyM")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", null)));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "SYSTEM TABLE")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "SYSTEM table")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "LOCAL TEMPORARY")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "local TEMPORARY")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "GLOBAL TEMPORARY")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "global temporary")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "unknown")));
    }
    {
        DefaultTableTypeResolver resolver = new DefaultTableTypeResolver();
        List<DbTableTypeSpec> dbTableTypeSpecs = new ArrayList<>();
        dbTableTypeSpecs.add(new DbTableTypeSpec("oracle", Collections.emptyList(), Arrays.asList("*view*")));
        dbTableTypeSpecs.add(new DbTableTypeSpec("mysql", Collections.emptyList(), Arrays.asList("*table*", "null", "*unknown*")));
        resolver.setDbTableTypeSpecs(dbTableTypeSpecs);
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "TABLE")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "table")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "A-TABLE-B")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "a-table-b")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", null)));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "SYSTEM TABLE")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "unknown")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "view")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "VIEW")));
    }
}

```java:test_tgt

@Test
public void isDataTableTest() throws Exception {
    {
        DefaultTableTypeResolver resolver = new DefaultTableTypeResolver();
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "table")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "TABLE")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "view")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "VIEW")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "alias")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "AliAs")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "synonym")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "SYnonyM")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", null)));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "SYSTEM TABLE")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "SYSTEM table")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "LOCAL TEMPORARY")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "local TEMPORARY")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "GLOBAL TEMPORARY")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "global temporary")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "unknown")));
    }
    {
        DefaultTableTypeResolver resolver = new DefaultTableTypeResolver();
        List<DbTableTypeSpec> dbTableTypeSpecs = new ArrayList<>();
        dbTableTypeSpecs.add(new DbTableTypeSpec("*oracle*", Collections.emptyList(), Arrays.asList("view")));
        dbTableTypeSpecs.add(new DbTableTypeSpec("*mysql*", Collections.emptyList(), Arrays.asList("table", "null", "unknown")));
        resolver.setDbTableTypeSpecs(dbTableTypeSpecs);
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "TABLE")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "table")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", null)));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "unknown")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "A-TABLE-B")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "view")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "VIEW")));
    }
}

```java:llm_gen

@Test
public void isDataTableTest() throws Exception {
    {
        DefaultTableTypeResolver resolver = new DefaultTableTypeResolver();
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "table")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "TABLE")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "view")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "VIEW")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "alias")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "AliAs")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "synonym")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "SYnonyM")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", null)));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "SYSTEM TABLE")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "SYSTEM table")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "LOCAL TEMPORARY")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "local TEMPORARY")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "GLOBAL TEMPORARY")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "global temporary")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "unknown")));
    }
    {
        DefaultTableTypeResolver resolver = new DefaultTableTypeResolver();
        List<DbTableTypeSpec> dbTableTypeSpecs = new ArrayList<>();
        dbTableTypeSpecs.add(new DbTableTypeSpec("oracle", Collections.emptyList(), Arrays.asList("VIEW")));
        dbTableTypeSpecs.add(new DbTableTypeSpec("mysql", Collections.emptyList(), Arrays.asList("TABLE", "null", "unknown")));
        resolver.setDbTableTypeSpecs(dbTableTypeSpecs);
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "TABLE")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "table")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "A-TABLE-B")));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "a-table-b")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", null)));
        assertFalse(resolver.isDataTable(connection, new SimpleTable("test", "SYSTEM TABLE")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "unknown")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "view")));
        assertTrue(resolver.isDataTable(connection, new SimpleTable("test", "VIEW")));
    }
}

### 115.Correct
link: https://github.com/ctripcorp/x-pipe/commit/b603d5d1aace0bbc9e450ece2d079cf8c0755a22
p_path: redis/redis-console/src/main/java/com/ctrip/xpipe/redis/console/controller/api/data/ClusterUpdateController.java#getClusters
t_path: redis/redis-console/src/test/java/com/ctrip/xpipe/redis/console/controller/api/data/ClusterUpdateControllerTest.java#testGetClusters

```java:test_src

@Test
public void testGetClusters() throws CheckFailException {
    ClusterTbl clusterTbl1 = new ClusterTbl().setClusterName("cluster-name1").setClusterType(ClusterType.SINGLE_DC.toString()).setClusterDescription("").setActivedcId(1).setIsXpipeInterested(true).setStatus("normal").setClusterDesignatedRouteIds("").setClusterLastModifiedTime(DateTimeUtils.currentTimeAsString());
    ClusterTbl clusterTbl2 = new ClusterTbl().setClusterName("cluster-name2").setClusterType(ClusterType.SINGLE_DC.toString()).setClusterDescription("").setActivedcId(2).setIsXpipeInterested(true).setStatus("normal").setClusterDesignatedRouteIds("").setClusterLastModifiedTime(DateTimeUtils.currentTimeAsString());
    clusterDao.createCluster(clusterTbl1);
    clusterDao.createCluster(clusterTbl2);
    List<ClusterCreateInfo> clusters = clusterController.getClusters(ClusterType.SINGLE_DC.toString());
    Assert.assertEquals(2, clusters.size());
    Assert.assertEquals("cluster-name1", clusters.get(0).getClusterName());
    Assert.assertEquals("cluster-name2", clusters.get(1).getClusterName());
}

```java:test_tgt

@Test
public void testGetClusters() throws CheckFailException {
    ClusterTbl clusterTbl1 = new ClusterTbl().setClusterName("cluster-name1").setClusterType(ClusterType.SINGLE_DC.toString()).setClusterDescription("").setActivedcId(1).setIsXpipeInterested(true).setStatus("normal").setClusterDesignatedRouteIds("").setClusterLastModifiedTime(DateTimeUtils.currentTimeAsString());
    ClusterTbl clusterTbl2 = new ClusterTbl().setClusterName("cluster-name2").setClusterType(ClusterType.SINGLE_DC.toString()).setClusterDescription("").setActivedcId(2).setIsXpipeInterested(true).setStatus("normal").setClusterDesignatedRouteIds("").setClusterLastModifiedTime(DateTimeUtils.currentTimeAsString());
    clusterDao.createCluster(clusterTbl1);
    clusterDao.createCluster(clusterTbl2);
    List<ClusterCreateInfo> clusters = clusterController.getClusters(Collections.singleton(ClusterType.SINGLE_DC.toString()));
    Assert.assertEquals(2, clusters.size());
    Assert.assertEquals("cluster-name1", clusters.get(0).getClusterName());
    Assert.assertEquals("cluster-name2", clusters.get(1).getClusterName());
}

```java:llm_gen

@Test
public void testGetClusters() throws CheckFailException {
    ClusterTbl clusterTbl1 = new ClusterTbl().setClusterName("cluster-name1").setClusterType(ClusterType.SINGLE_DC.toString()).setClusterDescription("").setActivedcId(1).setIsXpipeInterested(true).setStatus("normal").setClusterDesignatedRouteIds("").setClusterLastModifiedTime(DateTimeUtils.currentTimeAsString());
    ClusterTbl clusterTbl2 = new ClusterTbl().setClusterName("cluster-name2").setClusterType(ClusterType.SINGLE_DC.toString()).setClusterDescription("").setActivedcId(2).setIsXpipeInterested(true).setStatus("normal").setClusterDesignatedRouteIds("").setClusterLastModifiedTime(DateTimeUtils.currentTimeAsString());
    clusterDao.createCluster(clusterTbl1);
    clusterDao.createCluster(clusterTbl2);
    List<ClusterCreateInfo> clusters = clusterController.getClusters(Collections.singleton(ClusterType.SINGLE_DC.toString()));
    Assert.assertEquals(2, clusters.size());
    Assert.assertEquals("cluster-name1", clusters.get(0).getClusterName());
    Assert.assertEquals("cluster-name2", clusters.get(1).getClusterName());
}

### 116.Correct
link: https://github.com/google/tink/commit/b0c03e2304a0a0cc20f6ba8de4a6b85f8d1683be
p_path: java_src/src/main/java/com/google/crypto/tink/streamingaead/StreamingAeadKeyTemplates.java#createAesCtrHmacStreamingKeyTemplate
t_path: java_src/src/test/java/com/google/crypto/tink/streamingaead/StreamingAeadKeyTemplatesTest.java#testCreateAesCtrHmacStreamingKeyTemplate

```java:test_src

@Test
public void testCreateAesCtrHmacStreamingKeyTemplate() throws Exception {
    int mainKeySize = 42;
    int derivedKeySize = 24;
    int tagSize = 45;
    int ciphertextSegmentSize = 12345;
    HashType hkdfHashType = HashType.SHA512;
    HashType macHashType = HashType.UNKNOWN_HASH;
    KeyTemplate template = StreamingAeadKeyTemplates.createAesCtrHmacStreamingKeyTemplate(mainKeySize, hkdfHashType, derivedKeySize, macHashType, tagSize, ciphertextSegmentSize);
    assertEquals(new AesCtrHmacStreamingKeyManager().getKeyType(), template.getTypeUrl());
    assertEquals(OutputPrefixType.RAW, template.getOutputPrefixType());
    AesCtrHmacStreamingKeyFormat format = AesCtrHmacStreamingKeyFormat.parseFrom(template.getValue(), ExtensionRegistryLite.getEmptyRegistry());
    assertEquals(mainKeySize, format.getKeySize());
    assertEquals(derivedKeySize, format.getParams().getDerivedKeySize());
    assertEquals(hkdfHashType, format.getParams().getHkdfHashType());
    assertEquals(ciphertextSegmentSize, format.getParams().getCiphertextSegmentSize());
    assertEquals(macHashType, format.getParams().getHmacParams().getHash());
    assertEquals(tagSize, format.getParams().getHmacParams().getTagSize());
}

```java:test_tgt

@Test
public void testCreateAesCtrHmacStreamingKeyTemplate() throws Exception {
    int mainKeySize = 42;
    int derivedKeySize = 24;
    int tagSize = 45;
    int ciphertextSegmentSize = 12345;
    HashType hkdfHashType = HashType.SHA512;
    HashType macHashType = HashType.UNKNOWN_HASH;
    KeyTemplate template = StreamingAeadKeyTemplates.createAesCtrHmacStreamingKeyTemplate(mainKeySize, hkdfHashType, derivedKeySize, macHashType, tagSize, ciphertextSegmentSize);
    assertEquals(AesCtrHmacStreamingKeyManager.getKeyType(), template.getTypeUrl());
    assertEquals(OutputPrefixType.RAW, template.getOutputPrefixType());
    AesCtrHmacStreamingKeyFormat format = AesCtrHmacStreamingKeyFormat.parseFrom(template.getValue(), ExtensionRegistryLite.getEmptyRegistry());
    assertEquals(mainKeySize, format.getKeySize());
    assertEquals(derivedKeySize, format.getParams().getDerivedKeySize());
    assertEquals(hkdfHashType, format.getParams().getHkdfHashType());
    assertEquals(ciphertextSegmentSize, format.getParams().getCiphertextSegmentSize());
    assertEquals(macHashType, format.getParams().getHmacParams().getHash());
    assertEquals(tagSize, format.getParams().getHmacParams().getTagSize());
}

```java:llm_gen

@Test
public void testCreateAesCtrHmacStreamingKeyTemplate() throws Exception {
    int mainKeySize = 42;
    int derivedKeySize = 24;
    int tagSize = 45;
    int ciphertextSegmentSize = 12345;
    HashType hkdfHashType = HashType.SHA512;
    HashType macHashType = HashType.UNKNOWN_HASH;
    KeyTemplate template = StreamingAeadKeyTemplates.createAesCtrHmacStreamingKeyTemplate(mainKeySize, hkdfHashType, derivedKeySize, macHashType, tagSize, ciphertextSegmentSize);
    assertEquals(AesCtrHmacStreamingKeyManager.getKeyType(), template.getTypeUrl());
    assertEquals(OutputPrefixType.RAW, template.getOutputPrefixType());
    AesCtrHmacStreamingKeyFormat format = AesCtrHmacStreamingKeyFormat.parseFrom(template.getValue(), ExtensionRegistryLite.getEmptyRegistry());
    assertEquals(mainKeySize, format.getKeySize());
    assertEquals(derivedKeySize, format.getParams().getDerivedKeySize());
    assertEquals(hkdfHashType, format.getParams().getHkdfHashType());
    assertEquals(ciphertextSegmentSize, format.getParams().getCiphertextSegmentSize());
    assertEquals(macHashType, format.getParams().getHmacParams().getHash());
    assertEquals(tagSize, format.getParams().getHmacParams().getTagSize());
}


### 117.Missing Asserts
link: https://github.com/pinpoint-apm/pinpoint/commit/c43f848a205d65cfdc0c94fb91f79e4621837435
p_path: exceptiontrace/exceptiontrace-web/src/main/java/com/navercorp/pinpoint/exceptiontrace/web/model/ExceptionTraceValueView.java#getFieldName
t_path: exceptiontrace/exceptiontrace-web/src/test/java/com/navercorp/pinpoint/exceptiontrace/web/model/ExceptionTraceValueViewTest.java#testGetFieldName

```java:test_src

@Test
void testGetFieldName() {
    ExceptionTraceValueView view = new ExceptionTraceValueView();
    GroupedFieldName emptyFieldName = new GroupedFieldName();
    emptyFieldName.setErrorMessage("");
    view.setGroupedFieldName(emptyFieldName);
    assertEquals("", view.getFieldName());
    GroupedFieldName nullFieldName = new GroupedFieldName();
    view.setGroupedFieldName(nullFieldName);
    assertEquals("total", view.getFieldName());
    view.setGroupedFieldName(null);
    assertEquals("total", view.getFieldName());
}

```java:test_tgt

@Test
void testGetFieldName() {
    ExceptionTraceValueView view = new ExceptionTraceValueView();
    GroupedFieldName emptyFieldName = new GroupedFieldName();
    emptyFieldName.setErrorMessage("");
    view.setGroupedFieldName(emptyFieldName);
    assertEquals(ExceptionTraceValueView.EMPTY_STRING, view.getFieldName());
    GroupedFieldName nullStringFieldName = new GroupedFieldName();
    emptyFieldName.setErrorMessage("null");
    view.setGroupedFieldName(emptyFieldName);
    assertEquals(ExceptionTraceValueView.EMPTY_STRING, view.getFieldName());
    GroupedFieldName nullFieldName = new GroupedFieldName();
    view.setGroupedFieldName(nullFieldName);
    assertEquals(ExceptionTraceValueView.TOTAL_FIELDNAME, view.getFieldName());
    view.setGroupedFieldName(null);
    assertEquals(ExceptionTraceValueView.TOTAL_FIELDNAME, view.getFieldName());
}

```java:llm_gen

@Test
void testGetFieldName() {
    ExceptionTraceValueView view = new ExceptionTraceValueView();
    GroupedFieldName emptyFieldName = new GroupedFieldName();
    emptyFieldName.setErrorMessage("");
    view.setGroupedFieldName(emptyFieldName);
    assertEquals("", view.getFieldName());
    GroupedFieldName nullFieldName = new GroupedFieldName();
    view.setGroupedFieldName(nullFieldName);
    assertEquals("total", view.getFieldName());
    view.setGroupedFieldName(null);
    assertEquals("total", view.getFieldName());
    GroupedFieldName fieldWithEmptyString = new GroupedFieldName();
    fieldWithEmptyString.setErrorMessage(" ");
    view.setGroupedFieldName(fieldWithEmptyString);
    assertEquals("", view.getFieldName());
}

### 118.External Class Modification
link: https://github.com/halo-dev/halo/commit/57fb644173843333b53261524be085827c74dcea
p_path: api/src/main/java/run/halo/app/extension/index/query/QueryFactory.java#notEqual
t_path: api/src/test/java/run/halo/app/extension/index/query/QueryFactoryTest.java#notEqualTest

````java:test_src

@Test
void notEqualTest() {
    var indexView = EmployeeDataSet.createEmployeeIndexView();
    var resultSet = notEqual("lastName", "Fay").matches(indexView);
    assertThat(resultSet).containsExactlyInAnyOrder("101", "102", "103");
}

```java:test_tgt

@Test
void notEqualTest() {
    var indexView = IndexViewDataSet.createEmployeeIndexView();
    var resultSet = notEqual("lastName", "Fay").matches(indexView);
    assertThat(resultSet).containsExactlyInAnyOrder("101", "102", "103");
}

```java:llm_gen

@Test
void notEqualTest() {
    var indexView = EmployeeDataSet.createEmployeeIndexView();
    var resultSet = notEqual("lastName", "Fay").matches(indexView);
    assertThat(resultSet).containsExactlyInAnyOrder("101", "102", "103");

    var nullResultSet = notEqual("lastName", null).matches(indexView);
    assertThat(nullResultSet).containsExactlyInAnyOrder("101", "102", "103", "104");
}

### 119.Test Preparation Error
link: https://github.com/box/mojito/commit/3c5da943ef12edc814d3e9303913f1f78e4dc89a
p_path: webapp/src/main/java/com/box/l10n/mojito/service/sla/DropScheduleService.java#getDropCreatedDate
t_path: webapp/src/test/java/com/box/l10n/mojito/service/sla/DropScheduleServiceTest.java#testGetDropCreatedDate

```java:test_src

@Test
public void testGetDropCreatedDate() {
    DateTime before = new DateTime("2018-06-08T14:00:00.000-07:00", dateTimeZone);
    assertEquals("2018-06-06T20:00:00.000-07:00", dropSchedule.getDropCreatedDate(before).toString());
}

```java:test_tgt

@Test
public void testGetDropCreatedDate() {
    ZonedDateTime before = JSR310Migration.newDateTimeCtorWithStringAndDateTimeZone("2018-06-08T14:00:00.000-07:00", dateTimeZone);
    JSR310MigrationForTesting.junitAssertEqualsDateTime("2018-06-06T20:00:00.000-07:00", dropSchedule.getDropCreatedDate(before).toString());
}

```java:llm_gen

@Test
public void testGetDropCreatedDate() {
    ZonedDateTime before = ZonedDateTime.parse("2018-06-08T14:00:00.000-07:00");
    assertEquals("2018-06-06T20:00:00.000-07:00", dropSchedule.getDropCreatedDate(before).toString());
}

### 120.External Class Modification
link: https://github.com/apache/kafka/commit/bf88013a2812cab65bc70667e451e0a15d26b73c
p_path: group-coordinator/src/main/java/org/apache/kafka/coordinator/group/CoordinatorRecordHelpers.java#newOffsetCommitTombstoneRecord
t_path: group-coordinator/src/test/java/org/apache/kafka/coordinator/group/CoordinatorRecordHelpersTest.java#testNewOffsetCommitTombstoneRecord

```java:test_src

@Test
public void testNewOffsetCommitTombstoneRecord() {
    Record expectedRecord = new Record(new ApiMessageAndVersion(new OffsetCommitKey().setGroup("group-id").setTopic("foo").setPartition(1), (short) 1), null);
    Record record = RecordHelpers.newOffsetCommitTombstoneRecord("group-id", "foo", 1);
    assertEquals(expectedRecord, record);
}

```java:test_tgt

@Test
public void testNewOffsetCommitTombstoneRecord() {
    CoordinatorRecord expectedRecord = new CoordinatorRecord(new ApiMessageAndVersion(new OffsetCommitKey().setGroup("group-id").setTopic("foo").setPartition(1), (short) 1), null);
    CoordinatorRecord record = CoordinatorRecordHelpers.newOffsetCommitTombstoneRecord("group-id", "foo", 1);
    assertEquals(expectedRecord, record);
}

```java:llm_gen

@Test
public void testNewOffsetCommitTombstoneRecord() {
    CoordinatorRecord expectedRecord = new CoordinatorRecord(new ApiMessageAndVersion(new OffsetCommitKey().setGroup("group-id").setTopic("foo").setPartition(1), (short) 1), null);
    CoordinatorRecord record = RecordHelpers.newOffsetCommitTombstoneRecord("group-id", "foo", 1);
    assertEquals(expectedRecord, record);
}

### 121.Correct
link: https://github.com/StarRocks/starrocks/commit/3aa2b039765d8d893b73b61edbf315aeac73be30
p_path: fe/fe-core/src/main/java/com/starrocks/load/routineload/KafkaProgress.java#convertOffset
t_path: fe/fe-core/src/test/java/com/starrocks/load/routineload/KafkaProgressTest.java#testConvertOffset

```java:test_src

@Test
public void testConvertOffset() throws Exception {
    new MockUp<KafkaUtil>() {
        @Mock
        public Map<Integer, Long> getLatestOffsets(String brokerList, String topic, ImmutableMap<String, String> properties, List<Integer> partitions) throws UserException {
            Map<Integer, Long> result = Maps.newHashMap();
            result.put(0, 100L);
            return result;
        }
        @Mock
        public Map<Integer, Long> getBeginningOffsets(String brokerList, String topic, ImmutableMap<String, String> properties, List<Integer> partitions) throws UserException {
            Map<Integer, Long> result = Maps.newHashMap();
            result.put(1, 1L);
            return result;
        }
    };
    KafkaProgress progress = new KafkaProgress();
    // modify offset while paused when partition is not ready
    try {
        List<Pair<Integer, Long>> partitionToOffset = new ArrayList<>();
        partitionToOffset.add(new Pair<>(3, 20L));
        progress.modifyOffset(partitionToOffset);
    } catch (DdlException e) {
        Assert.assertEquals("The specified partition 3 is not in the consumed partitions", e.getMessage());
    }
    progress.addPartitionOffset(new Pair<>(0, -1L));
    progress.addPartitionOffset(new Pair<>(1, -2L));
    progress.addPartitionOffset(new Pair<>(2, 10L));
    progress.addPartitionOffset(new Pair<>(3, 10L));
    progress.convertOffset("127.0.0.1:9020", "topic", Maps.newHashMap());
    List<Pair<Integer, Long>> partitionToOffset = new ArrayList<>();
    partitionToOffset.add(new Pair<>(3, 20L));
    progress.modifyOffset(partitionToOffset);
    Assert.assertEquals(4, partitionToOffset.size());
    Assert.assertEquals(100L, (long) progress.getOffsetByPartition(0));
    Assert.assertEquals(1L, (long) progress.getOffsetByPartition(1));
    Assert.assertEquals(10L, (long) progress.getOffsetByPartition(2));
    Assert.assertEquals(20L, (long) progress.getOffsetByPartition(3));
}

```java:test_tgt

@Test
public void testConvertOffset() throws Exception {
    new MockUp<KafkaUtil>() {
        @Mock
        public Map<Integer, Long> getLatestOffsets(String brokerList, String topic, ImmutableMap<String, String> properties, List<Integer> partitions, long warehouseId) throws UserException {
            Map<Integer, Long> result = Maps.newHashMap();
            result.put(0, 100L);
            return result;
        }
        @Mock
        public Map<Integer, Long> getBeginningOffsets(String brokerList, String topic, ImmutableMap<String, String> properties, List<Integer> partitions, long warehouseId) throws UserException {
            Map<Integer, Long> result = Maps.newHashMap();
            result.put(1, 1L);
            return result;
        }
    };
    KafkaProgress progress = new KafkaProgress();
    // modify offset while paused when partition is not ready
    try {
        List<Pair<Integer, Long>> partitionToOffset = new ArrayList<>();
        partitionToOffset.add(new Pair<>(3, 20L));
        progress.modifyOffset(partitionToOffset);
    } catch (DdlException e) {
        Assert.assertEquals("The specified partition 3 is not in the consumed partitions", e.getMessage());
    }
    progress.addPartitionOffset(new Pair<>(0, -1L));
    progress.addPartitionOffset(new Pair<>(1, -2L));
    progress.addPartitionOffset(new Pair<>(2, 10L));
    progress.addPartitionOffset(new Pair<>(3, 10L));
    progress.convertOffset("127.0.0.1:9020", "topic", Maps.newHashMap(), WarehouseManager.DEFAULT_WAREHOUSE_ID);
    List<Pair<Integer, Long>> partitionToOffset = new ArrayList<>();
    partitionToOffset.add(new Pair<>(3, 20L));
    progress.modifyOffset(partitionToOffset);
    Assert.assertEquals(4, partitionToOffset.size());
    Assert.assertEquals(100L, (long) progress.getOffsetByPartition(0));
    Assert.assertEquals(1L, (long) progress.getOffsetByPartition(1));
    Assert.assertEquals(10L, (long) progress.getOffsetByPartition(2));
    Assert.assertEquals(20L, (long) progress.getOffsetByPartition(3));
}

```java:llm_gen

@Test
public void testConvertOffset() throws Exception {
    new MockUp<KafkaUtil>() {
        @Mock
        public Map<Integer, Long> getLatestOffsets(String brokerList, String topic, ImmutableMap<String, String> properties, List<Integer> partitions, long warehouseId) throws UserException {
            Map<Integer, Long> result = Maps.newHashMap();
            result.put(0, 100L);
            return result;
        }
        @Mock
        public Map<Integer, Long> getBeginningOffsets(String brokerList, String topic, ImmutableMap<String, String> properties, List<Integer> partitions, long warehouseId) throws UserException {
            Map<Integer, Long> result = Maps.newHashMap();
            result.put(1, 1L);
            return result;
        }
    };
    KafkaProgress progress = new KafkaProgress();
    try {
        List<Pair<Integer, Long>> partitionToOffset = new ArrayList<>();
        partitionToOffset.add(new Pair<>(3, 20L));
        progress.modifyOffset(partitionToOffset);
    } catch (DdlException e) {
        Assert.assertEquals("The specified partition 3 is not in the consumed partitions", e.getMessage());
    }
    progress.addPartitionOffset(new Pair<>(0, -1L));
    progress.addPartitionOffset(new Pair<>(1, -2L));
    progress.addPartitionOffset(new Pair<>(2, 10L));
    progress.addPartitionOffset(new Pair<>(3, 10L));
    progress.convertOffset("127.0.0.1:9020", "topic", Maps.newHashMap(), 0L);
    List<Pair<Integer, Long>> partitionToOffset = new ArrayList<>();
    partitionToOffset.add(new Pair<>(3, 20L));
    progress.modifyOffset(partitionToOffset);
    Assert.assertEquals(4, partitionToOffset.size());
    Assert.assertEquals(100L, (long) progress.getOffsetByPartition(0));
    Assert.assertEquals(1L, (long) progress.getOffsetByPartition(1));
    Assert.assertEquals(10L, (long) progress.getOffsetByPartition(2));
    Assert.assertEquals(20L, (long) progress.getOffsetByPartition(3));
}

### 122.Missing Asserts
link: https://github.com/linkedin/venice/commit/49382976f1e5bdd6b280313381cae12267889325
p_path: clients/venice-push-job/src/main/java/com/linkedin/venice/hadoop/input/kafka/VeniceKafkaInputReducer.java#extract
t_path: clients/venice-push-job/src/test/java/com/linkedin/venice/hadoop/input/kafka/TestVeniceKafkaInputReducer.java#testExtract

```java:test_src

@Test(dataProvider = "Two-True-and-False", dataProviderClass = DataProviderUtils.class)
public void testExtract(boolean isChunkingEnabled, boolean valueContainsRmdPayload) {
    byte[] keyBytes = "test_key".getBytes();
    KafkaInputMapperKey mapperKey = new KafkaInputMapperKey();
    mapperKey.key = ByteBuffer.wrap(keyBytes);
    mapperKey.offset = 1;
    RecordSerializer<KafkaInputMapperKey> keySerializer = FastSerializerDeserializerFactory.getFastAvroGenericSerializer(KafkaInputMapperKey.SCHEMA$);
    byte[] serializedMapperKey = keySerializer.serialize(mapperKey);
    BytesWritable keyWritable = new BytesWritable();
    keyWritable.set(serializedMapperKey, 0, serializedMapperKey.length);
    VeniceKafkaInputReducer reducer = new VeniceKafkaInputReducer();
    reducer.setChunkingEnabled(isChunkingEnabled);
    reducer.setSourceVersionCompressor(new NoopCompressor());
    reducer.setDestVersionCompressor(new NoopCompressor());
    List<BytesWritable> values = getValues(Arrays.asList(MapperValueType.PUT, MapperValueType.PUT, MapperValueType.PUT), valueContainsRmdPayload);
    VeniceReducer.VeniceWriterMessage message = reducer.extract(keyWritable, values.iterator(), Mockito.mock(Reporter.class));
    Assert.assertNotNull(message);
    Assert.assertEquals(message.getKeyBytes(), keyBytes);
    Assert.assertEquals(message.getValueBytes(), (VALUE_PREFIX + 2).getBytes());
    Assert.assertEquals(message.getValueSchemaId(), 1);
    Assert.assertEquals(message.getRmdVersionId(), valueContainsRmdPayload ? 1 : -1);
    values = getValues(Arrays.asList(MapperValueType.PUT, MapperValueType.PUT, MapperValueType.DELETE), valueContainsRmdPayload);
    message = reducer.extract(keyWritable, values.iterator(), Mockito.mock(Reporter.class));
    if (valueContainsRmdPayload) {
        Assert.assertNotNull(message);
    } else {
        Assert.assertNull(message);
    }
    values = getValues(Arrays.asList(MapperValueType.PUT, MapperValueType.DELETE, MapperValueType.PUT), valueContainsRmdPayload);
    message = reducer.extract(keyWritable, values.iterator(), Mockito.mock(Reporter.class));
    Assert.assertNotNull(message);
    Assert.assertEquals(message.getKeyBytes(), keyBytes);
    Assert.assertEquals(message.getValueBytes(), (VALUE_PREFIX + 2).getBytes());
    Assert.assertEquals(message.getValueSchemaId(), 1);
    Assert.assertEquals(message.getRmdVersionId(), valueContainsRmdPayload ? 1 : -1);
}

```java:test_tgt

@Test(dataProvider = "Two-True-and-False", dataProviderClass = DataProviderUtils.class)
public void testExtract(boolean isChunkingEnabled, boolean valueContainsRmdPayload) {
    byte[] keyBytes = "test_key".getBytes();
    KafkaInputMapperKey mapperKey = new KafkaInputMapperKey();
    mapperKey.key = ByteBuffer.wrap(keyBytes);
    mapperKey.offset = 1;
    RecordSerializer<KafkaInputMapperKey> keySerializer = FastSerializerDeserializerFactory.getFastAvroGenericSerializer(KafkaInputMapperKey.SCHEMA$);
    byte[] serializedMapperKey = keySerializer.serialize(mapperKey);
    VeniceKafkaInputReducer reducer = new VeniceKafkaInputReducer();
    reducer.setChunkingEnabled(isChunkingEnabled);
    reducer.setSourceVersionCompressor(new NoopCompressor());
    reducer.setDestVersionCompressor(new NoopCompressor());
    List<byte[]> values = getValues(Arrays.asList(MapperValueType.PUT, MapperValueType.PUT, MapperValueType.PUT), valueContainsRmdPayload);
    AbstractPartitionWriter.VeniceWriterMessage message = reducer.extract(serializedMapperKey, values.iterator(), new ReporterBackedMapReduceDataWriterTaskTracker(Mockito.mock(Reporter.class)));
    Assert.assertNotNull(message);
    Assert.assertEquals(message.getKeyBytes(), keyBytes);
    Assert.assertEquals(message.getValueBytes(), (VALUE_PREFIX + 2).getBytes());
    Assert.assertEquals(message.getValueSchemaId(), 1);
    Assert.assertEquals(message.getRmdVersionId(), valueContainsRmdPayload ? 1 : -1);
    values = getValues(Arrays.asList(MapperValueType.PUT, MapperValueType.PUT, MapperValueType.DELETE), valueContainsRmdPayload);
    message = reducer.extract(serializedMapperKey, values.iterator(), new ReporterBackedMapReduceDataWriterTaskTracker(Mockito.mock(Reporter.class)));
    if (valueContainsRmdPayload) {
        Assert.assertNotNull(message);
    } else {
        Assert.assertNull(message);
    }
    values = getValues(Arrays.asList(MapperValueType.PUT, MapperValueType.DELETE, MapperValueType.PUT), valueContainsRmdPayload);
    message = reducer.extract(serializedMapperKey, values.iterator(), new ReporterBackedMapReduceDataWriterTaskTracker(Mockito.mock(Reporter.class)));
    Assert.assertNotNull(message);
    Assert.assertEquals(message.getKeyBytes(), keyBytes);
    Assert.assertEquals(message.getValueBytes(), (VALUE_PREFIX + 2).getBytes());
    Assert.assertEquals(message.getValueSchemaId(), 1);
    Assert.assertEquals(message.getRmdVersionId(), valueContainsRmdPayload ? 1 : -1);
}

```java:llm_gen

@Test(dataProvider = "Two-True-and-False", dataProviderClass = DataProviderUtils.class)
public void testExtract(boolean isChunkingEnabled, boolean valueContainsRmdPayload) {
    byte[] keyBytes = "test_key".getBytes();
    KafkaInputMapperKey mapperKey = new KafkaInputMapperKey();
    mapperKey.key = ByteBuffer.wrap(keyBytes);
    mapperKey.offset = 1;
    RecordSerializer<KafkaInputMapperKey> keySerializer = FastSerializerDeserializerFactory.getFastAvroGenericSerializer(KafkaInputMapperKey.SCHEMA$);
    byte[] serializedMapperKey = keySerializer.serialize(mapperKey);
    BytesWritable keyWritable = new BytesWritable();
    keyWritable.set(serializedMapperKey, 0, serializedMapperKey.length);
    VeniceKafkaInputReducer reducer = new VeniceKafkaInputReducer();
    reducer.setChunkingEnabled(isChunkingEnabled);
    reducer.setSourceVersionCompressor(new NoopCompressor());
    reducer.setDestVersionCompressor(new NoopCompressor());
    List<BytesWritable> values = getValues(Arrays.asList(MapperValueType.PUT, MapperValueType.PUT, MapperValueType.PUT), valueContainsRmdPayload);
    AbstractPartitionWriter.VeniceWriterMessage message = reducer.extract(keyBytes, values.iterator(), Mockito.mock(DataWriterTaskTracker.class));
    Assert.assertNotNull(message);
    Assert.assertEquals(message.getKeyBytes(), keyBytes);
    Assert.assertEquals(message.getValueBytes(), (VALUE_PREFIX + 2).getBytes());
    Assert.assertEquals(message.getValueSchemaId(), 1);
    Assert.assertEquals(message.getRmdVersionId(), valueContainsRmdPayload ? 1 : -1);
    values = getValues(Arrays.asList(MapperValueType.PUT, MapperValueType.PUT, MapperValueType.DELETE), valueContainsRmdPayload);
    message = reducer.extract(keyBytes, values.iterator(), Mockito.mock(DataWriterTaskTracker.class));
    if (valueContainsRmdPayload) {
        Assert.assertNotNull(message);
    } else {
        Assert.assertNull(message);
    }
    values = getValues(Arrays.asList(MapperValueType.PUT, MapperValueType.DELETE, MapperValueType.PUT), valueContainsRmdPayload);
    message = reducer.extract(keyBytes, values.iterator(), Mockito.mock(DataWriterTaskTracker.class));
    Assert.assertNotNull(message);
    Assert.assertEquals(message.getKeyBytes(), keyBytes);
    Assert.assertEquals(message.getValueBytes(), (VALUE_PREFIX + 2).getBytes());
    Assert.assertEquals(message.getValueSchemaId(), 1);
    Assert.assertEquals(message.getRmdVersionId(), valueContainsRmdPayload ? 1 : -1);
}

### 123.External File Modification
link: https://github.com/thingsboard/thingsboard/commit/f43263580078b5bc39e3969e1c8e86ac8a1f4918
p_path: application/src/main/java/org/thingsboard/server/controller/TbResourceController.java#getLwm2mListObjects
t_path: application/src/test/java/org/thingsboard/server/controller/TbResourceControllerTest.java#testGetLwm2mListObjects

```java:test_src

@Test
public void testGetLwm2mListObjects() throws Exception {
    loginTenantAdmin();
    List<TbResource> resources = loadLwm2mResources();
    List<LwM2mObject> objects = doGetTyped("/api/resource/lwm2m?sortProperty=id&sortOrder=ASC&objectIds=3_1.0,5_1.0,19_1.1", new TypeReference<>() {
    });
    Assert.assertNotNull(objects);
    Assert.assertEquals(3, objects.size());
    removeLoadResources(resources);
}

```java:test_tgt

@Test
public void testGetLwm2mListObjects() throws Exception {
    loginTenantAdmin();
    List<TbResource> resources = loadLwm2mResources();
    List<LwM2mObject> objects = doGetTyped("/api/resource/lwm2m?sortProperty=id&sortOrder=ASC&objectIds=3_1.2,5_1.2,19_1.1", new TypeReference<>() {
    });
    Assert.assertNotNull(objects);
    Assert.assertEquals(3, objects.size());
    removeLoadResources(resources);
}

```java:llm_gen

@Test
public void testGetLwm2mListObjects() throws Exception {
    loginTenantAdmin();
    List<TbResource> resources = loadLwm2mResources();
    List<LwM2mObject> objects = doGetTyped("/api/resource/lwm2m?sortProperty=id&sortOrder=ASC&objectIds=3_1.0,5_1.0,19_1.1", new TypeReference<>() {
    });
    Assert.assertNotNull(objects);
    Assert.assertEquals(3, objects.size());
    removeLoadResources(resources);
}

### 124.External Class Modification
link: https://github.com/apache/commons-collections/commit/56da86956588b45280938180b40eb3aac1d16a86
p_path: src/main/java/org/apache/commons/collections4/bloomfilter/LayerManager.java#neverAdvance
t_path: src/test/java/org/apache/commons/collections4/bloomfilter/LayerManagerTest.java#testNeverAdvance

```java:test_src

@Test
public void testNeverAdvance() {
    Predicate<LayerManager> underTest = LayerManager.ExtendCheck.neverAdvance();
    LayerManager layerManager = testingBuilder().build();
    assertFalse(underTest.test(layerManager));
    for (int i = 0; i < 10; i++) {
        layerManager.getTarget().merge(TestingHashers.randomHasher());
        assertFalse(underTest.test(layerManager));
    }
}

```java:test_tgt

@Test
public void testNeverAdvance() {
    Predicate<LayerManager<BloomFilter>> underTest = LayerManager.ExtendCheck.neverAdvance();
    LayerManager<BloomFilter> layerManager = testingBuilder().build();
    assertFalse(underTest.test(layerManager));
    for (int i = 0; i < 10; i++) {
        layerManager.getTarget().merge(TestingHashers.randomHasher());
        assertFalse(underTest.test(layerManager));
    }
}

```java:llm_gen

@Test
public void testNeverAdvance() {
    Predicate<LayerManager<BloomFilter>> underTest = LayerManager.neverAdvance();
    LayerManager<BloomFilter> layerManager = testingBuilder().build();
    assertFalse(underTest.test(layerManager));
    for (int i = 0; i < 10; i++) {
        layerManager.getTarget().merge(TestingHashers.randomHasher());
        assertFalse(underTest.test(layerManager));
    }
}

### 125.Field/Package Information Modification
link: https://github.com/pentaho/pentaho-platform/commit/32aa5ab0017440e4088dd9027872c193b0df4928
p_path: extensions/src/main/java/org/pentaho/platform/web/http/api/resources/UserRoleListResource.java#getUsers
t_path: extensions/src/test/java/org/pentaho/platform/web/http/api/resources/UserRoleListResourceTest.java#testGetUsers

```java:test_src

@Test
public void testGetUsers() throws Exception {
    UserListWrapper mockWrapper = mock(UserListWrapper.class);
    doReturn(mockWrapper).when(userRoleListResource.userRoleListService).getUsers();
    UserListWrapper testWrapper = userRoleListResource.getUsers();
    assertEquals(mockWrapper, testWrapper);
    verify(userRoleListResource.userRoleListService, times(1)).getUsers();
}

```java:test_tgt

@Test
public void testGetUsers() throws Exception {
    UserListWrapper mockWrapper = mock(UserListWrapper.class);
    doReturn(mockWrapper).when(userRoleListServiceMock).getUsers();
    UserListWrapper testWrapper = userRoleListResource.getUsers();
    assertEquals(mockWrapper, testWrapper);
    verify(userRoleListServiceMock, times(1)).getUsers();
}

```java:llm_gen

@Test
public void testGetUsers() {
    UserListWrapper mockWrapper = mock(UserListWrapper.class);
    doReturn(mockWrapper).when(userRoleListResource.userRoleListService).getUsers();
    UserListWrapper testWrapper = userRoleListResource.getUsers();
    assertEquals(mockWrapper, testWrapper);
    verify(userRoleListResource.userRoleListService, times(1)).getUsers();
}

### 126.Missing Asserts
link: https://github.com/DataSystemsLab/GeoSpark/commit/3f4697ac7c1583160f0aa19a02be79bba6a4f24c
p_path: common/src/main/java/org/apache/sedona/common/Functions.java#bestSRID
t_path: common/src/test/java/org/apache/sedona/common/FunctionsTest.java#testBestSRID

```java:test_src

@Test
public void testBestSRID() {
    int[][] testCases_special = { { 0, -70, 3409 }, { 0, 70, 3574 }, { -180, 60, 32660 }, { 180, 60, 32660 }, { -180, -60, 32760 }, { 180, -60, 32760 } };
    int numZones = (177 - (-177)) / 6 + 1;
    int numZonesSouth = (177 - (-177)) / 6 + 1;
    int[][] testCases_UTMNorth = new int[numZones][3];
    int[][] testCases_UTMSouth = new int[numZonesSouth][3];
    int indexNorth = 0;
    int northernLat = 60;
    for (int lon = -177, epsg = 32601; lon <= 177; lon += 6, epsg++) {
        testCases_UTMNorth[indexNorth][0] = lon;
        testCases_UTMNorth[indexNorth][1] = northernLat;
        testCases_UTMNorth[indexNorth][2] = epsg;
        indexNorth++;
    }
    int indexSouth = 0;
    int southernLat = -60;
    for (int lon = -177, epsg = 32701; lon <= 177; lon += 6, epsg++) {
        testCases_UTMSouth[indexSouth][0] = lon;
        testCases_UTMSouth[indexSouth][1] = southernLat;
        testCases_UTMSouth[indexSouth][2] = epsg;
        indexSouth++;
    }
    for (int[] testCase : testCases_special) {
        Geometry geom = GEOMETRY_FACTORY.createPoint(new Coordinate(testCase[0], testCase[1]));
        int actualEPSG = Functions.bestSRID(geom);
        int expectedEPSG = testCase[2];
        assertEquals("Failed at coordinates (" + testCase[0] + ", " + testCase[1] + ")", expectedEPSG, actualEPSG);
    }
    for (int[] testCase : testCases_UTMNorth) {
        Geometry geom = GEOMETRY_FACTORY.createPoint(new Coordinate(testCase[0], testCase[1]));
        int actualEPSG = Functions.bestSRID(geom);
        int expectedEPSG = testCase[2];
        assertEquals("Failed at coordinates (" + testCase[0] + ", " + testCase[1] + ")", expectedEPSG, actualEPSG);
    }
    for (int[] testCase : testCases_UTMSouth) {
        Geometry geom = GEOMETRY_FACTORY.createPoint(new Coordinate(testCase[0], testCase[1]));
        int actualEPSG = Functions.bestSRID(geom);
        int expectedEPSG = testCase[2];
        assertEquals("Failed at coordinates (" + testCase[0] + ", " + testCase[1] + ")", expectedEPSG, actualEPSG);
    }
    Geometry geom = GEOMETRY_FACTORY.createPolygon(new Coordinate[] { new Coordinate(-160, -40), new Coordinate(-160, 40), new Coordinate(160, 40), new Coordinate(160, -40), new Coordinate(-160, -40) });
    int expectedEPSG = 3395;
    int actualEPSG = Functions.bestSRID(geom);
    assertEquals("Expected World Mercator projection for wide range geometry", expectedEPSG, actualEPSG);
}

```java:test_tgt

@Test
public void testBestSRID() throws ParseException {
    int[][] testCases_special = { { 0, -70, 3409 }, { 0, 70, 3574 }, { -180, 60, 32660 }, { 180, 60, 32660 }, { -180, -60, 32760 }, { 180, -60, 32760 } };
    int numZones = (177 - (-177)) / 6 + 1;
    int numZonesSouth = (177 - (-177)) / 6 + 1;
    int[][] testCases_UTMNorth = new int[numZones][3];
    int[][] testCases_UTMSouth = new int[numZonesSouth][3];
    int indexNorth = 0;
    int northernLat = 60;
    for (int lon = -177, epsg = 32601; lon <= 177; lon += 6, epsg++) {
        testCases_UTMNorth[indexNorth][0] = lon;
        testCases_UTMNorth[indexNorth][1] = northernLat;
        testCases_UTMNorth[indexNorth][2] = epsg;
        indexNorth++;
    }
    int indexSouth = 0;
    int southernLat = -60;
    for (int lon = -177, epsg = 32701; lon <= 177; lon += 6, epsg++) {
        testCases_UTMSouth[indexSouth][0] = lon;
        testCases_UTMSouth[indexSouth][1] = southernLat;
        testCases_UTMSouth[indexSouth][2] = epsg;
        indexSouth++;
    }
    for (int[] testCase : testCases_special) {
        Geometry geom = GEOMETRY_FACTORY.createPoint(new Coordinate(testCase[0], testCase[1]));
        int actualEPSG = Functions.bestSRID(geom);
        System.out.println("actualEPSG: " + actualEPSG);
        int expectedEPSG = testCase[2];
        assertEquals("Failed at coordinates (" + testCase[0] + ", " + testCase[1] + ")", expectedEPSG, actualEPSG);
    }
    for (int[] testCase : testCases_UTMNorth) {
        Geometry geom = GEOMETRY_FACTORY.createPoint(new Coordinate(testCase[0], testCase[1]));
        int actualEPSG = Functions.bestSRID(geom);
        int expectedEPSG = testCase[2];
        assertEquals("Failed at coordinates (" + testCase[0] + ", " + testCase[1] + ")", expectedEPSG, actualEPSG);
    }
    for (int[] testCase : testCases_UTMSouth) {
        Geometry geom = GEOMETRY_FACTORY.createPoint(new Coordinate(testCase[0], testCase[1]));
        int actualEPSG = Functions.bestSRID(geom);
        int expectedEPSG = testCase[2];
        assertEquals("Failed at coordinates (" + testCase[0] + ", " + testCase[1] + ")", expectedEPSG, actualEPSG);
    }
    Geometry geom = GEOMETRY_FACTORY.createPolygon(new Coordinate[] { new Coordinate(-160, -40), new Coordinate(-160, 40), new Coordinate(160, 40), new Coordinate(160, -40), new Coordinate(-160, -40) });
    int expectedEPSG = 3395;
    int actualEPSG = Functions.bestSRID(geom);
    assertEquals("Expected World Mercator projection for wide range geometry", expectedEPSG, actualEPSG);
}

```java:llm_gen

@Test
public void testBestSRID() {
    int[][] testCases_special = { { 0, -70, 3409 }, { 0, 70, 3574 }, { -180, 60, 32660 }, { 180, 60, 32660 }, { -180, -60, 32760 }, { 180, -60, 32760 } };
    int numZones = (177 - (-177)) / 6 + 1;
    int numZonesSouth = (177 - (-177)) / 6 + 1;
    int[][] testCases_UTMNorth = new int[numZones][3];
    int[][] testCases_UTMSouth = new int[numZonesSouth][3];
    int indexNorth = 0;
    int northernLat = 60;
    for (int lon = -177, epsg = 32601; lon <= 177; lon += 6, epsg++) {
        testCases_UTMNorth[indexNorth][0] = lon;
        testCases_UTMNorth[indexNorth][1] = northernLat;
        testCases_UTMNorth[indexNorth][2] = epsg;
        indexNorth++;
    }
    int indexSouth = 0;
    int southernLat = -60;
    for (int lon = -177, epsg = 32701; lon <= 177; lon += 6, epsg++) {
        testCases_UTMSouth[indexSouth][0] = lon;
        testCases_UTMSouth[indexSouth][1] = southernLat;
        testCases_UTMSouth[indexSouth][2] = epsg;
        indexSouth++;
    }
    for (int[] testCase : testCases_special) {
        Geometry geom = GEOMETRY_FACTORY.createPoint(new Coordinate(testCase[0], testCase[1]));
        int actualEPSG = Functions.bestSRID(geom);
        int expectedEPSG = testCase[2];
        assertEquals("Failed at coordinates (" + testCase[0] + ", " + testCase[1] + ")", expectedEPSG, actualEPSG);
    }
    for (int[] testCase : testCases_UTMNorth) {
        Geometry geom = GEOMETRY_FACTORY.createPoint(new Coordinate(testCase[0], testCase[1]));
        int actualEPSG = Functions.bestSRID(geom);
        int expectedEPSG = testCase[2];
        assertEquals("Failed at coordinates (" + testCase[0] + ", " + testCase[1] + ")", expectedEPSG, actualEPSG);
    }
    for (int[] testCase : testCases_UTMSouth) {
        Geometry geom = GEOMETRY_FACTORY.createPoint(new Coordinate(testCase[0], testCase[1]));
        int actualEPSG = Functions.bestSRID(geom);
        int expectedEPSG = testCase[2];
        assertEquals("Failed at coordinates (" + testCase[0] + ", " + testCase[1] + ")", expectedEPSG, actualEPSG);
    }
    Geometry geom = GEOMETRY_FACTORY.createPolygon(new Coordinate[] { new Coordinate(-160, -40), new Coordinate(-160, 40), new Coordinate(160, 40), new Coordinate(160, -40), new Coordinate(-160, -40) });
    int expectedEPSG = 3395;
    int actualEPSG = Functions.bestSRID(geom);
    assertEquals("Expected World Mercator projection for wide range geometry", expectedEPSG, actualEPSG);

    // Test for NaN handling
    Geometry nanGeom = GEOMETRY_FACTORY.createPoint(new Coordinate(Double.NaN, Double.NaN));
    assertThrows(IllegalArgumentException.class, () -> Functions.bestSRID(nanGeom));
}


### 127.Correct
link: https://github.com/GoogleCloudPlatform/DataflowTemplates/commit/9796144ea0436a39cb073da91a445c2916a75fe9
p_path: v2/spanner-common/src/main/java/com/google/cloud/teleport/v2/spanner/migrations/schema/IdentityMapper.java#getSpannerColumns
t_path: v2/spanner-common/src/test/java/com/google/cloud/teleport/v2/spanner/migrations/schema/IdentityMapperTest.java#testGetSpannerColumns

```java:test_src

@Test
public void testGetSpannerColumns() {
    String spannerTable = "Users";
    List<String> expectedColumns = Arrays.asList("id", "first_name", "last_name");
    List<String> result = mapper.getSpannerColumns(spannerTable);
    assertEquals(expectedColumns, result);
}

```java:test_tgt

@Test
public void testGetSpannerColumns() {
    String spannerTable = "Users";
    List<String> expectedColumns = Arrays.asList("id", "first_name", "last_name");
    List<String> result = mapper.getSpannerColumns("", spannerTable);
    assertEquals(expectedColumns, result);
}

```java:llm_gen

@Test
public void testGetSpannerColumns() {
    String namespace = "test_namespace";
    String spannerTable = "Users";
    List<String> expectedColumns = Arrays.asList("id", "first_name", "last_name");
    List<String> result = mapper.getSpannerColumns(namespace, spannerTable);
    assertEquals(expectedColumns, result);
}

### 128.Test Preparation Error
link: https://github.com/box/mojito/commit/3c5da943ef12edc814d3e9303913f1f78e4dc89a
p_path: webapp/src/main/java/com/box/l10n/mojito/service/sla/DropScheduleService.java#getLastDropCreatedDate
t_path: webapp/src/test/java/com/box/l10n/mojito/service/sla/DropScheduleServiceTest.java#testGetLastDropCreatedDate

```java:test_src

@Test
public void testGetLastDropCreatedDate() {
    DateTime now = new DateTime("2018-06-08T14:00:00.000-07:00", dateTimeZone);
    doReturn(now).when(dateTimeUtils).now(dateTimeZone);
    DateTime expResult = new DateTime("2018-06-06T20:00:00.000-07:00", dateTimeZone);
    DateTime result = dropSchedule.getLastDropCreatedDate();
    assertEquals(expResult, result);
}

```java:test_tgt

@Test
public void testGetLastDropCreatedDate() {
    ZonedDateTime now = JSR310Migration.newDateTimeCtorWithStringAndDateTimeZone("2018-06-08T14:00:00.000-07:00", dateTimeZone);
    doReturn(now).when(dateTimeUtils).now(dateTimeZone);
    ZonedDateTime expResult = JSR310Migration.newDateTimeCtorWithStringAndDateTimeZone("2018-06-06T20:00:00.000-07:00", dateTimeZone);
    ZonedDateTime result = dropSchedule.getLastDropCreatedDate();
    JSR310MigrationForTesting.junitAssertEquals(expResult, result);
}

```java:llm_gen

@Test
public void testGetLastDropCreatedDate() {
    ZonedDateTime now = ZonedDateTime.parse("2018-06-08T14:00:00.000-07:00");
    doReturn(now).when(dateTimeUtils).now(dropScheduleConfig.getTimezone());
    ZonedDateTime expResult = ZonedDateTime.parse("2018-06-06T20:00:00.000-07:00");
    ZonedDateTime result = dropSchedule.getLastDropCreatedDate();
    assertEquals(expResult, result);
}

### 129.Missing Asserts
link: https://github.com/apache/kafka/commit/4e0578fb814e99da2a8f4d6adc123fe87c8f24f3
p_path: clients/src/main/java/org/apache/kafka/clients/consumer/internals/AsyncKafkaConsumer.java#offsetsForTimes
t_path: clients/src/test/java/org/apache/kafka/clients/consumer/internals/AsyncKafkaConsumerTest.java#testOffsetsForTimes

```java:test_src

@Test
public void testOffsetsForTimes() {
    consumer = newConsumer();
    Map<TopicPartition, OffsetAndTimestamp> expectedResult = mockOffsetAndTimestamp();
    Map<TopicPartition, Long> timestampToSearch = mockTimestampToSearch();
    doReturn(expectedResult).when(applicationEventHandler).addAndGet(any(), any());
    Map<TopicPartition, OffsetAndTimestamp> result = assertDoesNotThrow(() -> consumer.offsetsForTimes(timestampToSearch, Duration.ofMillis(1)));
    assertEquals(expectedResult, result);
    verify(applicationEventHandler).addAndGet(ArgumentMatchers.isA(ListOffsetsEvent.class), ArgumentMatchers.isA(Timer.class));
}

```java:test_tgt

@Test
public void testOffsetsForTimes() {
    consumer = newConsumer();
    Map<TopicPartition, OffsetAndTimestampInternal> expectedResult = mockOffsetAndTimestamp();
    Map<TopicPartition, Long> timestampToSearch = mockTimestampToSearch();
    doReturn(expectedResult).when(applicationEventHandler).addAndGet(any(), any());
    Map<TopicPartition, OffsetAndTimestamp> result = assertDoesNotThrow(() -> consumer.offsetsForTimes(timestampToSearch, Duration.ofMillis(1)));
    expectedResult.forEach((key, value) -> {
        OffsetAndTimestamp expected = value.buildOffsetAndTimestamp();
        assertEquals(expected, result.get(key));
    });
    verify(applicationEventHandler).addAndGet(ArgumentMatchers.isA(ListOffsetsEvent.class), ArgumentMatchers.isA(Timer.class));
}

```java:llm_gen

@Test
public void testOffsetsForTimes() {
    consumer = newConsumer();
    Map<TopicPartition, OffsetAndTimestamp> expectedResult = mockOffsetAndTimestamp();
    Map<TopicPartition, Long> timestampToSearch = mockTimestampToSearch();
    Map<TopicPartition, ListOffsetsEvent.ListOffsetsResult> mockResults = new HashMap<>();
    expectedResult.forEach((k, v) -> mockResults.put(k, new ListOffsetsEvent.ListOffsetsResult(v)));
    doReturn(mockResults).when(applicationEventHandler).addAndGet(any(), any());
    Map<TopicPartition, OffsetAndTimestamp> result = assertDoesNotThrow(() -> consumer.offsetsForTimes(timestampToSearch, Duration.ofMillis(1)));
    assertEquals(expectedResult, result);
    verify(applicationEventHandler).addAndGet(ArgumentMatchers.isA(ListOffsetsEvent.class), ArgumentMatchers.isA(Timer.class));
}

### 130.Correct
link: https://github.com/StarRocks/starrocks/commit/45207d8c1e04e7a78434cef4fbeebbeb735f66e4
p_path: fe/fe-core/src/main/java/com/starrocks/connector/iceberg/IcebergMetadata.java#listPartitionNames
t_path: fe/fe-core/src/test/java/com/starrocks/connector/iceberg/IcebergMetadataTest.java#testListPartitionNames

```java:test_src

@Test
public void testListPartitionNames() {
    mockedNativeTableB.newAppend().appendFile(FILE_B_1).appendFile(FILE_B_2).appendFile(FILE_B_3).commit();
    new MockUp<IcebergHiveCatalog>() {
        @Mock
        org.apache.iceberg.Table getTable(String dbName, String tableName) throws StarRocksConnectorException {
            return mockedNativeTableB;
        }
    };
    IcebergHiveCatalog icebergHiveCatalog = new IcebergHiveCatalog(CATALOG_NAME, new Configuration(), DEFAULT_CONFIG);
    CachingIcebergCatalog cachingIcebergCatalog = new CachingIcebergCatalog(CATALOG_NAME, icebergHiveCatalog, DEFAULT_CATALOG_PROPERTIES, Executors.newSingleThreadExecutor());
    IcebergMetadata metadata = new IcebergMetadata(CATALOG_NAME, HDFS_ENVIRONMENT, cachingIcebergCatalog, Executors.newSingleThreadExecutor(), Executors.newSingleThreadExecutor());
    List<String> partitionNames = metadata.listPartitionNames("db", "table");
    Assert.assertEquals(2, partitionNames.size());
    Assert.assertTrue(partitionNames.contains("k2=2"));
    Assert.assertTrue(partitionNames.contains("k2=3"));
}

```java:test_tgt

@Test
public void testListPartitionNames() {
    mockedNativeTableB.newAppend().appendFile(FILE_B_1).appendFile(FILE_B_2).appendFile(FILE_B_3).commit();
    new MockUp<IcebergHiveCatalog>() {
        @Mock
        org.apache.iceberg.Table getTable(String dbName, String tableName) throws StarRocksConnectorException {
            return mockedNativeTableB;
        }
    };
    IcebergHiveCatalog icebergHiveCatalog = new IcebergHiveCatalog(CATALOG_NAME, new Configuration(), DEFAULT_CONFIG);
    CachingIcebergCatalog cachingIcebergCatalog = new CachingIcebergCatalog(CATALOG_NAME, icebergHiveCatalog, DEFAULT_CATALOG_PROPERTIES, Executors.newSingleThreadExecutor());
    IcebergMetadata metadata = new IcebergMetadata(CATALOG_NAME, HDFS_ENVIRONMENT, cachingIcebergCatalog, Executors.newSingleThreadExecutor(), Executors.newSingleThreadExecutor());
    List<String> partitionNames = metadata.listPartitionNames("db", "table", -1);
    Assert.assertEquals(2, partitionNames.size());
    Assert.assertTrue(partitionNames.contains("k2=2"));
    Assert.assertTrue(partitionNames.contains("k2=3"));
}

```java:llm_gen

@Test
public void testListPartitionNames() {
    mockedNativeTableB.newAppend().appendFile(FILE_B_1).appendFile(FILE_B_2).appendFile(FILE_B_3).commit();
    new MockUp<IcebergHiveCatalog>() {
        @Mock
        org.apache.iceberg.Table getTable(String dbName, String tableName) throws StarRocksConnectorException {
            return mockedNativeTableB;
        }
    };
    IcebergHiveCatalog icebergHiveCatalog = new IcebergHiveCatalog(CATALOG_NAME, new Configuration(), DEFAULT_CONFIG);
    CachingIcebergCatalog cachingIcebergCatalog = new CachingIcebergCatalog(CATALOG_NAME, icebergHiveCatalog, DEFAULT_CATALOG_PROPERTIES, Executors.newSingleThreadExecutor());
    IcebergMetadata metadata = new IcebergMetadata(CATALOG_NAME, HDFS_ENVIRONMENT, cachingIcebergCatalog, Executors.newSingleThreadExecutor(), Executors.newSingleThreadExecutor());
    List<String> partitionNames = metadata.listPartitionNames("db", "table", 1L);
    Assert.assertEquals(2, partitionNames.size());
    Assert.assertTrue(partitionNames.contains("k2=2"));
    Assert.assertTrue(partitionNames.contains("k2=3"));
}

### 131.External Class Modification
link: https://github.com/weibocom/motan/commit/a5d969c1f45a862db9a7406cc79fdd147a963488
p_path: motan-extension/protocol-extension/motan-protocol-yar/src/main/java/com/weibo/api/motan/transport/netty4/yar/YarMessageHandlerWrapper.java#handle
t_path: motan-extension/protocol-extension/motan-protocol-yar/src/test/java/com/weibo/api/motan/transport/netty4/yar/YarMessageHandlerWrapperTest.java#testHandle

```java:test_src

@Test
public void testHandle() throws Exception {
    YarRequest yarRequest = new YarRequest(123, "JSON", "testmethod", new Object[] { "params", 456 });
    final YarResponse yarResponse = YarProtocolUtil.buildDefaultErrorResponse("test err", "JSON");
    YarMessageHandlerWarpper handler = new YarMessageHandlerWarpper(new YarMessageRouter() {
        @Override
        public Object handle(Channel channel, Object message) {
            AttachmentRequest request = (AttachmentRequest) message;
            verifyAttachments(request.getAttachments());
            return yarResponse;
        }
    });
    FullHttpResponse httpResponse = (FullHttpResponse) handler.handle(new MockChannel(), buildHttpRequest(yarRequest, uri));
    assertNotNull(httpResponse);
    assertNotNull(httpResponse.content());
    YarResponse retYarResponse = getYarResponse(httpResponse);
    assertNotNull(retYarResponse);
    assertEquals(yarResponse, retYarResponse);
}

```java:test_tgt

@Test
public void testHandle() throws Exception {
    YarRequest yarRequest = new YarRequest(123, "JSON", "testMethod", new Object[] { "params", 456 });
    final YarResponse yarResponse = YarProtocolUtil.buildDefaultErrorResponse("test err", "JSON");
    YarMessageHandlerWrapper handler = new YarMessageHandlerWrapper(new YarMessageRouter() {
        @Override
        public Object handle(Channel channel, Object message) {
            AttachmentRequest request = (AttachmentRequest) message;
            verifyAttachments(request.getAttachments());
            return yarResponse;
        }
    });
    FullHttpResponse httpResponse = handler.handle(new MockChannel(), buildHttpRequest(yarRequest, uri));
    assertNotNull(httpResponse);
    assertNotNull(httpResponse.content());
    YarResponse retYarResponse = getYarResponse(httpResponse);
    assertNotNull(retYarResponse);
    assertEquals(yarResponse, retYarResponse);
}

```java:llm_gen

@Test
public void testHandle() throws Exception {
    YarRequest yarRequest = new YarRequest(123, "JSON", "testmethod", new Object[] { "params", 456 });
    final YarResponse yarResponse = YarProtocolUtil.buildDefaultErrorResponse("test err", "JSON");
    YarMessageHandlerWrapper handler = new YarMessageHandlerWrapper(new YarMessageRouter() {
        @Override
        public Object handle(Channel channel, Object message) {
            AttachmentRequest request = (AttachmentRequest) message;
            verifyAttachments(request.getAttachments());
            return yarResponse;
        }
    });
    FullHttpResponse httpResponse = (FullHttpResponse) handler.handle(new MockChannel(), buildHttpRequest(yarRequest, uri));
    assertNotNull(httpResponse);
    assertNotNull(httpResponse.content());
    YarResponse retYarResponse = getYarResponse(httpResponse);
    assertNotNull(retYarResponse);
    assertEquals(yarResponse, retYarResponse);
}

### 132.Missing Asserts
link: https://github.com/apache/incubator-uniffle/commit/25d0585ddf6154e52ef01a7cbf9eb24809b7e585
p_path: client-spark/spark2/src/main/java/org/apache/spark/shuffle/writer/RssShuffleWriter.java#checkBlockSendResult
t_path: client-spark/spark3/src/test/java/org/apache/spark/shuffle/writer/RssShuffleWriterTest.java#checkBlockSendResultTest

```java:test_src

@Test
public void checkBlockSendResultTest() {
    SparkConf conf = new SparkConf();
    conf.setAppName("testApp").setMaster("local[2]").set(RssSparkConfig.RSS_TEST_FLAG.key(), "true").set(RssSparkConfig.RSS_TEST_MODE_ENABLE.key(), "true").set(RssSparkConfig.RSS_CLIENT_SEND_CHECK_TIMEOUT_MS.key(), "10000").set(RssSparkConfig.RSS_CLIENT_RETRY_MAX.key(), "10").set(RssSparkConfig.RSS_CLIENT_SEND_CHECK_INTERVAL_MS.key(), "1000").set(RssSparkConfig.RSS_STORAGE_TYPE.key(), StorageType.LOCALFILE.name()).set(RssSparkConfig.RSS_COORDINATOR_QUORUM.key(), "127.0.0.1:12345,127.0.0.1:12346");
    Map<String, Set<Long>> failBlocks = JavaUtils.newConcurrentMap();
    Map<String, Set<Long>> successBlocks = JavaUtils.newConcurrentMap();
    Serializer kryoSerializer = new KryoSerializer(conf);
    RssShuffleManager manager = TestUtils.createShuffleManager(conf, false, null, successBlocks, failBlocks, JavaUtils.newConcurrentMap());
    ShuffleWriteClient mockShuffleWriteClient = mock(ShuffleWriteClient.class);
    Partitioner mockPartitioner = mock(Partitioner.class);
    RssShuffleHandle<String, String, String> mockHandle = mock(RssShuffleHandle.class);
    ShuffleDependency<String, String, String> mockDependency = mock(ShuffleDependency.class);
    when(mockHandle.getDependency()).thenReturn(mockDependency);
    when(mockPartitioner.numPartitions()).thenReturn(2);
    TaskMemoryManager mockTaskMemoryManager = mock(TaskMemoryManager.class);
    when(mockHandle.getPartitionToServers()).thenReturn(Maps.newHashMap());
    when(mockDependency.partitioner()).thenReturn(mockPartitioner);
    BufferManagerOptions bufferOptions = new BufferManagerOptions(conf);
    WriteBufferManager bufferManager = new WriteBufferManager(0, 0, bufferOptions, kryoSerializer, Maps.newHashMap(), mockTaskMemoryManager, new ShuffleWriteMetrics(), RssSparkConfig.toRssConf(conf));
    WriteBufferManager bufferManagerSpy = spy(bufferManager);
    TaskContext contextMock = mock(TaskContext.class);
    ShuffleHandleInfo mockShuffleHandleInfo = mock(ShuffleHandleInfo.class);
    RssShuffleWriter<String, String, String> rssShuffleWriter = new RssShuffleWriter<>("appId", 0, "taskId", 1L, bufferManagerSpy, (new TaskMetrics()).shuffleWriteMetrics(), manager, conf, mockShuffleWriteClient, mockHandle, mockShuffleHandleInfo, contextMock);
    doReturn(1000000L).when(bufferManagerSpy).acquireMemory(anyLong());
    // case 1: all blocks are sent successfully
    successBlocks.put("taskId", Sets.newHashSet(1L, 2L, 3L));
    rssShuffleWriter.checkBlockSendResult(Sets.newHashSet(1L, 2L, 3L));
    successBlocks.clear();
    // case 2: partial blocks aren't sent before spark.rss.writer.send.check.timeout,
    // Runtime exception will be thrown
    successBlocks.put("taskId", Sets.newHashSet(1L, 2L));
    Throwable e2 = assertThrows(RuntimeException.class, () -> rssShuffleWriter.checkBlockSendResult(Sets.newHashSet(1L, 2L, 3L)));
    assertTrue(e2.getMessage().startsWith("Timeout:"));
    successBlocks.clear();
    // case 3: partial blocks are sent failed, Runtime exception will be thrown
    successBlocks.put("taskId", Sets.newHashSet(1L, 2L));
    failBlocks.put("taskId", Sets.newHashSet(3L));
    Throwable e3 = assertThrows(RuntimeException.class, () -> rssShuffleWriter.checkBlockSendResult(Sets.newHashSet(1L, 2L, 3L)));
    assertTrue(e3.getMessage().startsWith("Send failed:"));
    successBlocks.clear();
    failBlocks.clear();
}

```java:test_tgt

@Test
public void checkBlockSendResultTest() {
    SparkConf conf = new SparkConf();
    conf.setAppName("testApp").setMaster("local[2]").set(RssSparkConfig.RSS_TEST_FLAG.key(), "true").set(RssSparkConfig.RSS_TEST_MODE_ENABLE.key(), "true").set(RssSparkConfig.RSS_CLIENT_SEND_CHECK_TIMEOUT_MS.key(), "10000").set(RssSparkConfig.RSS_CLIENT_RETRY_MAX.key(), "10").set(RssSparkConfig.RSS_CLIENT_SEND_CHECK_INTERVAL_MS.key(), "1000").set(RssSparkConfig.RSS_STORAGE_TYPE.key(), StorageType.LOCALFILE.name()).set(RssSparkConfig.RSS_COORDINATOR_QUORUM.key(), "127.0.0.1:12345,127.0.0.1:12346");
    Map<String, Set<Long>> failBlocks = JavaUtils.newConcurrentMap();
    Map<String, Set<Long>> successBlocks = JavaUtils.newConcurrentMap();
    Map<String, Map<Long, BlockingQueue<ShuffleServerInfo>>> taskToFailedBlockIdsAndServer = JavaUtils.newConcurrentMap();
    Serializer kryoSerializer = new KryoSerializer(conf);
    RssShuffleManager manager = TestUtils.createShuffleManager(conf, false, null, successBlocks, failBlocks, taskToFailedBlockIdsAndServer);
    ShuffleWriteClient mockShuffleWriteClient = mock(ShuffleWriteClient.class);
    Partitioner mockPartitioner = mock(Partitioner.class);
    RssShuffleHandle<String, String, String> mockHandle = mock(RssShuffleHandle.class);
    ShuffleDependency<String, String, String> mockDependency = mock(ShuffleDependency.class);
    when(mockHandle.getDependency()).thenReturn(mockDependency);
    when(mockPartitioner.numPartitions()).thenReturn(2);
    TaskMemoryManager mockTaskMemoryManager = mock(TaskMemoryManager.class);
    when(mockHandle.getPartitionToServers()).thenReturn(Maps.newHashMap());
    when(mockDependency.partitioner()).thenReturn(mockPartitioner);
    BufferManagerOptions bufferOptions = new BufferManagerOptions(conf);
    WriteBufferManager bufferManager = new WriteBufferManager(0, 0, bufferOptions, kryoSerializer, Maps.newHashMap(), mockTaskMemoryManager, new ShuffleWriteMetrics(), RssSparkConfig.toRssConf(conf));
    WriteBufferManager bufferManagerSpy = spy(bufferManager);
    TaskContext contextMock = mock(TaskContext.class);
    ShuffleHandleInfo mockShuffleHandleInfo = mock(ShuffleHandleInfo.class);
    RssShuffleWriter<String, String, String> rssShuffleWriter = new RssShuffleWriter<>("appId", 0, "taskId", 1L, bufferManagerSpy, (new TaskMetrics()).shuffleWriteMetrics(), manager, conf, mockShuffleWriteClient, mockHandle, mockShuffleHandleInfo, contextMock);
    doReturn(1000000L).when(bufferManagerSpy).acquireMemory(anyLong());
    // case 1: all blocks are sent successfully
    successBlocks.put("taskId", Sets.newHashSet(1L, 2L, 3L));
    rssShuffleWriter.checkBlockSendResult(Sets.newHashSet(1L, 2L, 3L));
    successBlocks.clear();
    // case 2: partial blocks aren't sent before spark.rss.writer.send.check.timeout,
    // Runtime exception will be thrown
    successBlocks.put("taskId", Sets.newHashSet(1L, 2L));
    Throwable e2 = assertThrows(RuntimeException.class, () -> rssShuffleWriter.checkBlockSendResult(Sets.newHashSet(1L, 2L, 3L)));
    assertTrue(e2.getMessage().startsWith("Timeout:"));
    successBlocks.clear();
    // case 3: partial blocks are sent failed, Runtime exception will be thrown
    successBlocks.put("taskId", Sets.newHashSet(1L, 2L));
    failBlocks.put("taskId", Sets.newHashSet(3L));
    Map<Long, BlockingQueue<ShuffleServerInfo>> blockIdToShuffleServerInfoMap = JavaUtils.newConcurrentMap();
    BlockingQueue blockingQueue = new LinkedBlockingQueue<>();
    ShuffleServerInfo shuffleServerInfo = new ShuffleServerInfo("127.0.0.1", 20001);
    blockingQueue.add(shuffleServerInfo);
    blockIdToShuffleServerInfoMap.put(3L, blockingQueue);
    taskToFailedBlockIdsAndServer.put("taskId", blockIdToShuffleServerInfoMap);
    Throwable e3 = assertThrows(RuntimeException.class, () -> rssShuffleWriter.checkBlockSendResult(Sets.newHashSet(1L, 2L, 3L)));
    assertTrue(e3.getMessage().startsWith("Send failed:"));
    successBlocks.clear();
    failBlocks.clear();
}

```java:llm_gen

@Test
public void checkBlockSendResultTest() {
    SparkConf conf = new SparkConf();
    conf.setAppName("testApp").setMaster("local[2]").set(RssSparkConfig.RSS_TEST_FLAG.key(), "true").set(RssSparkConfig.RSS_TEST_MODE_ENABLE.key(), "true").set(RssSparkConfig.RSS_CLIENT_SEND_CHECK_TIMEOUT_MS.key(), "10000").set(RssSparkConfig.RSS_CLIENT_RETRY_MAX.key(), "10").set(RssSparkConfig.RSS_CLIENT_SEND_CHECK_INTERVAL_MS.key(), "1000").set(RssSparkConfig.RSS_STORAGE_TYPE.key(), StorageType.LOCALFILE.name()).set(RssSparkConfig.RSS_COORDINATOR_QUORUM.key(), "127.0.0.1:12345,127.0.0.1:12346");
    Map<String, Set<Long>> successBlocks = JavaUtils.newConcurrentMap();
    Map<String, Map<Long, BlockingQueue<ShuffleServerInfo>>> failBlocks = JavaUtils.newConcurrentMap();
    Serializer kryoSerializer = new KryoSerializer(conf);
    RssShuffleManager manager = TestUtils.createShuffleManager(conf, false, null, successBlocks, failBlocks, JavaUtils.newConcurrentMap());
    ShuffleWriteClient mockShuffleWriteClient = mock(ShuffleWriteClient.class);
    Partitioner mockPartitioner = mock(Partitioner.class);
    RssShuffleHandle<String, String, String> mockHandle = mock(RssShuffleHandle.class);
    ShuffleDependency<String, String, String> mockDependency = mock(ShuffleDependency.class);
    when(mockHandle.getDependency()).thenReturn(mockDependency);
    when(mockPartitioner.numPartitions()).thenReturn(2);
    TaskMemoryManager mockTaskMemoryManager = mock(TaskMemoryManager.class);
    when(mockHandle.getPartitionToServers()).thenReturn(Maps.newHashMap());
    when(mockDependency.partitioner()).thenReturn(mockPartitioner);
    BufferManagerOptions bufferOptions = new BufferManagerOptions(conf);
    WriteBufferManager bufferManager = new WriteBufferManager(0, 0, bufferOptions, kryoSerializer, Maps.newHashMap(), mockTaskMemoryManager, new ShuffleWriteMetrics(), RssSparkConfig.toRssConf(conf));
    WriteBufferManager bufferManagerSpy = spy(bufferManager);
    TaskContext contextMock = mock(TaskContext.class);
    ShuffleHandleInfo mockShuffleHandleInfo = mock(ShuffleHandleInfo.class);
    RssShuffleWriter<String, String, String> rssShuffleWriter = new RssShuffleWriter<>("appId", 0, "taskId", 1L, bufferManagerSpy, (new TaskMetrics()).shuffleWriteMetrics(), manager, conf, mockShuffleWriteClient, mockHandle, mockShuffleHandleInfo, contextMock);
    doReturn(1000000L).when(bufferManagerSpy).acquireMemory(anyLong());
    successBlocks.put("taskId", Sets.newHashSet(1L, 2L, 3L));
    rssShuffleWriter.checkBlockSendResult(Sets.newHashSet(1L, 2L, 3L));
    successBlocks.clear();
    successBlocks.put("taskId", Sets.newHashSet(1L, 2L));
    Throwable e2 = assertThrows(RuntimeException.class, () -> rssShuffleWriter.checkBlockSendResult(Sets.newHashSet(1L, 2L, 3L)));
    assertTrue(e2.getMessage().startsWith("Timeout:"));
    successBlocks.clear();
    successBlocks.put("taskId", Sets.newHashSet(1L, 2L));
    BlockingQueue<ShuffleServerInfo> queue = new LinkedBlockingQueue<>();
    queue.add(new ShuffleServerInfo("id", "host", 0));
    failBlocks.put("taskId", ImmutableMap.of(3L, queue));
    Throwable e3 = assertThrows(RuntimeException.class, () -> rssShuffleWriter.checkBlockSendResult(Sets.newHashSet(1L, 2L, 3L)));
    assertTrue(e3.getMessage().startsWith("Send failed:"));
    successBlocks.clear();
    failBlocks.clear();
}

### 133.Correct
link: https://github.com/YunaiV/ruoyi-vue-pro/commit/ba3fe15ec5d65d140e2fce416349ab01a571b22f
p_path: yudao-module-crm/yudao-module-crm-biz/src/main/java/cn/iocoder/yudao/module/crm/service/clue/CrmClueServiceImpl.java#getCluePage
t_path: yudao-module-crm/yudao-module-crm-biz/src/test/java/cn/iocoder/yudao/module/crm/service/clue/CrmClueServiceImplTest.java#testGetCluePage

```java:test_src

@Test
@Disabled
public void testGetCluePage() {
    CrmClueDO dbClue = randomPojo(CrmClueDO.class, o -> {
        o.setTransformStatus(null);
        o.setFollowUpStatus(null);
        o.setName(null);
        o.setCustomerId(null);
        o.setContactNextTime(null);
        o.setTelephone(null);
        o.setMobile(null);
        o.setAddress(null);
        o.setContactLastTime(null);
        o.setCreateTime(null);
    });
    clueMapper.insert(dbClue);
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setTransformStatus(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setFollowUpStatus(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setName(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setCustomerId(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setContactNextTime(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setTelephone(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setMobile(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setAddress(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setContactLastTime(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setCreateTime(null)));
    CrmCluePageReqVO reqVO = new CrmCluePageReqVO();
    reqVO.setName(null);
    reqVO.setTelephone(null);
    reqVO.setMobile(null);
    PageResult<CrmClueDO> pageResult = clueService.getCluePage(reqVO);
    assertEquals(1, pageResult.getTotal());
    assertEquals(1, pageResult.getList().size());
    assertPojoEquals(dbClue, pageResult.getList().get(0));
}

```java:test_tgt

@Test
@Disabled
public void testGetCluePage() {
    CrmClueDO dbClue = randomPojo(CrmClueDO.class, o -> {
        o.setTransformStatus(null);
        o.setFollowUpStatus(null);
        o.setName(null);
        o.setCustomerId(null);
        o.setContactNextTime(null);
        o.setTelephone(null);
        o.setMobile(null);
        o.setAddress(null);
        o.setContactLastTime(null);
        o.setCreateTime(null);
    });
    clueMapper.insert(dbClue);
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setTransformStatus(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setFollowUpStatus(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setName(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setCustomerId(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setContactNextTime(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setTelephone(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setMobile(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setAddress(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setContactLastTime(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setCreateTime(null)));
    CrmCluePageReqVO reqVO = new CrmCluePageReqVO();
    reqVO.setName(null);
    reqVO.setTelephone(null);
    reqVO.setMobile(null);
    PageResult<CrmClueDO> pageResult = clueService.getCluePage(reqVO, 1L);
    assertEquals(1, pageResult.getTotal());
    assertEquals(1, pageResult.getList().size());
    assertPojoEquals(dbClue, pageResult.getList().get(0));
}

```java:llm_gen

@Test
@Disabled
public void testGetCluePage() {
    CrmClueDO dbClue = randomPojo(CrmClueDO.class, o -> {
        o.setTransformStatus(null);
        o.setFollowUpStatus(null);
        o.setName(null);
        o.setCustomerId(null);
        o.setContactNextTime(null);
        o.setTelephone(null);
        o.setMobile(null);
        o.setAddress(null);
        o.setContactLastTime(null);
        o.setCreateTime(null);
    });
    clueMapper.insert(dbClue);
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setTransformStatus(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setFollowUpStatus(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setName(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setCustomerId(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setContactNextTime(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setTelephone(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setMobile(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setAddress(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setContactLastTime(null)));
    clueMapper.insert(cloneIgnoreId(dbClue, o -> o.setCreateTime(null)));
    CrmCluePageReqVO reqVO = new CrmCluePageReqVO();
    reqVO.setName(null);
    reqVO.setTelephone(null);
    reqVO.setMobile(null);
    PageResult<CrmClueDO> pageResult = clueService.getCluePage(reqVO, 1L);
    assertEquals(1, pageResult.getTotal());
    assertEquals(1, pageResult.getList().size());
    assertPojoEquals(dbClue, pageResult.getList().get(0));
}

### 134.Wrong Update Direction
link: https://github.com/StarRocks/starrocks/commit/841d50073e413a6148fff5df313484bc75eb9068
p_path: fe/fe-core/src/main/java/com/starrocks/mysql/MysqlPassword.java#checkPassword
t_path: fe/fe-core/src/test/java/com/starrocks/mysql/MysqlPasswordTest.java#testCheckPassword

```java:test_src

@Test
public void testCheckPassword() throws AnalysisException {
    Assert.assertEquals("*9A6EC51164108A8D3DA3BE3F35A56F6499B6FC32", new String(MysqlPassword.checkPassword("*9A6EC51164108A8D3DA3BE3F35A56F6499B6FC32")));
    Assert.assertEquals("", new String(MysqlPassword.checkPassword(null)));
}

```java:test_tgt

@Test
public void testCheckPassword() {
    Assert.assertEquals("*9A6EC51164108A8D3DA3BE3F35A56F6499B6FC32", new String(MysqlPassword.checkPassword("*9A6EC51164108A8D3DA3BE3F35A56F6499B6FC32")));
    Assert.assertEquals("", new String(MysqlPassword.checkPassword(null)));
}

```java:llm_gen

@Test
public void testCheckPassword() throws AnalysisException {
    Assert.assertEquals("*9A6EC51164108A8D3DA3BE3F35A56F6499B6FC32", new String(MysqlPassword.checkPassword("*9A6EC51164108A8D3DA3BE3F35A56F6499B6FC32")));
    Assert.assertEquals("", new String(MysqlPassword.checkPassword(null)));
    Assert.assertEquals("", new String(MysqlPassword.checkPassword("")));
}

### 135.External Class Modification
link: https://github.com/CorfuDB/CorfuDB/commit/f7f0984fad8cd14c88f918adabe24ce535617ded
p_path: infrastructure/src/main/java/org/corfudb/infrastructure/logreplication/infrastructure/msghandlers/LogReplicationServer.java#handleLeadershipQuery
t_path: infrastructure/src/test/java/org/corfudb/infrastructure/LogReplicationServerTest.java#testHandleLeadershipQuery

```java:test_src

@Test
public void testHandleLeadershipQuery() {
    final LogReplicationLeadershipRequestMsg leadershipQuery = LogReplicationLeadershipRequestMsg.newBuilder().build();
    final RequestMsg request = getRequestMsg(HeaderMsg.newBuilder().setClusterId(sourceClusterUuid).build(), CorfuMessage.RequestPayloadMsg.newBuilder().setLrLeadershipQuery(leadershipQuery).build());
    doReturn(SAMPLE_HOSTNAME).when(context).getLocalEndpoint();
    lrServer.getHandlerMethods().handle(request, null, mockServerRouter);
    ArgumentCaptor<ResponseMsg> argument = ArgumentCaptor.forClass(ResponseMsg.class);
    verify(mockServerRouter).sendResponse(argument.capture());
    lrServer.getHandlerMethods().handle(request, null, mockServerRouter);
    argument = ArgumentCaptor.forClass(ResponseMsg.class);
    verify(mockServerRouter, atMost(2)).sendResponse(argument.capture());
    Assertions.assertThat(argument.getValue().getPayload().getLrLeadershipResponse().getIsLeader()).isTrue();
}

```java:test_tgt

@Test
public void testHandleLeadershipQuery() {
    final LogReplicationLeadershipRequestMsg leadershipQuery = LogReplicationLeadershipRequestMsg.newBuilder().setSession(session).build();
    final RequestMsg request = getRequestMsg(HeaderMsg.newBuilder().setClusterId(sourceClusterUuid).build(), CorfuMessage.RequestPayloadMsg.newBuilder().setLrLeadershipQuery(leadershipQuery).build());
    doReturn(SAMPLE_HOSTNAME).when(context).getLocalEndpoint();
    lrServer.getHandlerMethods().handle(request, null, mockServerRouter);
    ArgumentCaptor<ResponseMsg> argument = ArgumentCaptor.forClass(ResponseMsg.class);
    verify(mockServerRouter).sendResponse(argument.capture());
    lrServer.getHandlerMethods().handle(request, null, mockServerRouter);
    argument = ArgumentCaptor.forClass(ResponseMsg.class);
    verify(mockServerRouter, atMost(2)).sendResponse(argument.capture());
    Assertions.assertThat(argument.getValue().getPayload().getLrLeadershipResponse().getIsLeader()).isTrue();
}

```java:llm_gen

@Test
public void testHandleLeadershipQuery() {
    final LogReplicationLeadershipRequestMsg leadershipQuery = LogReplicationLeadershipRequestMsg.newBuilder().build();
    final RequestMsg request = getRequestMsg(HeaderMsg.newBuilder().setClusterId(sourceClusterUuid).build(), CorfuMessage.RequestPayloadMsg.newBuilder().setLrLeadershipQuery(leadershipQuery).build());
    doReturn(SAMPLE_HOSTNAME).when(context).getLocalEndpoint();
    when(replicationContext.getIsLeader().get()).thenReturn(true);
    when(allSessions.contains(any())).thenReturn(true);
    lrServer.getHandlerMethods().handle(request, null, mockServerRouter);
    ArgumentCaptor<ResponseMsg> argument = ArgumentCaptor.forClass(ResponseMsg.class);
    verify(mockServerRouter).sendResponse(argument.capture());
    lrServer.getHandlerMethods().handle(request, null, mockServerRouter);
    argument = ArgumentCaptor.forClass(ResponseMsg.class);
    verify(mockServerRouter, atMost(2)).sendResponse(argument.capture());
    Assertions.assertThat(argument.getValue().getPayload().getLrLeadershipResponse().getIsLeader()).isTrue();
}

### 136.Missing Asserts
link: https://github.com/questdb/questdb/commit/c643f9616f5a9766a6281407a8e710747a50b419
p_path: core/src/main/java/io/questdb/std/str/Utf8s.java#startsWith
t_path: core/src/test/java/io/questdb/test/std/str/Utf8sTest.java#testStartsWith

```java:test_src

@Test
public void testStartsWith() {
    Assert.assertTrue(Utf8s.startsWith(new Utf8String("фу бар баз"), new Utf8String("фу")));
    Assert.assertFalse(Utf8s.startsWith(new Utf8String("фу бар баз"), new Utf8String("бар")));
    Assert.assertTrue(Utf8s.startsWith(new Utf8String("фу бар баз"), Utf8String.EMPTY));
    Assert.assertFalse(Utf8s.startsWith(Utf8String.EMPTY, new Utf8String("фу-фу-фу")));
}

```java:test_tgt

@Test
public void testStartsWith() {
    String asciiShort = "abcdef";
    String asciiMid = "abcdefgh";
    String asciiLong = "abcdefghijk";
    Assert.assertTrue(Utf8s.startsWith(utf8(asciiShort), utf8("ab")));
    Assert.assertTrue(Utf8s.startsWith(utf8(asciiShort), utf8(asciiShort)));
    Assert.assertFalse(Utf8s.startsWith(utf8(asciiShort), utf8(asciiMid)));
    Assert.assertFalse(Utf8s.startsWith(utf8(asciiShort), utf8(asciiLong)));
    Assert.assertFalse(Utf8s.startsWith(utf8(asciiShort), utf8("abcdex")));
    Assert.assertTrue(Utf8s.startsWith(utf8(asciiMid), utf8(asciiMid)));
    Assert.assertFalse(Utf8s.startsWith(utf8(asciiMid), utf8(asciiLong)));
    Assert.assertFalse(Utf8s.startsWith(utf8(asciiMid), utf8("abcdefgx")));
    Assert.assertFalse(Utf8s.startsWith(utf8(asciiMid), utf8("xabcde")));
    Assert.assertTrue(Utf8s.startsWith(utf8(asciiLong), utf8(asciiShort)));
    Assert.assertTrue(Utf8s.startsWith(utf8(asciiLong), utf8(asciiMid)));
    Assert.assertFalse(Utf8s.startsWith(utf8(asciiLong), utf8("xabcdefghijk")));
    Assert.assertFalse(Utf8s.startsWith(utf8(asciiLong), utf8("abcdefghijkl")));
    Assert.assertFalse(Utf8s.startsWith(utf8(asciiLong), utf8("x")));
    String nonAsciiLong = "фу бар баз";
    Assert.assertTrue(Utf8s.startsWith(utf8(nonAsciiLong), utf8("фу")));
    Assert.assertFalse(Utf8s.startsWith(utf8(nonAsciiLong), utf8("бар")));
    Assert.assertTrue(Utf8s.startsWith(utf8(nonAsciiLong), Utf8String.EMPTY));
    Assert.assertFalse(Utf8s.startsWith(Utf8String.EMPTY, utf8("фу-фу-фу")));
}

```java:llm_gen

@Test
public void testStartsWith() {
    Assert.assertTrue(Utf8s.startsWith(new Utf8String("фу бар баз"), 0L, new Utf8String("фу"), 0L));
    Assert.assertFalse(Utf8s.startsWith(new Utf8String("фу бар баз"), 0L, new Utf8String("бар"), 0L));
    Assert.assertTrue(Utf8s.startsWith(new Utf8String("фу бар баз"), 0L, Utf8String.EMPTY, 0L));
    Assert.assertFalse(Utf8s.startsWith(Utf8String.EMPTY, 0L, new Utf8String("фу-фу-фу"), 0L));
}

### 137.Missing Asserts
link: https://github.com/thingsboard/thingsboard/commit/f43263580078b5bc39e3969e1c8e86ac8a1f4918
p_path: application/src/main/java/org/thingsboard/server/controller/EdgeController.java#saveEdge
t_path: application/src/test/java/org/thingsboard/server/controller/EdgeControllerTest.java#testSaveEdge

```java:test_src

@Test
public void testSaveEdge() throws Exception {
    Edge edge = constructEdge("My edge", "default");
    Mockito.reset(tbClusterService, auditLogService);
    Edge savedEdge = doPost("/api/edge", edge, Edge.class);
    Assert.assertNotNull(savedEdge);
    Assert.assertNotNull(savedEdge.getId());
    Assert.assertTrue(savedEdge.getCreatedTime() > 0);
    Assert.assertEquals(tenantId, savedEdge.getTenantId());
    Assert.assertNotNull(savedEdge.getCustomerId());
    Assert.assertEquals(NULL_UUID, savedEdge.getCustomerId().getId());
    Assert.assertEquals(edge.getName(), savedEdge.getName());
    testNotifyEntityBroadcastEntityStateChangeEventOneTimeMsgToEdgeServiceNever(savedEdge, savedEdge.getId(), savedEdge.getId(), tenantId, tenantAdminUser.getCustomerId(), tenantAdminUser.getId(), tenantAdminUser.getEmail(), ActionType.ADDED);
    savedEdge.setName("My new edge");
    doPost("/api/edge", savedEdge, Edge.class);
    Edge foundEdge = doGet("/api/edge/" + savedEdge.getId().getId().toString(), Edge.class);
    Assert.assertEquals(foundEdge.getName(), savedEdge.getName());
    testNotifyEntityBroadcastEntityStateChangeEventOneTimeMsgToEdgeServiceNever(foundEdge, foundEdge.getId(), foundEdge.getId(), tenantId, tenantAdminUser.getCustomerId(), tenantAdminUser.getId(), tenantAdminUser.getEmail(), ActionType.UPDATED);
}

```java:test_tgt

@Test
public void testSaveEdge() throws Exception {
    Edge edge = constructEdge("My edge", "default");
    Mockito.reset(tbClusterService, auditLogService);
    Edge savedEdge = doPost("/api/edge", edge, Edge.class);
    Assert.assertNotNull(savedEdge);
    Assert.assertNotNull(savedEdge.getId());
    Assert.assertTrue(savedEdge.getCreatedTime() > 0);
    Assert.assertEquals(tenantId, savedEdge.getTenantId());
    Assert.assertNotNull(savedEdge.getCustomerId());
    Assert.assertEquals(NULL_UUID, savedEdge.getCustomerId().getId());
    Assert.assertEquals(edge.getName(), savedEdge.getName());
    testNotifyEntityBroadcastEntityStateChangeEventManyTimeMsgToEdgeServiceNever(savedEdge, savedEdge.getId(), savedEdge.getId(), tenantId, tenantAdminUser.getCustomerId(), tenantAdminUser.getId(), tenantAdminUser.getEmail(), ActionType.ADDED, 2);
    savedEdge.setName("My new edge");
    doPost("/api/edge", savedEdge, Edge.class);
    Edge foundEdge = doGet("/api/edge/" + savedEdge.getId().getId().toString(), Edge.class);
    Assert.assertEquals(foundEdge.getName(), savedEdge.getName());
    testNotifyEntityBroadcastEntityStateChangeEventManyTimeMsgToEdgeServiceNever(foundEdge, foundEdge.getId(), foundEdge.getId(), tenantId, tenantAdminUser.getCustomerId(), tenantAdminUser.getId(), tenantAdminUser.getEmail(), ActionType.UPDATED, 1);
}

```java:llm_gen

@Test
public void testSaveEdge() throws Exception {
    Edge edge = constructEdge("My edge", "default");
    Mockito.reset(tbClusterService, auditLogService);
    Edge savedEdge = doPost("/api/edge", edge, Edge.class);
    Assert.assertNotNull(savedEdge);
    Assert.assertNotNull(savedEdge.getId());
    Assert.assertTrue(savedEdge.getCreatedTime() > 0);
    Assert.assertEquals(tenantId, savedEdge.getTenantId());
    Assert.assertEquals(edge.getName(), savedEdge.getName());
    testNotifyEntityBroadcastEntityStateChangeEventOneTimeMsgToEdgeServiceNever(savedEdge, savedEdge.getId(), savedEdge.getId(), tenantId, tenantAdminUser.getCustomerId(), tenantAdminUser.getId(), tenantAdminUser.getEmail(), ActionType.ADDED);
    savedEdge.setName("My new edge");
    doPost("/api/edge", savedEdge, Edge.class);
    Edge foundEdge = doGet("/api/edge/" + savedEdge.getId().getId().toString(), Edge.class);
    Assert.assertEquals(foundEdge.getName(), savedEdge.getName());
    testNotifyEntityBroadcastEntityStateChangeEventOneTimeMsgToEdgeServiceNever(foundEdge, foundEdge.getId(), foundEdge.getId(), tenantId, tenantAdminUser.getCustomerId(), tenantAdminUser.getId(), tenantAdminUser.getEmail(), ActionType.UPDATED);
}

### 138.External Function Modification
link: https://github.com/dhis2/dhis2-core/commit/ddaa2e9ce37708072964bfa61e488e0b403dfdaa
p_path: dhis-2/dhis-api/src/main/java/org/hisp/dhis/relationship/RelationshipStore.java#getByEvent
t_path: dhis-2/dhis-test-integration/src/test/java/org/hisp/dhis/relationship/hibernate/RelationshipStoreTest.java#testGetByEvent

```java:test_src

@Test
void testGetByEvent() {
    Program programA = addProgram();
    Enrollment enrollment = addEnrollment(programA);
    ProgramStage programStageA = addProgramStage(programA);
    Event event = addEvent(enrollment, programStageA);
    trackedEntityA = createTrackedEntity(organisationUnit);
    trackedEntityService.addTrackedEntity(trackedEntityA);
    Relationship relationshipA = addTeiToEventRelationship(trackedEntityA, event);
    List<Relationship> relationshipList = relationshipService.getRelationshipsByEvent(event, true);
    assertEquals(1, relationshipList.size());
    assertTrue(relationshipList.contains(relationshipA));
    assertTrue(relationshipService.getRelationshipByRelationship(relationshipA).isPresent());
}

```java:test_tgt

@Test
void testGetByEvent() {
    Program programA = addProgram();
    Enrollment enrollment = addEnrollment(programA);
    ProgramStage programStageA = addProgramStage(programA);
    Event event = addEvent(enrollment, programStageA);
    trackedEntityA = createTrackedEntity(organisationUnit);
    trackedEntityService.addTrackedEntity(trackedEntityA);
    Relationship relationshipA = addTeiToEventRelationship(trackedEntityA, event);
    List<Relationship> relationshipList = relationshipService.getRelationshipsByEvent(event, false);
    assertEquals(1, relationshipList.size());
    assertTrue(relationshipList.contains(relationshipA));
    assertTrue(relationshipService.getRelationshipByRelationship(relationshipA).isPresent());
}

```java:llm_gen

@Test
void testGetByEvent() {
    Program programA = addProgram();
    Enrollment enrollment = addEnrollment(programA);
    ProgramStage programStageA = addProgramStage(programA);
    Event event = addEvent(enrollment, programStageA);
    trackedEntityA = createTrackedEntity(organisationUnit);
    trackedEntityService.addTrackedEntity(trackedEntityA);
    Relationship relationshipA = addTeiToEventRelationship(trackedEntityA, event);
    List<Relationship> relationshipList = relationshipService.getByEvent(event, new PagingAndSortingCriteriaAdapter(), true);
    assertEquals(1, relationshipList.size());
    assertTrue(relationshipList.contains(relationshipA));
    assertTrue(relationshipService.getRelationshipByRelationship(relationshipA).isPresent());
}

### 139.External Class Modification
link: https://github.com/alibaba/nacos/commit/4d30b042ee2bbd387ef6774e293310e107737b94
p_path: logger-adapter-impl/log4j2-adapter/src/main/java/com/alibaba/nacos/logger/adapter/log4j2/NacosClientPropertiesLookup.java#lookup
t_path: logger-adapter-impl/log4j2-adapter/src/test/java/com/alibaba/nacos/logger/adapter/log4j2/NacosClientPropertiesLookupTest.java#testLookUp

```java:test_src

@Test
public void testLookUp() {
    NacosClientProperties.PROTOTYPE.setProperty("test.nacos.logging.lookup", "true");
    NacosClientPropertiesLookup nacosClientPropertiesLookup = new NacosClientPropertiesLookup();
    final String actual = nacosClientPropertiesLookup.lookup("test.nacos.logging.lookup");
    Assert.assertEquals("true", actual);
}

```java:test_tgt

@Test
public void testLookUp() {
    System.setProperty("test.nacos.logging.lookup", "true");
    NacosLoggingProperties properties = new NacosLoggingProperties("", System.getProperties());
    Log4j2NacosLoggingPropertiesHolder.setProperties(properties);
    NacosClientPropertiesLookup nacosClientPropertiesLookup = new NacosClientPropertiesLookup();
    final String actual = nacosClientPropertiesLookup.lookup("test.nacos.logging.lookup");
    Assert.assertEquals("true", actual);
}

```java:llm_gen

@Test
public void testLookUp() {
    Log4j2NacosLoggingPropertiesHolder.setValue("test.nacos.logging.lookup", "true");
    NacosClientPropertiesLookup nacosClientPropertiesLookup = new NacosClientPropertiesLookup();
    final String actual = nacosClientPropertiesLookup.lookup(null, "test.nacos.logging.lookup");
    Assert.assertEquals("true", actual);
}


### 140.Wrong Update Direction
link: https://github.com/questdb/questdb/commit/e065400768734bde734149b1272b0f2f8968f779
p_path: core/src/main/java/io/questdb/std/str/Path.java#prefix
t_path: core/src/test/java/io/questdb/test/std/str/PathTest.java#testPrefix

```java:test_src

@Test
public void testPrefix() {
    try (Path p0 = new Path(4).putAscii("foobar").$()) {
        path.of("baz").prefix(p0, p0.size()).$();
        TestUtils.assertEquals("foobarbaz", path.toString());
    }
}

```java:test_tgt

@Test
public void testPrefix() {
    try (Path p0 = new Path(4).putAscii("foobar").$()) {
        path.of("baz").prefix(p0, p0.size()).$();
        Assert.assertTrue(p0.isAscii());
        Assert.assertTrue(path.isAscii());
        TestUtils.assertEquals("foobarbaz", path.toString());
    }
}

```java:llm_gen

@Test
public void testPrefix() {
    try (Path p0 = new Path(4).putAscii("foobar").$()) {
        path.of("baz").prefix(p0, p0.size()).$();
        TestUtils.assertEquals("foobarbaz", path.toString());
    }
    try (Path p0 = new Path(4).putNonAscii("日本語").$()) {
        path.of("baz").prefix(p0, p0.size()).$();
        TestUtils.assertEquals("日本語baz", path.toString());
    }
}

### 141.External Class Modification
link: https://github.com/huaweicloud/Sermant/commit/d270273bef4eede4287a89ce412e1f61f7b6fc62
p_path: sermant-plugins/sermant-database-write-prohibition/postgresql-9.4.x-plugin/src/main/java/com/huaweicloud/sermant/postgresqlv9/interceptors/Jdbc2StatementInterceptor.java#doBefore
t_path: sermant-plugins/sermant-database-write-prohibition/postgresql-9.4.x-plugin/src/test/java/com/huaweicloud/sermant/postgresqlv9/interceptors/Jdbc2StatementInterceptorTest.java#testDoBefore

```java:test_src

@Test
public void testDoBefore() throws Exception {
    ExecuteContext context = ExecuteContext.forMemberMethod(abstractJdbc3gStatement, methodMock, null, null, null);
    jdbc4StatementInterceptor.before(context);
    Assert.assertNotNull(ThreadConnectionUtil.getConnection());
}

```java:test_tgt

@Test
public void testDoBefore() throws Exception {
    ExecuteContext context = ExecuteContext.forMemberMethod(abstractJdbc3gStatement, methodMock, null, null, null);
    jdbc2StatementInterceptor.before(context);
    Assert.assertNotNull(ThreadDatabaseUrlUtil.getDatabaseUrl());
}

```java:llm_gen

@Test
public void testDoBefore() throws Exception {
    ExecuteContext context = ExecuteContext.forMemberMethod(abstractJdbc3gStatement, methodMock, null, null, null);
    when(abstractJdbc3gStatement.getPGConnection().getMetaData().getURL()).thenReturn("jdbc:postgresql://localhost:5432/test");
    jdbc4StatementInterceptor.before(context);
    Assert.assertNotNull(ThreadDatabaseUrlUtil.getDatabaseUrl());
}

### 142.Correct
link: https://github.com/alibaba/nacos/commit/2f2fc1b12b4ffba0f51ae1b5efd8ff18951e669f
p_path: client/src/main/java/com/alibaba/nacos/client/naming/backups/FailoverReactor.java#failoverServiceCntMetrics
t_path: client/src/test/java/com/alibaba/nacos/client/naming/backups/FailoverReactorTest.java#testFailoverServiceCntMetrics

```java:test_src

@Test
public void testFailoverServiceCntMetrics() throws NoSuchMethodException, InvocationTargetException, IllegalAccessException {
    Method method = FailoverReactor.class.getDeclaredMethod("failoverServiceCntMetrics", Map.class);
    method.setAccessible(true);
    method.invoke(failoverReactor, new Object[1]);
}

```java:test_tgt

@Test
public void testFailoverServiceCntMetrics() throws NoSuchMethodException, InvocationTargetException, IllegalAccessException {
    Method method = FailoverReactor.class.getDeclaredMethod("failoverServiceCntMetrics");
    method.setAccessible(true);
    method.invoke(failoverReactor);
}

```java:llm_gen

@Test
public void testFailoverServiceCntMetrics() throws NoSuchMethodException, InvocationTargetException, IllegalAccessException {
    Method method = FailoverReactor.class.getDeclaredMethod("failoverServiceCntMetrics");
    method.setAccessible(true);
    method.invoke(failoverReactor);
}

### 143.Field/Package Information Modification
link: https://github.com/openhab/openhab-core/commit/1b503afdbbc654e0d845dce7c713813cf652ead5
p_path: bundles/org.openhab.core.persistence/src/main/java/org/openhab/core/persistence/extensions/PersistenceExtensions.java#updatedSince
t_path: bundles/org.openhab.core.persistence/src/test/java/org/openhab/core/persistence/extensions/PersistenceExtensionsTest.java#testUpdatedSince

```java:test_src

@Test
public void testUpdatedSince() {
    boolean updated = PersistenceExtensions.updatedSince(numberItem, ZonedDateTime.of(1940, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), TestPersistenceService.ID);
    assertFalse(updated);
    updated = PersistenceExtensions.updatedSince(numberItem, ZonedDateTime.of(2005, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), TestPersistenceService.ID);
    assertTrue(updated);
    updated = PersistenceExtensions.updatedSince(numberItem, ZonedDateTime.of(2005, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()));
    assertFalse(updated);
}

```java:test_tgt

@Test
public void testUpdatedSince() {
    Boolean updated = PersistenceExtensions.updatedSince(numberItem, ZonedDateTime.of(BEFORE_START, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), SERVICE_ID);
    assertEquals(updated, true);
    updated = PersistenceExtensions.updatedSince(numberItem, ZonedDateTime.of(HISTORIC_INTERMEDIATE_VALUE_1, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), SERVICE_ID);
    assertEquals(updated, true);
    updated = PersistenceExtensions.updatedSince(numberItem, ZonedDateTime.of(HISTORIC_INTERMEDIATE_VALUE_1, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()));
    assertNull(updated);
}

```java:llm_gen

@Test
public void testUpdatedSince() {
    Boolean updated = PersistenceExtensions.updatedSince(numberItem, ZonedDateTime.of(1940, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), TestPersistenceService.ID);
    assertFalse(updated);
    updated = PersistenceExtensions.updatedSince(numberItem, ZonedDateTime.of(2005, 1, 1, 0, 0, 0, 0, ZoneId.systemDefault()), TestPersistenceService.ID);
    assertTrue(updated);
}

### 144.Correct
link: https://github.com/apache/flink-kubernetes-operator/commit/c576c41742b0844c7506c37c456073a65d60ed09
p_path: flink-autoscaler-standalone/src/main/java/org/apache/flink/autoscaler/standalone/AutoscalerStateStoreFactory.java#createJdbcStateStore
t_path: flink-autoscaler-standalone/src/test/java/org/apache/flink/autoscaler/standalone/AutoscalerStateStoreFactoryTest.java#testCreateJdbcStateStore

```java:test_src

@Test
void testCreateJdbcStateStore() throws Exception {
    final var jdbcUrl = "jdbc:derby:memory:test";
    DriverManager.getConnection(String.format("%s;create=true", jdbcUrl)).close();
    final var conf = new Configuration();
    conf.set(STATE_STORE_TYPE, JDBC);
    conf.set(STATE_STORE_JDBC_URL, jdbcUrl);
    var stateStore = AutoscalerStateStoreFactory.create(conf);
    assertThat(stateStore).isInstanceOf(JdbcAutoScalerStateStore.class);
    try {
        DriverManager.getConnection(String.format("%s;shutdown=true", jdbcUrl)).close();
    } catch (SQLException ignored) {
    }
}

```java:test_tgt

@Test
void testCreateJdbcStateStore() throws Exception {
    final var jdbcUrl = "jdbc:derby:memory:test";
    DriverManager.getConnection(String.format("%s;create=true", jdbcUrl)).close();
    final var conf = new Configuration();
    conf.set(STATE_STORE_TYPE, JDBC);
    conf.set(JDBC_URL, jdbcUrl);
    var stateStore = AutoscalerStateStoreFactory.create(conf);
    assertThat(stateStore).isInstanceOf(JdbcAutoScalerStateStore.class);
    try {
        DriverManager.getConnection(String.format("%s;shutdown=true", jdbcUrl)).close();
    } catch (SQLException ignored) {
    }
}

```java:llm_gen

@Test
void testCreateJdbcStateStore() throws Exception {
    final var jdbcUrl = "jdbc:derby:memory:test";
    DriverManager.getConnection(String.format("%s;create=true", jdbcUrl)).close();
    final var conf = new Configuration();
    conf.set(STATE_STORE_TYPE, JDBC);
    conf.set(JDBC_URL, jdbcUrl);
    var stateStore = AutoscalerStateStoreFactory.create(conf);
    assertThat(stateStore).isInstanceOf(JdbcAutoScalerStateStore.class);
    try {
        DriverManager.getConnection(String.format("%s;shutdown=true", jdbcUrl)).close();
    } catch (SQLException ignored) {
    }
}


### 145.Correct
link: https://github.com/Graylog2/graylog2-server/commit/efcc2ef391ea4b930a49b8b101454fb3f4d96a59
p_path: graylog2-server/src/main/java/org/graylog2/indexer/ranges/MongoIndexRangeService.java#handleIndexDeletion
t_path: graylog2-server/src/test/java/org/graylog2/indexer/ranges/MongoIndexRangeServiceTest.java#testHandleIndexDeletion

```java:test_src

@Test
@MongoDBFixtures("MongoIndexRangeServiceTest.json")
public void testHandleIndexDeletion() throws Exception {
    when(indexSetRegistry.isManagedIndex("graylog_1")).thenReturn(true);
    assertThat(indexRangeService.findAll()).hasSize(2);
    localEventBus.post(IndicesDeletedEvent.create(Collections.singleton("graylog_1")));
    assertThat(indexRangeService.findAll()).hasSize(1);
}

```java:test_tgt

@Test
@MongoDBFixtures("MongoIndexRangeServiceTest.json")
public void testHandleIndexDeletion() throws Exception {
    assertThat(indexRangeService.findAll()).hasSize(2);
    localEventBus.post(IndicesDeletedEvent.create(Collections.singleton("graylog_1")));
    assertThat(indexRangeService.findAll()).hasSize(1);
}

```java:llm_gen

@Test
@MongoDBFixtures("MongoIndexRangeServiceTest.json")
public void testHandleIndexDeletion() throws Exception {
    assertThat(indexRangeService.findAll()).hasSize(2);
    localEventBus.post(IndicesDeletedEvent.create(Collections.singleton("graylog_1")));
    assertThat(indexRangeService.findAll()).hasSize(1);
}

### 146.External Function Modification
link: https://github.com/ical4j/ical4j/commit/f4cec5ed560bd5dfcdd6c68993c4246355084583
p_path: src/main/java/net/fortuna/ical4j/model/Period.java#isEmpty
t_path: src/test/java/net/fortuna/ical4j/model/PeriodTest.java#testIsEmpty

```java:test_src

public void testIsEmpty() {
    Calendar cal = Calendar.getInstance();
    DateTime start = new DateTime(cal.getTime());
    assertTrue(new Period(start, start).isEmpty());
    assertTrue(new Period(start, java.time.Period.ZERO).isEmpty());
    cal.add(Calendar.SECOND, 1);
    assertFalse(new Period(start, new DateTime(cal.getTime())).isEmpty());
    assertFalse(new Period(start, java.time.Duration.ofSeconds(1)).isEmpty());
}

```java:test_tgt

public void testIsEmpty() {
    ZonedDateTime start = ZonedDateTime.now();
    assertTrue(new Period<>(start, start).isEmpty());
    assertTrue(new Period<>(start, java.time.Period.ZERO).isEmpty());
    assertFalse(new Period<>(start, start.withSecond(1)).isEmpty());
    assertFalse(new Period<>(start, java.time.Duration.ofSeconds(1)).isEmpty());
}

```java:llm_gen

public void testIsEmpty() {
    Calendar cal = Calendar.getInstance();
    DateTime start = new DateTime(cal.getTime());
    // Test with same start and end (date-time precision)
    assertTrue(new Period(start, start).isEmpty());
    // Test with zero duration (date-time precision)
    assertTrue(new Period(start, java.time.Period.ZERO).isEmpty());
    // Test with different start and end (date-time precision)
    cal.add(Calendar.SECOND, 1);
    assertFalse(new Period(start, new DateTime(cal.getTime())).isEmpty());
    // Test with non-zero duration (date-time precision)
    assertFalse(new Period(start, java.time.Duration.ofSeconds(1)).isEmpty());
    // Test with non-date-time precision
    DateTime dateOnlyStart = new DateTime(cal.getTime()).withTimeAtStartOfDay();
    assertTrue(new Period(dateOnlyStart, dateOnlyStart).isEmpty());
    DateTime dateOnlyEnd = dateOnlyStart.plusDays(1);
    assertFalse(new Period(dateOnlyStart, dateOnlyEnd).isEmpty());
}

### 147.External File Modification
link: https://github.com/soot-oss/SootUp/commit/c3aa6378905c7e531b26fa983e773ff884d83868
p_path: sootup.java.bytecode/src/main/java/sootup/java/bytecode/inputlocation/JavaModulePathAnalysisInputLocation.java#getModuleInfo
t_path: sootup.java.bytecode/src/test/java/sootup/java/bytecode/inputlocation/JavaModulePathAnalysisInputLocationTest.java#testGetModuleInfo

```java:test_src

@Test
public void testGetModuleInfo() {
    JavaProject p = JavaProject.builder(new JavaLanguage(9)).addInputLocation(new JavaModulePathAnalysisInputLocation(testPath + "requires_exports/jar")).build();
    JavaModuleView view = (JavaModuleView) p.createView();
    ModulePackageName modMain = JavaModuleIdentifierFactory.getInstance().getPackageName("pkgmain", "modmain");
    ModulePackageName modB = JavaModuleIdentifierFactory.getInstance().getPackageName("pkgb", "modb");
    ModulePackageName modC = JavaModuleIdentifierFactory.getInstance().getPackageName("pkgc", "modc");
    Optional<JavaModuleInfo> moduleInfoMain = view.getModuleInfo(modMain.getModuleSignature());
    assertTrue(moduleInfoMain.isPresent());
    Optional<JavaModuleInfo> moduleInfoB = view.getModuleInfo(modB.getModuleSignature());
    assertTrue(moduleInfoB.isPresent());
    Optional<JavaModuleInfo> moduleInfoC = view.getModuleInfo(modC.getModuleSignature());
    assertTrue(moduleInfoC.isPresent());
}

```java:test_tgt

@Test
public void testGetModuleInfo() {
    List<AnalysisInputLocation> inputLocations = Collections.singletonList(new JavaModulePathAnalysisInputLocation(testPath + "requires_exports/jar"));
    List<ModuleInfoAnalysisInputLocation> moduleInfoAnalysisInputLocations = Collections.emptyList();
    JavaModuleView view = new JavaModuleView(inputLocations, moduleInfoAnalysisInputLocations);
    ModulePackageName modMain = JavaModuleIdentifierFactory.getInstance().getPackageName("pkgmain", "modmain");
    ModulePackageName modB = JavaModuleIdentifierFactory.getInstance().getPackageName("pkgb", "modb");
    ModulePackageName modC = JavaModuleIdentifierFactory.getInstance().getPackageName("pkgc", "modc");
    Optional<JavaModuleInfo> moduleInfoMain = view.getModuleInfo(modMain.getModuleSignature());
    assertTrue(moduleInfoMain.isPresent());
    Optional<JavaModuleInfo> moduleInfoB = view.getModuleInfo(modB.getModuleSignature());
    assertTrue(moduleInfoB.isPresent());
    Optional<JavaModuleInfo> moduleInfoC = view.getModuleInfo(modC.getModuleSignature());
    assertTrue(moduleInfoC.isPresent());
}

```java:llm_gen

@Test
public void testGetModuleInfo() {
    JavaProject p = JavaProject.builder(new JavaLanguage(9)).addInputLocation(new JavaModulePathAnalysisInputLocation(testPath + "requires_exports/jar")).build();
    JavaModuleView view = (JavaModuleView) p.createView();
    ModulePackageName modMain = JavaModuleIdentifierFactory.getInstance().getPackageName("pkgmain", "modmain");
    ModulePackageName modB = JavaModuleIdentifierFactory.getInstance().getPackageName("pkgb", "modb");
    ModulePackageName modC = JavaModuleIdentifierFactory.getInstance().getPackageName("pkgc", "modc");
    Optional<JavaModuleInfo> moduleInfoMain = view.getModuleInfo(modMain.getModuleSignature(), view);
    assertTrue(moduleInfoMain.isPresent());
    Optional<JavaModuleInfo> moduleInfoB = view.getModuleInfo(modB.getModuleSignature(), view);
    assertTrue(moduleInfoB.isPresent());
    Optional<JavaModuleInfo> moduleInfoC = view.getModuleInfo(modC.getModuleSignature(), view);
    assertTrue(moduleInfoC.isPresent());
}

### 148.Correct
link: https://github.com/apache/kafka/commit/bf88013a2812cab65bc70667e451e0a15d26b73c
p_path: group-coordinator/src/main/java/org/apache/kafka/coordinator/group/CoordinatorRecordHelpers.java#newGroupEpochTombstoneRecord
t_path: group-coordinator/src/test/java/org/apache/kafka/coordinator/group/CoordinatorRecordHelpersTest.java#testNewGroupEpochTombstoneRecord

```java:test_src

@Test
public void testNewGroupEpochTombstoneRecord() {
    Record expectedRecord = new Record(new ApiMessageAndVersion(new ConsumerGroupMetadataKey().setGroupId("group-id"), (short) 3), null);
    assertEquals(expectedRecord, newGroupEpochTombstoneRecord("group-id"));
}

```java:test_tgt

@Test
public void testNewGroupEpochTombstoneRecord() {
    CoordinatorRecord expectedRecord = new CoordinatorRecord(new ApiMessageAndVersion(new ConsumerGroupMetadataKey().setGroupId("group-id"), (short) 3), null);
    assertEquals(expectedRecord, newGroupEpochTombstoneRecord("group-id"));
}

```java:llm_gen

@Test
public void testNewGroupEpochTombstoneRecord() {
    CoordinatorRecord expectedRecord = new CoordinatorRecord(new ApiMessageAndVersion(new ConsumerGroupMetadataKey().setGroupId("group-id"), (short) 3), null);
    assertEquals(expectedRecord, newGroupEpochTombstoneRecord("group-id"));
}

### 149.Wrong Update Direction
link: https://github.com/StarRocks/starrocks/commit/ae7a4bfb732d4fb07efe3f22c886461655de908d
p_path: fe/fe-core/src/main/java/com/starrocks/qe/scheduler/DefaultWorkerProvider.java#captureAvailableWorkers
t_path: fe/fe-core/src/test/java/com/starrocks/qe/scheduler/DefaultWorkerProviderTest.java#testCaptureAvailableWorkers

```java:test_src

@Test
public void testCaptureAvailableWorkers() {
    long deadBEId = 1L;
    long deadCNId = 11L;
    long inBlacklistBEId = 3L;
    long inBlacklistCNId = 13L;
    Set<Long> nonAvailableWorkerId = ImmutableSet.of(deadBEId, deadCNId, inBlacklistBEId, inBlacklistCNId);
    id2Backend.get(deadBEId).setAlive(false);
    id2ComputeNode.get(deadCNId).setAlive(false);
    new MockUp<SimpleScheduler>() {
        @Mock
        public boolean isInBlocklist(long backendId) {
            return backendId == inBlacklistBEId || backendId == inBlacklistCNId;
        }
    };
    Reference<Integer> nextComputeNodeIndex = new Reference<>(0);
    new MockUp<DefaultWorkerProvider>() {
        @Mock
        int getNextComputeNodeIndex() {
            int next = nextComputeNodeIndex.getRef();
            nextComputeNodeIndex.setRef(next + 1);
            return next;
        }
    };
    new MockUp<SystemInfoService>() {
        @Mock
        public ImmutableMap<Long, ComputeNode> getIdToBackend() {
            return id2Backend;
        }
        @Mock
        public ImmutableMap<Long, ComputeNode> getIdComputeNode() {
            return id2ComputeNode;
        }
    };
    DefaultWorkerProvider.Factory workerProviderFactory = new DefaultWorkerProvider.Factory();
    DefaultWorkerProvider workerProvider;
    List<Integer> numUsedComputeNodesList = ImmutableList.of(100, 0, -1, 1, 2, 3, 4, 5, 6);
    for (Integer numUsedComputeNodes : numUsedComputeNodesList) {
        nextComputeNodeIndex.setRef(0);
        workerProvider = workerProviderFactory.captureAvailableWorkers(GlobalStateMgr.getCurrentState().getNodeMgr().getClusterInfo(), true, numUsedComputeNodes, WarehouseManager.DEFAULT_WAREHOUSE_ID);
        int numAvailableComputeNodes = 0;
        for (long id = 0; id < 15; id++) {
            ComputeNode worker = workerProvider.getWorkerById(id);
            if (nonAvailableWorkerId.contains(id) || (numUsedComputeNodes > 0 && numAvailableComputeNodes >= numUsedComputeNodes)) {
                Assert.assertNull(worker);
            } else {
                Assert.assertNotNull("numUsedComputeNodes=" + numUsedComputeNodes + ",id=" + id, worker);
                Assert.assertEquals(id, worker.getId());
                if (id2ComputeNode.containsKey(id)) {
                    numAvailableComputeNodes++;
                }
            }
        }
    }
}

```java:test_tgt

@Test
public void testCaptureAvailableWorkers() {
    long deadBEId = 1L;
    long deadCNId = 11L;
    long inBlacklistBEId = 3L;
    long inBlacklistCNId = 13L;
    Set<Long> nonAvailableWorkerId = ImmutableSet.of(deadBEId, deadCNId, inBlacklistBEId, inBlacklistCNId);
    id2Backend.get(deadBEId).setAlive(false);
    id2ComputeNode.get(deadCNId).setAlive(false);
    new MockUp<SimpleScheduler>() {
        @Mock
        public boolean isInBlocklist(long backendId) {
            return backendId == inBlacklistBEId || backendId == inBlacklistCNId;
        }
    };
    Reference<Integer> nextComputeNodeIndex = new Reference<>(0);
    new MockUp<DefaultWorkerProvider>() {
        @Mock
        int getNextComputeNodeIndex() {
            int next = nextComputeNodeIndex.getRef();
            nextComputeNodeIndex.setRef(next + 1);
            return next;
        }
    };
    new MockUp<SystemInfoService>() {
        @Mock
        public ImmutableMap<Long, ComputeNode> getIdToBackend() {
            return id2Backend;
        }
        @Mock
        public ImmutableMap<Long, ComputeNode> getIdComputeNode() {
            return id2ComputeNode;
        }
    };
    DefaultWorkerProvider.Factory workerProviderFactory = new DefaultWorkerProvider.Factory();
    DefaultWorkerProvider workerProvider;
    List<Integer> numUsedComputeNodesList = ImmutableList.of(100, 0, -1, 1, 2, 3, 4, 5, 6);
    for (Integer numUsedComputeNodes : numUsedComputeNodesList) {
        nextComputeNodeIndex.setRef(0);
        workerProvider = workerProviderFactory.captureAvailableWorkers(GlobalStateMgr.getCurrentState().getNodeMgr().getClusterInfo(), true, numUsedComputeNodes, ComputationFragmentSchedulingPolicy.COMPUTE_NODES_ONLY, WarehouseManager.DEFAULT_WAREHOUSE_ID);
        int numAvailableComputeNodes = 0;
        for (long id = 0; id < 15; id++) {
            ComputeNode worker = workerProvider.getWorkerById(id);
            if (nonAvailableWorkerId.contains(id) || (numUsedComputeNodes > 0 && numAvailableComputeNodes >= numUsedComputeNodes)) {
                Assert.assertNull(worker);
            } else {
                Assert.assertNotNull("numUsedComputeNodes=" + numUsedComputeNodes + ",id=" + id, worker);
                Assert.assertEquals(id, worker.getId());
                if (id2ComputeNode.containsKey(id)) {
                    numAvailableComputeNodes++;
                }
            }
        }
    }
}

```java:llm_gen

@Test
public void testCaptureAvailableWorkers() {
    long deadBEId = 1L;
    long deadCNId = 11L;
    long inBlacklistBEId = 3L;
    long inBlacklistCNId = 13L;
    Set<Long> nonAvailableWorkerId = ImmutableSet.of(deadBEId, deadCNId, inBlacklistBEId, inBlacklistCNId);
    id2Backend.get(deadBEId).setAlive(false);
    id2ComputeNode.get(deadCNId).setAlive(false);
    new MockUp<SimpleScheduler>() {
        @Mock
        public boolean isInBlocklist(long backendId) {
            return backendId == inBlacklistBEId || backendId == inBlacklistCNId;
        }
    };
    Reference<Integer> nextComputeNodeIndex = new Reference<>(0);
    new MockUp<DefaultWorkerProvider>() {
        @Mock
        int getNextComputeNodeIndex() {
            int next = nextComputeNodeIndex.getRef();
            nextComputeNodeIndex.setRef(next + 1);
            return next;
        }
    };
    new MockUp<SystemInfoService>() {
        @Mock
        public ImmutableMap<Long, ComputeNode> getIdToBackend() {
            return id2Backend;
        }
        @Mock
        public ImmutableMap<Long, ComputeNode> getIdComputeNode() {
            return id2ComputeNode;
        }
    };
    DefaultWorkerProvider.Factory workerProviderFactory = new DefaultWorkerProvider.Factory();
    DefaultWorkerProvider workerProvider;
    List<Integer> numUsedComputeNodesList = ImmutableList.of(100, 0, -1, 1, 2, 3, 4, 5, 6);
    for (Integer numUsedComputeNodes : numUsedComputeNodesList) {
        nextComputeNodeIndex.setRef(0);
        workerProvider = workerProviderFactory.captureAvailableWorkers(GlobalStateMgr.getCurrentState().getNodeMgr().getClusterInfo(), true, numUsedComputeNodes, ComputationFragmentSchedulingPolicy.LOCAL, WarehouseManager.DEFAULT_WAREHOUSE_ID);
        int numAvailableComputeNodes = 0;
        for (long id = 0; id < 15; id++) {
            ComputeNode worker = workerProvider.getWorkerById(id);
            if (nonAvailableWorkerId.contains(id) || (numUsedComputeNodes > 0 && numAvailableComputeNodes >= numUsedComputeNodes)) {
                Assert.assertNull(worker);
            } else {
                Assert.assertNotNull("numUsedComputeNodes=" + numUsedComputeNodes + ",id=" + id, worker);
                Assert.assertEquals(id, worker.getId());
                if (id2ComputeNode.containsKey(id)) {
                    numAvailableComputeNodes++;
                }
            }
        }
    }
}

### 150.Wrong Update Direction
link: https://github.com/confluentinc/ksql/commit/08eb59f516a8a19c348516fa8f7a995c1d1820ea
p_path: ksqldb-engine/src/main/java/io/confluent/ksql/services/DefaultConnectClient.java#describe
t_path: ksqldb-engine/src/test/java/io/confluent/ksql/services/DefaultConnectClientTest.java#testDescribe

```java:test_src

@Test
public void testDescribe() throws JsonProcessingException {
    WireMock.stubFor(WireMock.get(WireMock.urlEqualTo("/connectors/foo")).withHeader(AUTHORIZATION.toString(), new EqualToPattern(AUTH_HEADER)).willReturn(WireMock.aResponse().withStatus(HttpStatus.SC_OK).withBody(MAPPER.writeValueAsString(SAMPLE_INFO))));
    final ConnectResponse<ConnectorInfo> response = client.describe("foo");
    assertThat(response.datum(), OptionalMatchers.of(is(SAMPLE_INFO)));
    assertThat("Expected no error!", !response.error().isPresent());
}

```java:test_tgt

@Test
public void testDescribe() throws JsonProcessingException {
    WireMock.stubFor(WireMock.get(WireMock.urlEqualTo(pathPrefix + "/connectors/foo")).withHeader(AUTHORIZATION.toString(), new EqualToPattern(AUTH_HEADER)).withHeader(CUSTOM_HEADER_NAME, new EqualToPattern(CUSTOM_HEADER_VALUE)).willReturn(WireMock.aResponse().withStatus(HttpStatus.SC_OK).withBody(MAPPER.writeValueAsString(SAMPLE_INFO))));
    final ConnectResponse<ConnectorInfo> response = client.describe("foo");
    assertThat(response.datum(), OptionalMatchers.of(is(SAMPLE_INFO)));
    assertThat("Expected no error!", !response.error().isPresent());
}

```java:llm_gen

@Test
public void testDescribe() throws JsonProcessingException {
    WireMock.stubFor(WireMock.get(WireMock.urlEqualTo("/connectors/foo"))
            .withHeader(AUTHORIZATION.toString(), new EqualToPattern(AUTH_HEADER))
            .willReturn(WireMock.aResponse()
                    .withStatus(HttpStatus.SC_OK)
                    .withBody(MAPPER.writeValueAsString(SAMPLE_INFO)));
    final ConnectResponse<ConnectorInfo> response = client.describe("foo");
    assertThat(response.datum(), OptionalMatchers.of(is(SAMPLE_INFO)));
    assertThat("Expected no error!", !response.error().isPresent());
}

### 151.External Function Modification
link: https://github.com/ls1intum/Artemis/commit/002538346660b4500073790b06009a156a04c433
p_path: src/main/java/de/tum/in/www1/artemis/service/connectors/GitService.java#checkoutRepositoryAtCommit
t_path: src/test/java/de/tum/in/www1/artemis/exercise/programmingexercise/GitServiceTest.java#testCheckoutRepositoryAtCommit

```java:test_src

@ParameterizedTest
@ValueSource(booleans = { true, false })
void testCheckoutRepositoryAtCommit(boolean withUrl) throws GitAPIException {
    prepareRepositoryContent();
    String commitHash = getCommitHash("my first commit");
    if (withUrl) {
        gitService.checkoutRepositoryAtCommit(gitUtilService.getRepoUrlByType(GitUtilService.REPOS.LOCAL), commitHash, true);
    } else {
        try (var repo = gitUtilService.getRepoByType(GitUtilService.REPOS.LOCAL)) {
            gitService.checkoutRepositoryAtCommit(repo, commitHash);
        }
    }
    assertThat(gitUtilService.getFileContent(GitUtilService.REPOS.LOCAL, GitUtilService.FILES.FILE1)).isEqualTo("lorem ipsum");
    assertThat(gitUtilService.getLog(GitUtilService.REPOS.LOCAL)).hasSize(2);
    assertThat(gitUtilService.getFileContent(GitUtilService.REPOS.LOCAL, GitUtilService.FILES.FILE2)).isEmpty();
}

```java:test_tgt

@ParameterizedTest
@ValueSource(booleans = { true, false })
void testCheckoutRepositoryAtCommit(boolean withUrl) throws GitAPIException {
    prepareRepositoryContent();
    String commitHash = getCommitHash("my first commit");
    if (withUrl) {
        gitService.checkoutRepositoryAtCommit(gitUtilService.getRepoUriByType(GitUtilService.REPOS.LOCAL), commitHash, true);
    } else {
        try (var repo = gitUtilService.getRepoByType(GitUtilService.REPOS.LOCAL)) {
            gitService.checkoutRepositoryAtCommit(repo, commitHash);
        }
    }
    assertThat(gitUtilService.getFileContent(GitUtilService.REPOS.LOCAL, GitUtilService.FILES.FILE1)).isEqualTo("lorem ipsum");
    assertThat(gitUtilService.getLog(GitUtilService.REPOS.LOCAL)).hasSize(2);
    assertThat(gitUtilService.getFileContent(GitUtilService.REPOS.LOCAL, GitUtilService.FILES.FILE2)).isEmpty();
}

```java:llm_gen

@ParameterizedTest
@ValueSource(booleans = { true, false })
void testCheckoutRepositoryAtCommit(boolean pullOnGet) throws GitAPIException {
    prepareRepositoryContent();
    String commitHash = getCommitHash("my first commit");
    gitService.checkoutRepositoryAtCommit(gitUtilService.getRepoUrlByType(GitUtilService.REPOS.LOCAL), commitHash, pullOnGet);
    assertThat(gitUtilService.getFileContent(GitUtilService.REPOS.LOCAL, GitUtilService.FILES.FILE1)).isEqualTo("lorem ipsum");
    assertThat(gitUtilService.getLog(GitUtilService.REPOS.LOCAL)).hasSize(2);
    assertThat(gitUtilService.getFileContent(GitUtilService.REPOS.LOCAL, GitUtilService.FILES.FILE2)).isEmpty();
}


### 152.External File Modification
link: https://github.com/NationalSecurityAgency/datawave/commit/a4587afa38a7500588d5eb403e0379e2505d9fb5
p_path: warehouse/query-core/src/main/java/datawave/query/util/sortedset/BufferedFileBackedSortedSet.java#tailSet
t_path: warehouse/query-core/src/test/java/datawave/query/util/sortedset/BufferedFileBackedSortedSetTest.java#testTailSet

```java:test_src

@Test
public void testTailSet() {
    int start = sortedOrder.length / 3;
    try {
        SortedSet<byte[]> subSet = set.tailSet(data[sortedOrder[start]]);
        SortedSet<byte[]> expected = new TreeSet<>(set.comparator());
        for (int i = start; i < sortedOrder.length; i++) {
            expected.add(data[sortedOrder[i]]);
        }
        assertEquals(expected, subSet);
    } catch (Exception e) {
    }
}

```java:test_tgt

@Test
public void testTailSet() {
    int start = sortedOrder.length / 3;
    try {
        SortedSet<E> subSet = set.tailSet(data[sortedOrder[start]]);
        SortedSet<E> expected = new TreeSet<>(set.comparator());
        for (int i = start; i < sortedOrder.length; i++) {
            expected.add(data[sortedOrder[i]]);
        }
        assertEquals(expected, subSet);
    } catch (Exception e) {
    }
}

```java:llm_gen

@Test
public void testTailSet() {
    int start = sortedOrder.length / 3;
    try {
        RewritableSortedSet<byte[]> subSet = set.tailSet(data[sortedOrder[start]]);
        SortedSet<byte[]> expected = new TreeSet<>(set.comparator());
        for (int i = start; i < sortedOrder.length; i++) {
            expected.add(data[sortedOrder[i]]);
        }
        assertEquals(expected, subSet);
    } catch (Exception e) {
    }
}

### 153.External Class Modification
link: https://github.com/Graylog2/graylog2-server/commit/b5a73d2f7f4ab10e97a951bcfec4bb661da149f4
p_path: graylog2-server/src/main/java/org/graylog2/indexer/migration/RemoteReindexMigration.java#progress
t_path: graylog2-server/src/test/java/org/graylog2/indexer/migration/RemoteReindexMigrationTest.java#testProgress

```java:test_src

@Test
void testProgress() {
    final RemoteReindexMigration migration = withIndices(new RemoteReindexIndex("one", RemoteReindexingMigrationAdapter.Status.FINISHED), new RemoteReindexIndex("two", RemoteReindexingMigrationAdapter.Status.FINISHED), new RemoteReindexIndex("three", RemoteReindexingMigrationAdapter.Status.ERROR), new RemoteReindexIndex("four", RemoteReindexingMigrationAdapter.Status.RUNNING), new RemoteReindexIndex("five", RemoteReindexingMigrationAdapter.Status.NOT_STARTED));
    Assertions.assertThat(migration.progress()).isEqualTo(60);
}

```java:test_tgt

@Test
void testProgress() {
    final RemoteReindexMigration migration = withIndices(index("one", RemoteReindexingMigrationAdapter.Status.FINISHED), index("two", RemoteReindexingMigrationAdapter.Status.FINISHED), index("three", RemoteReindexingMigrationAdapter.Status.ERROR), index("four", RemoteReindexingMigrationAdapter.Status.RUNNING), index("five", RemoteReindexingMigrationAdapter.Status.NOT_STARTED));
    Assertions.assertThat(migration.progress()).isEqualTo(60);
}

```java:llm_gen

@Test
void testProgress() {
    final RemoteReindexMigration migration = withIndices(new RemoteReindexIndex("one", RemoteReindexingMigrationAdapter.Status.FINISHED), new RemoteReindexIndex("two", RemoteReindexingMigrationAdapter.Status.FINISHED), new RemoteReindexIndex("three", RemoteReindexingMigrationAdapter.Status.ERROR), new RemoteReindexIndex("four", RemoteReindexingMigrationAdapter.Status.RUNNING), new RemoteReindexIndex("five", RemoteReindexingMigrationAdapter.Status.NOT_STARTED));
    Assertions.assertThat(migration.progress()).isEqualTo(66);
}

### 154.Partial Updates
link: https://github.com/ls1intum/Artemis/commit/002538346660b4500073790b06009a156a04c433
p_path: src/main/java/de/tum/in/www1/artemis/service/connectors/gitlabci/GitLabCIService.java#createBuildPlanForExercise
t_path: src/test/java/de/tum/in/www1/artemis/service/GitlabCIServiceTest.java#testCreateBuildPlanForExercise

```java:test_src

@Test
@WithMockUser(username = TEST_PREFIX + "instructor1", roles = "INSTRUCTOR")
void testCreateBuildPlanForExercise() throws GitLabApiException {
    final ProgrammingExercise exercise = programmingExerciseRepository.findByIdElseThrow(programmingExerciseId);
    final ProgrammingExerciseStudentParticipation participation = participationUtilService.addStudentParticipationForProgrammingExercise(exercise, TEST_PREFIX + "student1");
    final String repositoryPath = urlService.getRepositoryPathFromRepositoryUrl(participation.getVcsRepositoryUrl());
    mockAddBuildPlanToGitLabRepositoryConfiguration(false);
    continuousIntegrationService.createBuildPlanForExercise(exercise, "TEST-EXERCISE", participation.getVcsRepositoryUrl(), null, null);
    verify(gitlab, atLeastOnce()).getProjectApi();
    verify(gitlab.getProjectApi(), atLeastOnce()).getProject(eq(repositoryPath));
    verify(gitlab.getProjectApi(), atLeastOnce()).updateProject(any(Project.class));
    verify(gitlab.getProjectApi(), atLeastOnce()).createVariable(anyString(), anyString(), anyString(), any(), anyBoolean(), anyBoolean());
    var buildPlanOptional = buildPlanRepository.findByProgrammingExercises_IdWithProgrammingExercises(exercise.getId());
    assertThat(buildPlanOptional).isPresent();
    assertThat(buildPlanOptional.get().getBuildPlan()).isNotBlank();
}

```java:test_tgt

@Test
@WithMockUser(username = TEST_PREFIX + "instructor1", roles = "INSTRUCTOR")
void testCreateBuildPlanForExercise() throws GitLabApiException {
    final ProgrammingExercise exercise = programmingExerciseRepository.findByIdElseThrow(programmingExerciseId);
    final ProgrammingExerciseStudentParticipation participation = participationUtilService.addStudentParticipationForProgrammingExercise(exercise, TEST_PREFIX + "student1");
    final String repositoryPath = uriService.getRepositoryPathFromRepositoryUri(participation.getVcsRepositoryUri());
    mockAddBuildPlanToGitLabRepositoryConfiguration(false);
    continuousIntegrationService.createBuildPlanForExercise(exercise, "TEST-EXERCISE", participation.getVcsRepositoryUri(), null, null);
    verify(gitlab, atLeastOnce()).getProjectApi();
    verify(gitlab.getProjectApi(), atLeastOnce()).getProject(eq(repositoryPath));
    verify(gitlab.getProjectApi(), atLeastOnce()).updateProject(any(Project.class));
    verify(gitlab.getProjectApi(), atLeastOnce()).createVariable(anyString(), anyString(), anyString(), any(), anyBoolean(), anyBoolean());
    var buildPlanOptional = buildPlanRepository.findByProgrammingExercises_IdWithProgrammingExercises(exercise.getId());
    assertThat(buildPlanOptional).isPresent();
    assertThat(buildPlanOptional.get().getBuildPlan()).isNotBlank();
}

```java:llm_gen

@Test
@WithMockUser(username = TEST_PREFIX + "instructor1", roles = "INSTRUCTOR")
void testCreateBuildPlanForExercise() throws GitLabApiException {
    final ProgrammingExercise exercise = programmingExerciseRepository.findByIdElseThrow(programmingExerciseId);
    final ProgrammingExerciseStudentParticipation participation = participationUtilService.addStudentParticipationForProgrammingExercise(exercise, TEST_PREFIX + "student1");
    final String repositoryPath = urlService.getRepositoryPathFromRepositoryUrl(participation.getVcsRepositoryUrl());
    mockAddBuildPlanToGitLabRepositoryConfiguration(false);
    continuousIntegrationService.createBuildPlanForExercise(exercise, "TEST-EXERCISE", participation.getVcsRepositoryUri(), null, null);
    verify(gitlab, atLeastOnce()).getProjectApi();
    verify(gitlab.getProjectApi(), atLeastOnce()).getProject(eq(repositoryPath));
    verify(gitlab.getProjectApi(), atLeastOnce()).updateProject(any(Project.class));
    verify(gitlab.getProjectApi(), atLeastOnce()).createVariable(anyString(), anyString(), anyString(), any(), anyBoolean(), anyBoolean());
    var buildPlanOptional = buildPlanRepository.findByProgrammingExercises_IdWithProgrammingExercises(exercise.getId());
    assertThat(buildPlanOptional).isPresent();
    assertThat(buildPlanOptional.get().getBuildPlan()).isNotBlank();
}


### 155.Missing Asserts
link: https://github.com/apache/iceberg/commit/4c9f47d208b16921f825a66e24d0693f2b76b03b
p_path: kafka-connect/kafka-connect/src/main/java/org/apache/iceberg/connect/data/IcebergWriterFactory.java#autoCreateTable
t_path: kafka-connect/kafka-connect/src/test/java/org/apache/iceberg/connect/data/IcebergWriterFactoryTest.java#testAutoCreateTable

```java:test_src

@ParameterizedTest
@ValueSource(booleans = { true, false })
@SuppressWarnings("unchecked")
public void testAutoCreateTable(boolean partitioned) {
    Catalog catalog = mock(Catalog.class);
    when(catalog.loadTable(any())).thenThrow(new NoSuchTableException("no such table"));
    TableSinkConfig tableConfig = mock(TableSinkConfig.class);
    if (partitioned) {
        when(tableConfig.partitionBy()).thenReturn(ImmutableList.of("data"));
    }
    IcebergSinkConfig config = mock(IcebergSinkConfig.class);
    when(config.autoCreateProps()).thenReturn(ImmutableMap.of("test-prop", "foo1"));
    when(config.tableConfig(any())).thenReturn(tableConfig);
    SinkRecord record = mock(SinkRecord.class);
    when(record.value()).thenReturn(ImmutableMap.of("id", 123, "data", "foo2"));
    IcebergWriterFactory factory = new IcebergWriterFactory(catalog, config);
    factory.autoCreateTable("db.tbl", record);
    ArgumentCaptor<TableIdentifier> identCaptor = ArgumentCaptor.forClass(TableIdentifier.class);
    ArgumentCaptor<Schema> schemaCaptor = ArgumentCaptor.forClass(Schema.class);
    ArgumentCaptor<PartitionSpec> specCaptor = ArgumentCaptor.forClass(PartitionSpec.class);
    ArgumentCaptor<Map<String, String>> propsCaptor = ArgumentCaptor.forClass(Map.class);
    verify(catalog).createTable(identCaptor.capture(), schemaCaptor.capture(), specCaptor.capture(), propsCaptor.capture());
    assertThat(identCaptor.getValue()).isEqualTo(TableIdentifier.of("db", "tbl"));
    assertThat(schemaCaptor.getValue().findField("id").type()).isEqualTo(LongType.get());
    assertThat(schemaCaptor.getValue().findField("data").type()).isEqualTo(StringType.get());
    assertThat(specCaptor.getValue().isPartitioned()).isEqualTo(partitioned);
    assertThat(propsCaptor.getValue()).containsKey("test-prop");
}

```java:test_tgt

@ParameterizedTest
@ValueSource(booleans = { true, false })
@SuppressWarnings("unchecked")
public void testAutoCreateTable(boolean partitioned) {
    Catalog catalog = mock(Catalog.class, withSettings().extraInterfaces(SupportsNamespaces.class));
    when(catalog.loadTable(any())).thenThrow(new NoSuchTableException("no such table"));
    TableSinkConfig tableConfig = mock(TableSinkConfig.class);
    if (partitioned) {
        when(tableConfig.partitionBy()).thenReturn(ImmutableList.of("data"));
    }
    IcebergSinkConfig config = mock(IcebergSinkConfig.class);
    when(config.autoCreateProps()).thenReturn(ImmutableMap.of("test-prop", "foo1"));
    when(config.tableConfig(any())).thenReturn(tableConfig);
    SinkRecord record = mock(SinkRecord.class);
    when(record.value()).thenReturn(ImmutableMap.of("id", 123, "data", "foo2"));
    IcebergWriterFactory factory = new IcebergWriterFactory(catalog, config);
    factory.autoCreateTable("foo1.foo2.foo3.bar", record);
    ArgumentCaptor<TableIdentifier> identCaptor = ArgumentCaptor.forClass(TableIdentifier.class);
    ArgumentCaptor<Schema> schemaCaptor = ArgumentCaptor.forClass(Schema.class);
    ArgumentCaptor<PartitionSpec> specCaptor = ArgumentCaptor.forClass(PartitionSpec.class);
    ArgumentCaptor<Map<String, String>> propsCaptor = ArgumentCaptor.forClass(Map.class);
    verify(catalog).createTable(identCaptor.capture(), schemaCaptor.capture(), specCaptor.capture(), propsCaptor.capture());
    assertThat(identCaptor.getValue()).isEqualTo(TableIdentifier.of(Namespace.of("foo1", "foo2", "foo3"), "bar"));
    assertThat(schemaCaptor.getValue().findField("id").type()).isEqualTo(LongType.get());
    assertThat(schemaCaptor.getValue().findField("data").type()).isEqualTo(StringType.get());
    assertThat(specCaptor.getValue().isPartitioned()).isEqualTo(partitioned);
    assertThat(propsCaptor.getValue()).containsKey("test-prop");
    ArgumentCaptor<Namespace> namespaceCaptor = ArgumentCaptor.forClass(Namespace.class);
    verify((SupportsNamespaces) catalog, times(3)).createNamespace(namespaceCaptor.capture());
    List<Namespace> capturedArguments = namespaceCaptor.getAllValues();
    assertThat(capturedArguments.get(0)).isEqualTo(Namespace.of("foo1"));
    assertThat(capturedArguments.get(1)).isEqualTo(Namespace.of("foo1", "foo2"));
    assertThat(capturedArguments.get(2)).isEqualTo(Namespace.of("foo1", "foo2", "foo3"));
}

```java:llm_gen

@ParameterizedTest
@ValueSource(booleans = { true, false })
@SuppressWarnings("unchecked")
public void testAutoCreateTable(boolean partitioned) {
    Catalog catalog = mock(Catalog.class);
    when(catalog.loadTable(any())).thenThrow(new NoSuchTableException("no such table"));
    TableSinkConfig tableConfig = mock(TableSinkConfig.class);
    if (partitioned) {
        when(tableConfig.partitionBy()).thenReturn(ImmutableList.of("data"));
    }
    IcebergSinkConfig config = mock(IcebergSinkConfig.class);
    when(config.autoCreateProps()).thenReturn(ImmutableMap.of("test-prop", "foo1"));
    when(config.tableConfig(any())).thenReturn(tableConfig);
    SinkRecord record = mock(SinkRecord.class);
    when(record.value()).thenReturn(ImmutableMap.of("id", 123, "data", "foo2"));
    IcebergWriterFactory factory = new IcebergWriterFactory(catalog, config);
    factory.autoCreateTable("db.tbl", record);
    ArgumentCaptor<TableIdentifier> identCaptor = ArgumentCaptor.forClass(TableIdentifier.class);
    ArgumentCaptor<Schema> schemaCaptor = ArgumentCaptor.forClass(Schema.class);
    ArgumentCaptor<PartitionSpec> specCaptor = ArgumentCaptor.forClass(PartitionSpec.class);
    ArgumentCaptor<Map<String, String>> propsCaptor = ArgumentCaptor.forClass(Map.class);
    verify(catalog).createNamespaceIfNotExist(TableIdentifier.of("db", "tbl").namespace());
    verify(catalog).createTable(identCaptor.capture(), schemaCaptor.capture(), specCaptor.capture(), propsCaptor.capture());
    assertThat(identCaptor.getValue()).isEqualTo(TableIdentifier.of("db", "tbl"));
    assertThat(schemaCaptor.getValue().findField("id").type()).isEqualTo(LongType.get());
    assertThat(schemaCaptor.getValue().findField("data").type()).isEqualTo(StringType.get());
    assertThat(specCaptor.getValue().isPartitioned()).isEqualTo(partitioned);
    assertThat(propsCaptor.getValue()).containsKey("test-prop");
}

### 156.External File Modification
link: https://github.com/apache/dolphinscheduler/commit/7b9c9e0eb2d62da477943c918f0e36a6e800c1e3
p_path: dolphinscheduler-master/src/main/java/org/apache/dolphinscheduler/server/master/dispatch/host/assign/LowerWeightRoundRobin.java#doSelect
t_path: dolphinscheduler-master/src/test/java/org/apache/dolphinscheduler/server/master/dispatch/host/assign/LowerWeightRoundRobinTest.java#testDoSelect

```java:test_src

@Test
public void testDoSelect() {
    Collection<HostWeight> sources = new ArrayList<>();
    LowerWeightRoundRobin roundRobin = new LowerWeightRoundRobin();
    HostWeight result;
    result = roundRobin.doSelect(sources);
    Assertions.assertNull(result);
    sources.add(new HostWeight(HostWorker.of("192.158.2.1:11", 100, "default"), 0.06, 0.44, 3.14, 1, System.currentTimeMillis() - 60 * 8 * 1000));
    sources.add(new HostWeight(HostWorker.of("192.158.2.2:22", 100, "default"), 0.06, 0.56, 3.24, 2, System.currentTimeMillis() - 60 * 5 * 1000));
    sources.add(new HostWeight(HostWorker.of("192.158.2.3:33", 100, "default"), 0.06, 0.80, 3.15, 1, System.currentTimeMillis() - 60 * 2 * 1000));
    result = roundRobin.doSelect(sources);
    Assertions.assertEquals("192.158.2.1", result.getHost().getIp());
}

```java:test_tgt

@Test
public void testDoSelect() {
    Collection<HostWeight> sources = new ArrayList<>();
    LowerWeightRoundRobin roundRobin = new LowerWeightRoundRobin();
    HostWeight result;
    result = roundRobin.doSelect(sources);
    Assertions.assertNull(result);
    sources.add(new HostWeight(HostWorker.of("192.158.2.1:11", 100, "default"), 0.06, 0.44, 0.314, 0.1, System.currentTimeMillis() - 60 * 8 * 1000));
    sources.add(new HostWeight(HostWorker.of("192.158.2.2:22", 100, "default"), 0.06, 0.56, 0.324, 0.2, System.currentTimeMillis() - 60 * 5 * 1000));
    sources.add(new HostWeight(HostWorker.of("192.158.2.3:33", 100, "default"), 0.06, 0.80, 0.315, 0.1, System.currentTimeMillis() - 60 * 2 * 1000));
    result = roundRobin.doSelect(sources);
    Assertions.assertEquals("192.158.2.1", result.getHost().getIp());
}

```java:llm_gen

@Test
public void testDoSelect() {
    Collection<HostWeight> sources = new ArrayList<>();
    LowerWeightRoundRobin roundRobin = new LowerWeightRoundRobin();
    HostWeight result;
    result = roundRobin.doSelect(sources);
    Assertions.assertNull(result);
    sources.add(new HostWeight(HostWorker.of("192.158.2.1:11", 100, "default"), 0.06, 0.44, 3.14, 1, System.currentTimeMillis() - 60 * 8 * 1000));
    sources.add(new HostWeight(HostWorker.of("192.158.2.2:22", 100, "default"), 0.06, 0.56, 3.24, 2, System.currentTimeMillis() - 60 * 5 * 1000));
    sources.add(new HostWeight(HostWorker.of("192.158.2.3:33", 100, "default"), 0.06, 0.80, 3.15, 1, System.currentTimeMillis() - 60 * 2 * 1000));
    result = roundRobin.doSelect(sources);
    Assertions.assertEquals("192.158.2.1", result.getHost().getIp());
}

### 157.External Function Modification
link: https://github.com/apache/commons-collections/commit/4a2aa76d4bafd3ac7992844aa15dbcabd76b26d8
p_path: src/main/java/org/apache/commons/collections4/bloomfilter/SetOperations.java#orCardinality
t_path: src/test/java/org/apache/commons/collections4/bloomfilter/SetOperationsTest.java#testOrCardinality

```java:test_src

@Test
public final void testOrCardinality() {
    final Shape shape = Shape.fromKM(3, 128);
    BloomFilter filter1 = createFilter(shape, IndexProducer.fromIndexArray(1, 63, 64));
    BloomFilter filter2 = createFilter(shape, IndexProducer.fromIndexArray(5, 64, 69));
    assertSymmetricOperation(5, SetOperations::orCardinality, filter1, filter2);
    filter1 = createFilter(shape, IndexProducer.fromIndexArray(1, 63));
    filter2 = createFilter(shape, IndexProducer.fromIndexArray(5, 64, 69));
    assertSymmetricOperation(5, SetOperations::orCardinality, filter1, filter2);
    filter1 = createFilter(shape, IndexProducer.fromIndexArray(5, 63));
    filter2 = createFilter(shape, IndexProducer.fromIndexArray(5, 64, 69));
    assertSymmetricOperation(4, SetOperations::orCardinality, filter1, filter2);
}

```java:test_tgt

@Test
public final void testOrCardinality() {
    final Shape shape = Shape.fromKM(3, 128);
    BloomFilter filter1 = createFilter(shape, IndexExtractor.fromIndexArray(1, 63, 64));
    BloomFilter filter2 = createFilter(shape, IndexExtractor.fromIndexArray(5, 64, 69));
    assertSymmetricOperation(5, SetOperations::orCardinality, filter1, filter2);
    filter1 = createFilter(shape, IndexExtractor.fromIndexArray(1, 63));
    filter2 = createFilter(shape, IndexExtractor.fromIndexArray(5, 64, 69));
    assertSymmetricOperation(5, SetOperations::orCardinality, filter1, filter2);
    filter1 = createFilter(shape, IndexExtractor.fromIndexArray(5, 63));
    filter2 = createFilter(shape, IndexExtractor.fromIndexArray(5, 64, 69));
    assertSymmetricOperation(4, SetOperations::orCardinality, filter1, filter2);
}

```java:llm_gen

@Test
public final void testOrCardinality() {
    final Shape shape = Shape.fromKM(3, 128);
    BloomFilter filter1 = createFilter(shape, IndexProducer.fromIndexArray(1, 63, 64));
    BloomFilter filter2 = createFilter(shape, IndexProducer.fromIndexArray(5, 64, 69));
    assertSymmetricOperation(5, SetOperations::orCardinality, filter1, filter2);
    filter1 = createFilter(shape, IndexProducer.fromIndexArray(1, 63));
    filter2 = createFilter(shape, IndexProducer.fromIndexArray(5, 64, 69));
    assertSymmetricOperation(5, SetOperations::orCardinality, filter1, filter2);
    filter1 = createFilter(shape, IndexProducer.fromIndexArray(5, 63));
    filter2 = createFilter(shape, IndexProducer.fromIndexArray(5, 64, 69));
    assertSymmetricOperation(4, SetOperations::orCardinality, filter1, filter2);
    filter1 = createFilter(shape, IndexProducer.fromIndexArray(1, 2, 3));
    filter2 = createFilter(shape, IndexProducer.fromIndexArray(4, 5, 6));
    assertSymmetricOperation(6, SetOperations::orCardinality, filter1, filter2);
}

### 158.Missing Asserts
link: https://github.com/iterate-ch/cyberduck/commit/914ac407f70a03651a40d40c5584d8ca207566b3
p_path: core/src/main/java/ch/cyberduck/core/PathRelativizer.java#relativize
t_path: core/src/test/java/ch/cyberduck/core/PathRelativizerTest.java#testRelativize

```java:test_src

@Test
public void testRelativize() {
    assertEquals("", PathRelativizer.relativize("/r", "/r"));
    assertEquals("/", PathRelativizer.relativize("/r", "/r//"));
    assertEquals("a", PathRelativizer.relativize("/", "/a"));
    assertEquals("/b/path", PathRelativizer.relativize("/a", "/b/path"));
    assertEquals("path", PathRelativizer.relativize("/a", "/a/path"));
    assertEquals("path/", PathRelativizer.relativize("/a", "/a/path/"));
    assertEquals("a/path", PathRelativizer.relativize("public_html", "/home/user/public_html/a/path"));
    assertEquals("/home/user/public_html/a/path", PathRelativizer.relativize(null, "/home/user/public_html/a/path"));
}

```java:test_tgt

@Test
public void testRelativize() {
    assertEquals("", PathRelativizer.relativize("/r", "/r"));
    assertEquals("/", PathRelativizer.relativize("/r", "/r//"));
    assertEquals("a", PathRelativizer.relativize("/", "/a"));
    assertEquals("/b/path", PathRelativizer.relativize("/a", "/b/path"));
    assertEquals("path", PathRelativizer.relativize("/a", "/a/path"));
    assertEquals("path", PathRelativizer.relativize("/a/", "/a/path"));
    assertEquals("path/", PathRelativizer.relativize("/a", "/a/path/"));
    assertEquals("a/path", PathRelativizer.relativize("public_html", "/home/user/public_html/a/path"));
    assertEquals("/home/user/public_html/a/path", PathRelativizer.relativize(null, "/home/user/public_html/a/path"));
}

```java:llm_gen

@Test
public void testRelativize() {
    assertEquals("", PathRelativizer.relativize("/r", "/r"));
    assertEquals("", PathRelativizer.relativize("/r/", "/r/"));
    assertEquals("a", PathRelativizer.relativize("/", "/a"));
    assertEquals("/b/path", PathRelativizer.relativize("/a", "/b/path"));
    assertEquals("path", PathRelativizer.relativize("/a", "/a/path"));
    assertEquals("path/", PathRelativizer.relativize("/a", "/a/path/"));
    assertEquals("a/path", PathRelativizer.relativize("public_html", "/home/user/public_html/a/path"));
    assertEquals("/home/user/public_html/a/path", PathRelativizer.relativize(null, "/home/user/public_html/a/path"));
}

### 159.External File Modification
link: https://github.com/rsksmart/rskj/commit/7b0652ea082b48a992d12021642765db595574de
p_path: rskj-core/src/main/java/co/rsk/config/RskSystemProperties.java#gasPriceBuffer
t_path: rskj-core/src/test/java/co/rsk/config/RskSystemPropertiesTest.java#testGasPriceBuffer

```java:test_src

@Test
void testGasPriceBuffer() {
    assertEquals(BigInteger.valueOf(5), config.gasPriceBuffer());
}

```java:test_tgt

@Test
void testGasPriceBuffer() {
    assertEquals(BigInteger.valueOf(105), config.gasPriceBuffer());
}

```java:llm_gen

@Test
void testGasPriceBuffer() {
    when(config.getInt(eq("miner.gasPriceBuffer"), anyInt())).thenReturn(110);
    assertEquals(BigInteger.valueOf(110), config.gasPriceBuffer());
}


### 160.Test Preparation Error
link: https://github.com/apache/shenyu/commit/c6323c01e47e249329d683cdfde56d2e793bb935
p_path: shenyu-admin/src/main/java/org/apache/shenyu/admin/service/register/AbstractContextPathRegisterService.java#registerContextPath
t_path: shenyu-admin/src/test/java/org/apache/shenyu/admin/service/register/AbstractContextPathRegisterServiceTest.java#testRegisterContextPath

```java:test_src

@Test
public void testRegisterContextPath() {
    MetaDataRegisterDTO dto = MetaDataRegisterDTO.builder().build();
    dto.setContextPath("Context_Path");
    dto.setAddPrefixed(true);
    RegisterExecutionLock registerExecutionLock = mock(RegisterExecutionLock.class);
    when(selectorService.registerDefault(dto, PluginEnum.CONTEXT_PATH.getName(), "")).thenReturn("Context_Path_Selector_Id");
    when(registerExecutionRepository.getLock(any())).thenReturn(registerExecutionLock);
    abstractContextPathRegisterService.registerContextPath(dto);
    verify(ruleService).registerDefault(any());
}

```java:test_tgt

@Test
public void testRegisterContextPath() {
    MetaDataRegisterDTO dto = MetaDataRegisterDTO.builder().build();
    dto.setContextPath("Context_Path");
    dto.setAddPrefixed(true);
    when(selectorService.registerDefault(dto, PluginEnum.CONTEXT_PATH.getName(), "")).thenReturn("Context_Path_Selector_Id");
    // org.springframework.integration.jdbc.lock.JdbcLockRegistry.JdbcLock is private and cannot be mocked directly so we mock the LockRegistry and return a mock MockLock
    // here  mock ReentrantLock   cause cpu usage 100% in the jdk 19 20 21 environment
    when(registry.obtain(any())).thenReturn(mock(MockLock.class));
    when(ruleService.findBySelectorIdAndName("Context_Path_Selector_Id", "Context_Path")).thenReturn(null);
    when(ruleService.registerDefault(any())).thenReturn("Context_Path_Rule_Id");
    abstractContextPathRegisterService.registerContextPath(dto);
    verify(ruleService).registerDefault(any());
}

```java:llm_gen

@Test
public void testRegisterContextPath() {
    MetaDataRegisterDTO dto = MetaDataRegisterDTO.builder().build();
    dto.setContextPath("Context_Path");
    dto.setAddPrefixed(true);
    Lock lock = mock(Lock.class);
    when(registry.obtain(any())).thenReturn(lock);
    when(selectorService.registerDefault(dto, PluginEnum.CONTEXT_PATH.getName(), "")).thenReturn("Context_Path_Selector_Id");
    abstractContextPathRegisterService.registerContextPath(dto);
    verify(ruleService).registerDefault(any());
}

### 161.Test Preparation Error
link: https://github.com/apache/iceberg/commit/e1f50fd3505b48e37f98049f8ea243aa9f1e08dd
p_path: core/src/main/java/org/apache/iceberg/jdbc/JdbcCatalog.java#initialize
t_path: core/src/test/java/org/apache/iceberg/jdbc/TestJdbcCatalog.java#testInitialize

```java:test_src

@Test
public void testInitialize() {
    Map<String, String> properties = Maps.newHashMap();
    properties.put(CatalogProperties.WAREHOUSE_LOCATION, this.tableDir.toAbsolutePath().toString());
    properties.put(CatalogProperties.URI, "jdbc:sqlite:file::memory:?icebergDB");
    JdbcCatalog jdbcCatalog = new JdbcCatalog();
    jdbcCatalog.setConf(conf);
    jdbcCatalog.initialize("test_jdbc_catalog", properties);
    jdbcCatalog.initialize("test_jdbc_catalog", properties);
    jdbcCatalog.initialize("test_jdbc_catalog", properties);
}

```java:test_tgt

@Test
public void testInitialize() {
    Map<String, String> properties = Maps.newHashMap();
    properties.put(CatalogProperties.WAREHOUSE_LOCATION, this.tableDir.toAbsolutePath().toString());
    properties.put(CatalogProperties.URI, "jdbc:sqlite:file::memory:?icebergDB");
    properties.put(JdbcUtil.SCHEMA_VERSION_PROPERTY, JdbcUtil.SchemaVersion.V1.name());
    JdbcCatalog jdbcCatalog = new JdbcCatalog();
    jdbcCatalog.setConf(conf);
    jdbcCatalog.initialize("test_jdbc_catalog", properties);
    jdbcCatalog.initialize("test_jdbc_catalog", properties);
    jdbcCatalog.initialize("test_jdbc_catalog", properties);
}

```java:llm_gen

@Test
public void testInitialize() {
    Map<String, String> properties = Maps.newHashMap();
    properties.put(CatalogProperties.WAREHOUSE_LOCATION, this.tableDir.toAbsolutePath().toString());
    properties.put(CatalogProperties.URI, "jdbc:sqlite:file::memory:?icebergDB");
    JdbcCatalog jdbcCatalog = new JdbcCatalog();
    jdbcCatalog.setConf(conf);
    jdbcCatalog.initialize("test_jdbc_catalog", properties);
    jdbcCatalog.initialize("test_jdbc_catalog", properties);
    jdbcCatalog.initialize("test_jdbc_catalog", properties);
    assertNotNull(jdbcCatalog.getCloseableGroup());
    assertTrue(jdbcCatalog.getCloseableGroup().getSuppressCloseFailure());
}

### 162.Test Preparation Error
link: https://github.com/apache/incubator-pinot/commit/7b69d094be7bc410d4bf8fe15e4c30233421e300
p_path: pinot-plugins/pinot-minion-tasks/pinot-minion-builtin-tasks/src/main/java/org/apache/pinot/plugin/minion/tasks/upsertcompaction/UpsertCompactionTaskGenerator.java#processValidDocIdMetadata
t_path: pinot-plugins/pinot-minion-tasks/pinot-minion-builtin-tasks/src/test/java/org/apache/pinot/plugin/minion/tasks/upsertcompaction/UpsertCompactionTaskGeneratorTest.java#testProcessValidDocIdMetadata

```java:test_src

@Test
public void testProcessValidDocIdMetadata() {
    Map<String, String> compactionConfigs = getCompactionConfigs("1", "10");
    Set<Map.Entry<String, String>> responseSet = new HashSet<>();
    String json = "[{" + "\"totalValidDocs\" : 50," + "\"totalInvalidDocs\" : 50," + "\"segmentName\" : \"" + _completedSegment.getSegmentName() + "\"," + "\"totalDocs\" : 100" + "}," + "{" + "\"totalValidDocs\" : 0," + "\"totalInvalidDocs\" : 10," + "\"segmentName\" : \"" + _completedSegment2.getSegmentName() + "\"," + "\"totalDocs\" : 10" + "}]";
    responseSet.add(new AbstractMap.SimpleEntry<>("", json));
    UpsertCompactionTaskGenerator.SegmentSelectionResult segmentSelectionResult = UpsertCompactionTaskGenerator.processValidDocIdMetadata(compactionConfigs, _completedSegmentsMap, responseSet);
    assertEquals(segmentSelectionResult.getSegmentsForCompaction().get(0).getSegmentName(), _completedSegment.getSegmentName());
    assertEquals(segmentSelectionResult.getSegmentsForDeletion().get(0), _completedSegment2.getSegmentName());
    compactionConfigs = getCompactionConfigs("60", "10");
    segmentSelectionResult = UpsertCompactionTaskGenerator.processValidDocIdMetadata(compactionConfigs, _completedSegmentsMap, responseSet);
    assertTrue(segmentSelectionResult.getSegmentsForCompaction().isEmpty());
    compactionConfigs = getCompactionConfigs("0", "10");
    segmentSelectionResult = UpsertCompactionTaskGenerator.processValidDocIdMetadata(compactionConfigs, _completedSegmentsMap, responseSet);
    assertEquals(segmentSelectionResult.getSegmentsForCompaction().get(0).getSegmentName(), _completedSegment.getSegmentName());
    compactionConfigs = getCompactionConfigs("30", "0");
    segmentSelectionResult = UpsertCompactionTaskGenerator.processValidDocIdMetadata(compactionConfigs, _completedSegmentsMap, responseSet);
    assertEquals(segmentSelectionResult.getSegmentsForCompaction().get(0).getSegmentName(), _completedSegment.getSegmentName());
}

```java:test_tgt

@Test
public void testProcessValidDocIdMetadata() throws IOException {
    Map<String, String> compactionConfigs = getCompactionConfigs("1", "10");
    List<ValidDocIdMetadataInfo> validDocIdMetadataInfoList = new ArrayList<>();
    String json = "[{" + "\"totalValidDocs\" : 50," + "\"totalInvalidDocs\" : 50," + "\"segmentName\" : \"" + _completedSegment.getSegmentName() + "\"," + "\"totalDocs\" : 100" + "}," + "{" + "\"totalValidDocs\" : 0," + "\"totalInvalidDocs\" : 10," + "\"segmentName\" : \"" + _completedSegment2.getSegmentName() + "\"," + "\"totalDocs\" : 10" + "}]";
    List<ValidDocIdMetadataInfo> validDocIdMetadataInfo = JsonUtils.stringToObject(json, new TypeReference<ArrayList<ValidDocIdMetadataInfo>>() {
    });
    UpsertCompactionTaskGenerator.SegmentSelectionResult segmentSelectionResult = UpsertCompactionTaskGenerator.processValidDocIdMetadata(compactionConfigs, _completedSegmentsMap, validDocIdMetadataInfo);
    assertEquals(segmentSelectionResult.getSegmentsForCompaction().get(0).getSegmentName(), _completedSegment.getSegmentName());
    assertEquals(segmentSelectionResult.getSegmentsForDeletion().get(0), _completedSegment2.getSegmentName());
    compactionConfigs = getCompactionConfigs("60", "10");
    segmentSelectionResult = UpsertCompactionTaskGenerator.processValidDocIdMetadata(compactionConfigs, _completedSegmentsMap, validDocIdMetadataInfo);
    assertTrue(segmentSelectionResult.getSegmentsForCompaction().isEmpty());
    compactionConfigs = getCompactionConfigs("0", "10");
    segmentSelectionResult = UpsertCompactionTaskGenerator.processValidDocIdMetadata(compactionConfigs, _completedSegmentsMap, validDocIdMetadataInfo);
    assertEquals(segmentSelectionResult.getSegmentsForCompaction().get(0).getSegmentName(), _completedSegment.getSegmentName());
    compactionConfigs = getCompactionConfigs("30", "0");
    segmentSelectionResult = UpsertCompactionTaskGenerator.processValidDocIdMetadata(compactionConfigs, _completedSegmentsMap, validDocIdMetadataInfo);
    assertEquals(segmentSelectionResult.getSegmentsForCompaction().get(0).getSegmentName(), _completedSegment.getSegmentName());
}

```java:llm_gen

@Test
public void testProcessValidDocIdMetadata() {
    Map<String, String> compactionConfigs = getCompactionConfigs("1", "10");
    List<ValidDocIdMetadataInfo> validDocIdMetadataInfoList = new ArrayList<>();
    validDocIdMetadataInfoList.add(new ValidDocIdMetadataInfo(_completedSegment.getSegmentName(), 50, 100));
    validDocIdMetadataInfoList.add(new ValidDocIdMetadataInfo(_completedSegment2.getSegmentName(), 10, 10));
    UpsertCompactionTaskGenerator.SegmentSelectionResult segmentSelectionResult = UpsertCompactionTaskGenerator.processValidDocIdMetadata(compactionConfigs, _completedSegmentsMap, validDocIdMetadataInfoList);
    assertEquals(segmentSelectionResult.getSegmentsForCompaction().get(0).getSegmentName(), _completedSegment.getSegmentName());
    assertEquals(segmentSelectionResult.getSegmentsForDeletion().get(0), _completedSegment2.getSegmentName());
    compactionConfigs = getCompactionConfigs("60", "10");
    segmentSelectionResult = UpsertCompactionTaskGenerator.processValidDocIdMetadata(compactionConfigs, _completedSegmentsMap, validDocIdMetadataInfoList);
    assertTrue(segmentSelectionResult.getSegmentsForCompaction().isEmpty());
    compactionConfigs = getCompactionConfigs("0", "10");
    segmentSelectionResult = UpsertCompactionTaskGenerator.processValidDocIdMetadata(compactionConfigs, _completedSegmentsMap, validDocIdMetadataInfoList);
    assertEquals(segmentSelectionResult.getSegmentsForCompaction().get(0).getSegmentName(), _completedSegment.getSegmentName());
    compactionConfigs = getCompactionConfigs("30", "0");
    segmentSelectionResult = UpsertCompactionTaskGenerator.processValidDocIdMetadata(compactionConfigs, _completedSegmentsMap, validDocIdMetadataInfoList);
    assertEquals(segmentSelectionResult.getSegmentsForCompaction().get(0).getSegmentName(), _completedSegment.getSegmentName());
}


### 163.External Function Modification
link: https://github.com/BentoBoxWorld/BentoBox/commit/b734d579a1d6bba9acdcb8a219bf089d5a1a066b
p_path: src/main/java/world/bentobox/bentobox/api/commands/admin/range/AdminRangeSetCommand.java#execute
t_path: src/test/java/world/bentobox/bentobox/api/commands/admin/range/AdminRangeSetCommandTest.java#testExecute

```java:test_src

@Test
public void testExecute() {
    when(pm.getUUID(Mockito.anyString())).thenReturn(uuid);
    AdminRangeSetCommand arc = new AdminRangeSetCommand(ac);
    List<String> args = new ArrayList<>();
    args.add("tastybento");
    args.add("48");
    arc.execute(user, "", args);
    Mockito.verify(user).sendMessage("commands.admin.range.set.success", TextVariables.NUMBER, "48");
}

```java:test_tgt

@Test
public void testExecute() {
    when(pm.getUUID(anyString())).thenReturn(uuid);
    AdminRangeSetCommand arc = new AdminRangeSetCommand(ac);
    List<String> args = new ArrayList<>();
    args.add("tastybento");
    args.add("48");
    assertTrue(arc.canExecute(user, "", args));
    assertTrue(arc.execute(user, "", args));
    verify(user).sendMessage("commands.admin.range.set.success", TextVariables.NUMBER, "48");
}

```java:llm_gen

@Test
public void testExecute() {
    when(pm.getUUID(Mockito.anyString())).thenReturn(uuid);
    when(getIslands().hasIsland(getWorld(), uuid)).thenReturn(true);
    when(getIslands().getIsland(getWorld(), uuid)).thenReturn(island);
    when(island.getRange()).thenReturn(50);
    when(island.getProtectionRange()).thenReturn(20);
    AdminRangeSetCommand arc = new AdminRangeSetCommand(ac);
    List<String> args = new ArrayList<>();
    args.add("tastybento");
    args.add("48");
    arc.execute(user, "", args);
    Mockito.verify(user).sendMessage("commands.admin.range.set.success", TextVariables.NUMBER, "48");
}


### 164.External Function Modification
link: https://github.com/thingsboard/thingsboard/commit/1e83e458f6cb6702129d3d7b4909e40961af0f81
p_path: dao/src/main/java/org/thingsboard/server/dao/service/Validator.java#validateIds
t_path: dao/src/test/java/org/thingsboard/server/dao/service/ValidatorTest.java#validateIdsTest

```java:test_src

@Test
void validateIdsTest() {
    List<? extends UUIDBased> list = List.of(goodDeviceId);
    Validator.validateIds(list, ids -> "Incorrect Id " + ids);
    assertThatThrownBy(() -> Validator.validateIds(null, id -> "Incorrect Ids " + id)).as("Ids are null").isInstanceOf(IncorrectParameterException.class).hasMessageContaining("Incorrect Ids null");
    assertThatThrownBy(() -> Validator.validateIds(Collections.emptyList(), ids -> "Incorrect Ids " + ids)).as("List is empty").isInstanceOf(IncorrectParameterException.class).hasMessageContaining("Incorrect Ids []");
    List<DeviceId> badList = new ArrayList<>(2);
    badList.add(goodDeviceId);
    badList.add(null);
    assertThatThrownBy(() -> Validator.validateIds(badList, ids -> "Incorrect Ids " + ids)).as("List contains null").isInstanceOf(IncorrectParameterException.class).hasMessageContaining("Incorrect Ids ").hasMessageContaining(goodDeviceId.getId().toString()).hasMessageContaining("null");
}

```java:test_tgt

@Test
void validateIdsTest() {
    List<? extends UUIDBased> list = List.of(goodDeviceId);
    Validator.validateIds(list, ids -> "Incorrect Id " + ids);
    assertThatThrownBy(() -> Validator.validateIds(null, id -> "Incorrect Ids " + id)).as("Ids are null").isInstanceOf(IncorrectParameterException.class).hasMessageContaining("Incorrect Ids null");
    assertThatThrownBy(() -> Validator.validateIds(Collections.emptyList(), ids -> "Incorrect Ids " + ids)).as("List is empty").isInstanceOf(IncorrectParameterException.class).hasMessageContaining("Incorrect Ids []");
    List<UUIDBased> badList = new ArrayList<>(2);
    badList.add(goodDeviceId);
    badList.add(null);
    assertThatThrownBy(() -> Validator.validateIds(badList, ids -> "Incorrect Ids " + ids)).as("List contains null").isInstanceOf(IncorrectParameterException.class).hasMessageContaining("Incorrect Ids ").hasMessageContaining(goodDeviceId.getId().toString()).hasMessageContaining("null");
}

```java:llm_gen

@Test
void validateIdsTest() {
    List<? extends UUIDBased> list = List.of(goodDeviceId);
    Validator.validateIds(list, ids -> "Incorrect Id " + ids);
    assertThatThrownBy(() -> Validator.validateIds(null, id -> "Incorrect Ids " + id)).as("Ids are null").isInstanceOf(IncorrectParameterException.class).hasMessageContaining("Incorrect Ids null");
    assertThatThrownBy(() -> Validator.validateIds(Collections.emptyList(), ids -> "Incorrect Ids " + ids)).as("List is empty").isInstanceOf(IncorrectParameterException.class).hasMessageContaining("Incorrect Ids []");
    List<DeviceId> badList = new ArrayList<>(2);
    badList.add(goodDeviceId);
    badList.add(null);
    assertThatThrownBy(() -> Validator.validateIds(badList, ids -> "Incorrect Ids " + ids)).as("List contains null").isInstanceOf(IncorrectParameterException.class).hasMessageContaining("Incorrect Ids ").hasMessageContaining(goodDeviceId.getId().toString()).hasMessageContaining("null");
}

### 165.Correct
link: https://github.com/StarRocks/starrocks/commit/9e11e613a3483de068ee383c8e4e6f4fd70f8ead
p_path: fe/fe-core/src/main/java/com/starrocks/transaction/GlobalTransactionMgr.java#beginTransaction
t_path: fe/fe-core/src/test/java/com/starrocks/transaction/GlobalTransactionMgrTest.java#testBeginTransaction

```java:test_src

@Test
public void testBeginTransaction() throws LabelAlreadyUsedException, AnalysisException, BeginTransactionException, DuplicatedRequestException {
    FakeGlobalStateMgr.setGlobalStateMgr(masterGlobalStateMgr);
    long transactionId = masterTransMgr.beginTransaction(GlobalStateMgrTestUtil.testDbId1, Lists.newArrayList(GlobalStateMgrTestUtil.testTableId1), GlobalStateMgrTestUtil.testTxnLable1, transactionSource, LoadJobSourceType.FRONTEND, Config.stream_load_default_timeout_second);
    TransactionState transactionState = masterTransMgr.getTransactionState(GlobalStateMgrTestUtil.testDbId1, transactionId);
    assertNotNull(transactionState);
    assertEquals(transactionId, transactionState.getTransactionId());
    assertEquals(TransactionStatus.PREPARE, transactionState.getTransactionStatus());
    assertEquals(GlobalStateMgrTestUtil.testDbId1, transactionState.getDbId());
    assertEquals(transactionSource.toString(), transactionState.getCoordinator().toString());
}

```java:test_tgt

@Test
public void testBeginTransaction() throws LabelAlreadyUsedException, AnalysisException, RunningTxnExceedException, DuplicatedRequestException {
    FakeGlobalStateMgr.setGlobalStateMgr(masterGlobalStateMgr);
    long transactionId = masterTransMgr.beginTransaction(GlobalStateMgrTestUtil.testDbId1, Lists.newArrayList(GlobalStateMgrTestUtil.testTableId1), GlobalStateMgrTestUtil.testTxnLable1, transactionSource, LoadJobSourceType.FRONTEND, Config.stream_load_default_timeout_second);
    TransactionState transactionState = masterTransMgr.getTransactionState(GlobalStateMgrTestUtil.testDbId1, transactionId);
    assertNotNull(transactionState);
    assertEquals(transactionId, transactionState.getTransactionId());
    assertEquals(TransactionStatus.PREPARE, transactionState.getTransactionStatus());
    assertEquals(GlobalStateMgrTestUtil.testDbId1, transactionState.getDbId());
    assertEquals(transactionSource.toString(), transactionState.getCoordinator().toString());
}

```java:llm_gen

@Test
public void testBeginTransaction() throws LabelAlreadyUsedException, AnalysisException, RunningTxnExceedException, DuplicatedRequestException {
    FakeGlobalStateMgr.setGlobalStateMgr(masterGlobalStateMgr);
    long transactionId = masterTransMgr.beginTransaction(GlobalStateMgrTestUtil.testDbId1, Lists.newArrayList(GlobalStateMgrTestUtil.testTableId1), GlobalStateMgrTestUtil.testTxnLable1, transactionSource, LoadJobSourceType.FRONTEND, Config.stream_load_default_timeout_second);
    TransactionState transactionState = masterTransMgr.getTransactionState(GlobalStateMgrTestUtil.testDbId1, transactionId);
    assertNotNull(transactionState);
    assertEquals(transactionId, transactionState.getTransactionId());
    assertEquals(TransactionStatus.PREPARE, transactionState.getTransactionStatus());
    assertEquals(GlobalStateMgrTestUtil.testDbId1, transactionState.getDbId());
    assertEquals(transactionSource.toString(), transactionState.getCoordinator().toString());
}

### 166.Wrong Update Direction
link: https://github.com/apache/incubator-fury/commit/e9678c5352365114733bef7bd1df1aa2645a8948
p_path: java/fury-core/src/main/java/org/apache/fury/collection/ObjectArray.java#clearObjectArray
t_path: java/fury-core/src/test/java/org/apache/fury/collection/ObjectArrayTest.java#testClearObjectArray

```java:test_src

@Test
public void testClearObjectArray() {
   int[] numObjs = new int[] { 100, 500, 1000, 5000, 10000, 100000, 1000000 };
   for (int numObj : numObjs) {
       Object[] array = new Object[numObj];
       Object o = new Object();
       for (int i = 0; i < numObj; i++) {
           array[i] = o;
       }
       ObjectArray.clearObjectArray(array, 0, array.length);
       for (int i = 0; i < array.length; i++) {
           Object value = array[i];
           if (value != null) {
               throw new IllegalStateException(String.format("numObj: %d, index: %d", numObj, i));
           }
       }
   }
}

```java:test_tgt

@Test
public void testClearObjectArray() {
   int[] numObjs = new int[] { 100, 500, 1000, 5000, 10000, 100000, 1000000 };
   for (int numObj : numObjs) {
       Object[] array = new Object[numObj];
       Object o = new Object();
       for (int i = 0; i < numObj; i++) {
           array[i] = o;
       }
       ObjectArray.clearObjectArray(array, 0, array.length);
       for (int i = 0; i < array.length; i++) {
           Object value = array[i];
           if (value != null) {
               throw new IllegalStateException(String.format("numObj: %d, index: %d", numObj, i));
           }
       }
       for (int i = 0; i < numObj; i++) {
           array[i] = o;
       }
       ObjectArray.clearObjectArray(array, 1, array.length - 1);
       for (int i = 1; i < array.length; i++) {
           Object value = array[i];
           if (value != null) {
               throw new IllegalStateException(String.format("numObj: %d, index: %d", numObj, i));
           }
       }
   }
}

```java:llm_gen

@Test
public void testClearObjectArray() {
   int[] numObjs = new int[] { 100, 500, 1000, 5000, 10000, 100000, 1000000 };
   for (int numObj : numObjs) {
       Object[] array = new Object[numObj];
       Object o = new Object();
       for (int i = 0; i < numObj; i++) {
           array[i] = o;
       }
       ObjectArray.clearObjectArray(array, 0, numObj);
       for (int i = 0; i < numObj; i++) {
           Object value = array[i];
           if (value != null) {
               throw new IllegalStateException(String.format("numObj: %d, index: %d", numObj, i));
           }
       }
   }
}

### 167.Correct
link: https://github.com/StarRocks/starrocks/commit/309bc24639a15392b09bccdf8f2aa5cdc920608f
p_path: fe/fe-core/src/main/java/com/starrocks/server/GlobalStateMgr.java#canSkipBadReplayedJournal
t_path: fe/fe-core/src/test/java/com/starrocks/server/GlobalStateMgrTest.java#testCanSkipBadReplayedJournal

```java:test_src

@Test
public void testCanSkipBadReplayedJournal() {
   boolean originVal = Config.metadata_journal_ignore_replay_failure;
   Config.metadata_journal_ignore_replay_failure = false;
   Assert.assertFalse(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalException(OperationType.OP_ADD_ANALYZE_STATUS, "failed")));
   Assert.assertFalse(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalException(OperationType.OP_CREATE_DB_V2, "failed")));
   Assert.assertFalse(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalInconsistentException(OperationType.OP_ADD_ANALYZE_STATUS, "failed")));
   Assert.assertFalse(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalInconsistentException(OperationType.OP_CREATE_DB_V2, "failed")));
   Config.metadata_journal_ignore_replay_failure = true;
   Assert.assertTrue(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalException(OperationType.OP_ADD_ANALYZE_STATUS, "failed")));
   Assert.assertFalse(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalException(OperationType.OP_CREATE_DB_V2, "failed")));
   Assert.assertTrue(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalInconsistentException(OperationType.OP_ADD_ANALYZE_STATUS, "failed")));
   Assert.assertFalse(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalInconsistentException(OperationType.OP_CREATE_DB_V2, "failed")));
   Config.metadata_journal_ignore_replay_failure = originVal;
}

```java:test_tgt

@Test
public void testCanSkipBadReplayedJournal() {
   boolean originVal = Config.metadata_journal_ignore_replay_failure;
   Config.metadata_journal_ignore_replay_failure = false;
   Assert.assertFalse(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalException(OperationType.OP_ADD_ANALYZE_STATUS, "failed")));
   Assert.assertFalse(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalException(OperationType.OP_CREATE_DB_V2, "failed")));
   Assert.assertFalse(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalInconsistentException(OperationType.OP_ADD_ANALYZE_STATUS, "failed")));
   Assert.assertFalse(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalInconsistentException(OperationType.OP_CREATE_DB_V2, "failed")));
   Config.metadata_journal_ignore_replay_failure = true;
   Assert.assertTrue(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalException(OperationType.OP_ADD_ANALYZE_STATUS, "failed")));
   Assert.assertFalse(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalException(OperationType.OP_CREATE_DB_V2, "failed")));
   Assert.assertTrue(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalInconsistentException(OperationType.OP_ADD_ANALYZE_STATUS, "failed")));
   Assert.assertFalse(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalInconsistentException(OperationType.OP_CREATE_DB_V2, "failed")));
   Config.metadata_journal_ignore_replay_failure = originVal;
   originVal = Config.metadata_enable_recovery_mode;
   Config.metadata_enable_recovery_mode = true;
   Assert.assertTrue(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalException(OperationType.OP_ADD_ANALYZE_STATUS, "failed")));
   Assert.assertTrue(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalException(OperationType.OP_CREATE_DB_V2, "failed")));
   Assert.assertTrue(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalInconsistentException(OperationType.OP_ADD_ANALYZE_STATUS, "failed")));
   Assert.assertTrue(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalInconsistentException(OperationType.OP_CREATE_DB_V2, "failed")));
   Config.metadata_enable_recovery_mode = originVal;
}

```java:llm_gen

@Test
public void testCanSkipBadReplayedJournal() {
   boolean originIgnoreVal = Config.metadata_journal_ignore_replay_failure;
   boolean originRecoveryVal = Config.metadata_enable_recovery_mode;

   Config.metadata_journal_ignore_replay_failure = false;
   Config.metadata_enable_recovery_mode = false;
   Assert.assertFalse(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalException(OperationType.OP_ADD_ANALYZE_STATUS, "failed")));
   Assert.assertFalse(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalException(OperationType.OP_CREATE_DB_V2, "failed")));
   Assert.assertFalse(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalInconsistentException(OperationType.OP_ADD_ANALYZE_STATUS, "failed")));
   Assert.assertFalse(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalInconsistentException(OperationType.OP_CREATE_DB_V2, "failed")));

   Config.metadata_journal_ignore_replay_failure = true;
   Config.metadata_enable_recovery_mode = false;
   Assert.assertTrue(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalException(OperationType.OP_ADD_ANALYZE_STATUS, "failed")));
   Assert.assertFalse(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalException(OperationType.OP_CREATE_DB_V2, "failed")));
   Assert.assertTrue(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalInconsistentException(OperationType.OP_ADD_ANALYZE_STATUS, "failed")));
   Assert.assertFalse(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalInconsistentException(OperationType.OP_CREATE_DB_V2, "failed")));

   Config.metadata_enable_recovery_mode = true;
   Assert.assertTrue(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalException(OperationType.OP_ADD_ANALYZE_STATUS, "failed")));
   Assert.assertTrue(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalException(OperationType.OP_CREATE_DB_V2, "failed")));
   Assert.assertTrue(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalInconsistentException(OperationType.OP_ADD_ANALYZE_STATUS, "failed")));
   Assert.assertTrue(GlobalStateMgr.getServingState().canSkipBadReplayedJournal(new JournalInconsistentException(OperationType.OP_CREATE_DB_V2, "failed")));

   Config.metadata_journal_ignore_replay_failure = originIgnoreVal;
   Config.metadata_enable_recovery_mode = originRecoveryVal;
}


### 168.Missing Asserts
link: https://github.com/apache/incubator-pinot/commit/acb8f19d7fbb810a0e554fc5ac206e2aefd0961b
p_path: pinot-controller/src/main/java/org/apache/pinot/controller/helix/core/rebalance/TableRebalancer.java#isExternalViewConverged
t_path: pinot-controller/src/test/java/org/apache/pinot/controller/helix/core/rebalance/TableRebalancerTest.java#testIsExternalViewConverged

```java:test_src

@Test
public void testIsExternalViewConverged() {
   String offlineTableName = "testTable_OFFLINE";
   Map<String, Map<String, String>> externalViewSegmentStates = new TreeMap<>();
   Map<String, Map<String, String>> idealStateSegmentStates = new TreeMap<>();
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, null));
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, true, null));
   Map<String, String> instanceStateMap = new TreeMap<>();
   instanceStateMap.put("instance1", ONLINE);
   externalViewSegmentStates.put("segment1", instanceStateMap);
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, null));
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, true, null));
   instanceStateMap = new TreeMap<>();
   instanceStateMap.put("instance1", OFFLINE);
   idealStateSegmentStates.put("segment2", instanceStateMap);
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, null));
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, true, null));
   instanceStateMap.put("instance2", CONSUMING);
   assertFalse(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, null));
   assertFalse(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, true, null));
   instanceStateMap = new TreeMap<>();
   externalViewSegmentStates.put("segment2", instanceStateMap);
   assertFalse(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, null));
   assertFalse(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, true, null));
   instanceStateMap.put("instance2", OFFLINE);
   assertFalse(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, null));
   assertFalse(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, true, null));
   instanceStateMap.put("instance2", CONSUMING);
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, null));
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, true, null));
   instanceStateMap.put("instance3", CONSUMING);
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, null));
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, true, null));
   instanceStateMap.put("instance2", ERROR);
   try {
       TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, null);
       fail();
   } catch (Exception e) {
   }
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, true, null));
}

```java:test_tgt

@Test
public void testIsExternalViewConverged() {
   String offlineTableName = "testTable_OFFLINE";
   Map<String, Map<String, String>> externalViewSegmentStates = new TreeMap<>();
   Map<String, Map<String, String>> idealStateSegmentStates = new TreeMap<>();
   boolean[] falseAndTrue = new boolean[] { false, true };
   for (boolean lowDiskMode : falseAndTrue) {
       for (boolean bestEfforts : falseAndTrue) {
           assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, lowDiskMode, bestEfforts, null));
       }
   }
   Map<String, String> instanceStateMap = new TreeMap<>();
   instanceStateMap.put("instance1", ONLINE);
   externalViewSegmentStates.put("segment1", instanceStateMap);
   for (boolean lowDiskMode : falseAndTrue) {
       for (boolean bestEfforts : falseAndTrue) {
           assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, lowDiskMode, bestEfforts, null));
       }
   }
   instanceStateMap = new TreeMap<>();
   instanceStateMap.put("instance1", OFFLINE);
   idealStateSegmentStates.put("segment2", instanceStateMap);
   for (boolean lowDiskMode : falseAndTrue) {
       for (boolean bestEfforts : falseAndTrue) {
           assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, lowDiskMode, bestEfforts, null));
       }
   }
   instanceStateMap.put("instance2", CONSUMING);
   for (boolean lowDiskMode : falseAndTrue) {
       for (boolean bestEfforts : falseAndTrue) {
           assertFalse(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, lowDiskMode, bestEfforts, null));
       }
   }
   instanceStateMap = new TreeMap<>();
   externalViewSegmentStates.put("segment2", instanceStateMap);
   for (boolean lowDiskMode : falseAndTrue) {
       for (boolean bestEfforts : falseAndTrue) {
           assertFalse(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, lowDiskMode, bestEfforts, null));
       }
   }
   instanceStateMap.put("instance2", OFFLINE);
   for (boolean lowDiskMode : falseAndTrue) {
       for (boolean bestEfforts : falseAndTrue) {
           assertFalse(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, lowDiskMode, bestEfforts, null));
       }
   }
   instanceStateMap.put("instance2", CONSUMING);
   for (boolean lowDiskMode : falseAndTrue) {
       for (boolean bestEfforts : falseAndTrue) {
           assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, lowDiskMode, bestEfforts, null));
       }
   }
   instanceStateMap.put("instance3", CONSUMING);
   for (boolean bestEfforts : falseAndTrue) {
       assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, bestEfforts, null));
       assertFalse(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, true, bestEfforts, null));
   }
   instanceStateMap.put("instance2", ERROR);
   instanceStateMap.remove("instance3");
   for (boolean lowDiskMode : falseAndTrue) {
       try {
           TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, lowDiskMode, false, null);
           fail();
       } catch (Exception e) {
       }
       assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, lowDiskMode, true, null));
   }
   instanceStateMap.put("instance2", CONSUMING);
   instanceStateMap.put("instance3", ERROR);
   for (boolean lowDiskMode : falseAndTrue) {
       for (boolean bestEfforts : falseAndTrue) {
           if (lowDiskMode && !bestEfforts) {
               try {
                   TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, true, false, null);
                   fail();
               } catch (Exception e) {
               }
           } else {
               assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, lowDiskMode, bestEfforts, null));
           }
       }
   }
}

```java:llm_gen

@Test
public void testIsExternalViewConverged() {
   String offlineTableName = "testTable_OFFLINE";
   Map<String, Map<String, String>> externalViewSegmentStates = new TreeMap<>();
   Map<String, Map<String, String>> idealStateSegmentStates = new TreeMap<>();
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, false, null));
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, true, null));
   Map<String, String> instanceStateMap = new TreeMap<>();
   instanceStateMap.put("instance1", ONLINE);
   externalViewSegmentStates.put("segment1", instanceStateMap);
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, false, null));
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, true, null));
   instanceStateMap = new TreeMap<>();
   instanceStateMap.put("instance1", OFFLINE);
   idealStateSegmentStates.put("segment2", instanceStateMap);
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, false, null));
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, true, null));
   instanceStateMap.put("instance2", CONSUMING);
   assertFalse(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, false, null));
   assertFalse(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, true, null));
   instanceStateMap = new TreeMap<>();
   externalViewSegmentStates.put("segment2", instanceStateMap);
   assertFalse(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, false, null));
   assertFalse(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, true, null));
   instanceStateMap.put("instance2", OFFLINE);
   assertFalse(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, false, null));
   assertFalse(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, true, null));
   instanceStateMap.put("instance2", CONSUMING);
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, false, null));
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, true, null));
   instanceStateMap.put("instance3", CONSUMING);
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, false, null));
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, true, null));
   instanceStateMap.put("instance2", ERROR);
   try {
       TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, false, null);
       fail();
   } catch (Exception e) {
   }
   assertTrue(TableRebalancer.isExternalViewConverged(offlineTableName, externalViewSegmentStates, idealStateSegmentStates, false, true, null));
}

### 169.External Function Modification
link: https://github.com/soot-oss/SootUp/commit/a6d0912529c2183df1042fc28388bc52c298f6de
p_path: sootup.core/src/main/java/sootup/core/graph/MutableBlockStmtGraph.java#addNode
t_path: sootup.core/src/test/java/sootup/core/graph/MutableBlockStmtGraphTest.java#addNodeTest

```java:test_src

@Test
public void addNodeTest() {
   MutableBlockStmtGraph graph = new MutableBlockStmtGraph();
   assertEquals(0, graph.getBlocks().size());
   graph.addNode(firstGoto);
   assertEquals(1, graph.getBlocks().size());
   // test duplicate insertion of the same node
   graph.addNode(firstGoto);
   assertEquals(1, graph.getBlocks().size());
   assertEquals(1, graph.getBlockOf(firstGoto).getStmts().size());
   graph.addNode(secondNop);
   assertEquals(2, graph.getBlocks().size());
   assertEquals(1, graph.getBlockOf(firstGoto).getStmts().size());
   graph.removeNode(firstGoto);
   assertEquals(1, graph.getBlocks().size());
   assertEquals(1, graph.getBlockOf(secondNop).getStmts().size());
   // removal of not existing
   try {
       graph.removeNode(firstGoto);
       fail("should not be reachable due to exception");
   } catch (Exception ignored) {
   }
   assertEquals(1, graph.getBlocks().size());
   graph.removeNode(secondNop);
   assertEquals(0, graph.getBlocks().size());
}

```java:test_tgt

@Test
public void addNodeTest() {
   MutableBlockStmtGraph graph = new MutableBlockStmtGraph();
   assertEquals(0, graph.getBlocks().size());
   graph.addNode(firstGoto);
   assertEquals(1, graph.getBlocks().size());
   // test duplicate insertion of the same node
   graph.addNode(firstGoto);
   assertEquals(1, graph.getBlocks().size());
   assertEquals(1, graph.getBlockOf(firstGoto).getStmts().size());
   graph.addNode(secondNop);
   assertEquals(2, graph.getBlocks().size());
   assertEquals(1, graph.getBlockOf(firstGoto).getStmts().size());
   try {
       graph.removeNode(firstGoto);
       fail("should not be reachable due to exception");
   } catch (Exception ignored) {
   }
   graph.removeNode(firstGoto, false);
   assertEquals(1, graph.getBlocks().size());
   assertEquals(1, graph.getBlockOf(secondNop).getStmts().size());
   // removal of not existing
   try {
       graph.removeNode(firstGoto);
       fail("should not be reachable due to exception");
   } catch (Exception ignored) {
   }
   assertEquals(1, graph.getBlocks().size());
   graph.removeNode(secondNop);
   assertEquals(0, graph.getBlocks().size());
}

```java:llm_gen

@Test
public void addNodeTest() {
   MutableBlockStmtGraph graph = new MutableBlockStmtGraph();
   assertEquals(0, graph.getBlocks().size());
   graph.addNode(firstGoto);
   assertEquals(1, graph.getBlocks().size());
   graph.addNode(firstGoto);
   assertEquals(1, graph.getBlocks().size());
   assertEquals(1, graph.getBlockOf(firstGoto).getStmts().size());
   graph.addNode(secondNop);
   assertEquals(2, graph.getBlocks().size());
   assertEquals(1, graph.getBlockOf(firstGoto).getStmts().size());
   graph.removeNode(firstGoto);
   assertEquals(1, graph.getBlocks().size());
   assertEquals(1, graph.getBlockOf(secondNop).getStmts().size());
   try {
       graph.removeNode(firstGoto);
       fail("should not be reachable due to exception");
   } catch (Exception ignored) {
   }
   assertEquals(1, graph.getBlocks().size());
   graph.removeNode(secondNop);
   assertEquals(0, graph.getBlocks().size());
}

### 170.Field/Package Information Modification
link: https://github.com/StarRocks/starrocks/commit/b36fac22ae398af5678216cc0460ca003c9c324a
p_path: fe/fe-core/src/main/java/com/starrocks/alter/LakeTableAsyncFastSchemaChangeJob.java#getInfo
t_path: fe/fe-core/src/test/java/com/starrocks/alter/LakeTableAsyncFastSchemaChangeJobTest.java#testGetInfo

```java:test_src

@Test
public void testGetInfo() throws Exception {
   LakeTable table = createTable(connectContext, "CREATE TABLE t1(c0 INT) DUPLICATE KEY(c0) DISTRIBUTED BY HASH(c0) " + "BUCKETS 2 PROPERTIES('fast_schema_evolution'='true')");
   AlterJobV2 job = mustAlterTable(table, "ALTER TABLE t1 ADD COLUMN c1 BIGINT");
   List<List<Comparable>> infoList = new ArrayList<>();
   job.getInfo(infoList);
   Assert.assertEquals(1, infoList.size());
   List<Comparable> info = infoList.get(0);
   Assert.assertEquals(13, info.size());
   Assert.assertEquals(job.getJobId(), info.get(0));
   Assert.assertEquals(table.getName(), info.get(1));
   Assert.assertEquals(TimeUtils.longToTimeString(job.createTimeMs), info.get(2));
   Assert.assertEquals(TimeUtils.longToTimeString(job.finishedTimeMs), info.get(3));
   Assert.assertEquals(table.getIndexNameById(table.getBaseIndexId()), info.get(4));
   Assert.assertEquals(table.getBaseIndexId(), info.get(5));
   Assert.assertEquals(table.getBaseIndexId(), info.get(6));
   Assert.assertEquals(String.format("%d:0", table.getIndexIdToMeta().get(table.getBaseIndexId()).getSchemaVersion()), info.get(7));
   Assert.assertEquals(job.getTransactionId().get(), info.get(8));
   Assert.assertEquals(job.getJobState().name(), info.get(9));
   Assert.assertEquals(job.errMsg, info.get(10));
   Assert.assertEquals(job.getTimeoutMs() / 1000, info.get(12));
}

```java:test_tgt

@Test
public void testGetInfo() throws Exception {
   LakeTable table = createTable(connectContext, "CREATE TABLE t1(c0 INT) DUPLICATE KEY(c0) DISTRIBUTED BY HASH(c0) " + "BUCKETS 2 PROPERTIES('fast_schema_evolution'='true')");
   AlterJobV2 job = mustAlterTable(table, "ALTER TABLE t1 ADD COLUMN c1 BIGINT");
   List<List<Comparable>> infoList = new ArrayList<>();
   job.getInfo(infoList);
   Assert.assertEquals(1, infoList.size());
   List<Comparable> info = infoList.get(0);
   Assert.assertEquals(14, info.size());
   Assert.assertEquals(job.getJobId(), info.get(0));
   Assert.assertEquals(table.getName(), info.get(1));
   Assert.assertEquals(TimeUtils.longToTimeString(job.createTimeMs), info.get(2));
   Assert.assertEquals(TimeUtils.longToTimeString(job.finishedTimeMs), info.get(3));
   Assert.assertEquals(table.getIndexNameById(table.getBaseIndexId()), info.get(4));
   Assert.assertEquals(table.getBaseIndexId(), info.get(5));
   Assert.assertEquals(table.getBaseIndexId(), info.get(6));
   Assert.assertEquals(String.format("%d:0", table.getIndexIdToMeta().get(table.getBaseIndexId()).getSchemaVersion()), info.get(7));
   Assert.assertEquals(job.getTransactionId().get(), info.get(8));
   Assert.assertEquals(job.getJobState().name(), info.get(9));
   Assert.assertEquals(job.errMsg, info.get(10));
   Assert.assertEquals(job.getTimeoutMs() / 1000, info.get(12));
   Assert.assertEquals("default_warehouse", info.get(13));
}

```java:llm_gen

@Test
public void testGetInfo() throws Exception {
   LakeTable table = createTable(connectContext, "CREATE TABLE t1(c0 INT) DUPLICATE KEY(c0) DISTRIBUTED BY HASH(c0) " + "BUCKETS 2 PROPERTIES('fast_schema_evolution'='true')");
   AlterJobV2 job = mustAlterTable(table, "ALTER TABLE t1 ADD COLUMN c1 BIGINT");
   List<List<Comparable>> infoList = new ArrayList<>();
   job.getInfo(infoList);
   Assert.assertEquals(1, infoList.size());
   List<Comparable> info = infoList.get(0);
   Assert.assertEquals(14, info.size());
   Assert.assertEquals(job.getJobId(), info.get(0));
   Assert.assertEquals(table.getName(), info.get(1));
   Assert.assertEquals(TimeUtils.longToTimeString(job.createTimeMs), info.get(2));
   Assert.assertEquals(TimeUtils.longToTimeString(job.finishedTimeMs), info.get(3));
   Assert.assertEquals(table.getIndexNameById(table.getBaseIndexId()), info.get(4));
   Assert.assertEquals(table.getBaseIndexId(), info.get(5));
   Assert.assertEquals(table.getBaseIndexId(), info.get(6));
   Assert.assertEquals(String.format("%d:0", table.getIndexIdToMeta().get(table.getBaseIndexId()).getSchemaVersion()), info.get(7));
   Assert.assertEquals(job.getTransactionId().get(), info.get(8));
   Assert.assertEquals(job.getJobState().name(), info.get(9));
   Assert.assertEquals(job.errMsg, info.get(10));
   Assert.assertEquals(job.getTimeoutMs() / 1000, info.get(12));
   Assert.assertEquals("null", info.get(13));
}

### 171.Test Preparation Error
link: https://github.com/StarRocks/starrocks/commit/e79cbddb72453c46111915a2f53918c348f20bce
p_path: fe/fe-core/src/main/java/com/starrocks/server/SharedDataStorageVolumeMgr.java#getStorageVolumeOfDb
t_path: fe/fe-core/src/test/java/com/starrocks/server/SharedDataStorageVolumeMgrTest.java#testGetStorageVolumeOfDb

```java:test_src

@Test
public void testGetStorageVolumeOfDb() throws DdlException, AlreadyExistsException {
   new Expectations() {
       {
           editLog.logSetDefaultStorageVolume((SetDefaultStorageVolumeLog) any);
       }
   };
   SharedDataStorageVolumeMgr sdsvm = new SharedDataStorageVolumeMgr();
   sdsvm.createBuiltinStorageVolume();
   String defaultSVId = sdsvm.getStorageVolumeByName(SharedDataStorageVolumeMgr.BUILTIN_STORAGE_VOLUME).getId();
   String svName = "test";
   List<String> locations = Arrays.asList("s3://abc");
   Map<String, String> storageParams = new HashMap<>();
   storageParams.put(AWS_S3_REGION, "region");
   storageParams.put(AWS_S3_ENDPOINT, "endpoint");
   storageParams.put(AWS_S3_USE_AWS_SDK_DEFAULT_BEHAVIOR, "true");
   String testSVId = sdsvm.createStorageVolume(svName, "S3", locations, storageParams, Optional.empty(), "");
   StorageVolume sv = Deencapsulation.invoke(sdsvm, "getStorageVolumeOfDb", StorageVolumeMgr.DEFAULT);
   Assert.assertEquals(defaultSVId, sv.getId());
   sv = Deencapsulation.invoke(sdsvm, "getStorageVolumeOfDb", svName);
   Assert.assertEquals(testSVId, sv.getId());
}

```java:test_tgt

@Test
public void testGetStorageVolumeOfDb() throws DdlException, AlreadyExistsException {
   new Expectations() {
       {
           editLog.logSetDefaultStorageVolume((SetDefaultStorageVolumeLog) any);
       }
   };
   SharedDataStorageVolumeMgr sdsvm = new SharedDataStorageVolumeMgr();
   ErrorReportException ex = Assert.assertThrows(ErrorReportException.class, () -> Deencapsulation.invoke(sdsvm, "getStorageVolumeOfDb", StorageVolumeMgr.DEFAULT));
   Assert.assertEquals(ErrorCode.ERR_NO_DEFAULT_STORAGE_VOLUME, ex.getErrorCode());
   sdsvm.createBuiltinStorageVolume();
   String defaultSVId = sdsvm.getStorageVolumeByName(SharedDataStorageVolumeMgr.BUILTIN_STORAGE_VOLUME).getId();
   String svName = "test";
   List<String> locations = Arrays.asList("s3://abc");
   Map<String, String> storageParams = new HashMap<>();
   storageParams.put(AWS_S3_REGION, "region");
   storageParams.put(AWS_S3_ENDPOINT, "endpoint");
   storageParams.put(AWS_S3_USE_AWS_SDK_DEFAULT_BEHAVIOR, "true");
   String testSVId = sdsvm.createStorageVolume(svName, "S3", locations, storageParams, Optional.empty(), "");
   StorageVolume sv = Deencapsulation.invoke(sdsvm, "getStorageVolumeOfDb", StorageVolumeMgr.DEFAULT);
   Assert.assertEquals(defaultSVId, sv.getId());
   sv = Deencapsulation.invoke(sdsvm, "getStorageVolumeOfDb", svName);
   Assert.assertEquals(testSVId, sv.getId());
}

```java:llm_gen

@Test
public void testGetStorageVolumeOfDb() throws DdlException, AlreadyExistsException {
   new Expectations() {
       {
           editLog.logSetDefaultStorageVolume((SetDefaultStorageVolumeLog) any);
       }
   };
   SharedDataStorageVolumeMgr sdsvm = new SharedDataStorageVolumeMgr();
   sdsvm.createBuiltinStorageVolume();
   String defaultSVId = sdsvm.getStorageVolumeByName(SharedDataStorageVolumeMgr.BUILTIN_STORAGE_VOLUME).getId();
   String svName = "test";
   List<String> locations = Arrays.asList("s3://abc");
   Map<String, String> storageParams = new HashMap<>();
   storageParams.put(AWS_S3_REGION, "region");
   storageParams.put(AWS_S3_ENDPOINT, "endpoint");
   storageParams.put(AWS_S3_USE_AWS_SDK_DEFAULT_BEHAVIOR, "true");
   String testSVId = sdsvm.createStorageVolume(svName, "S3", locations, storageParams, Optional.empty(), "");
   StorageVolume sv = Deencapsulation.invoke(sdsvm, "getStorageVolumeOfDb", StorageVolumeMgr.DEFAULT);
   Assert.assertEquals(defaultSVId, sv.getId());
   sv = Deencapsulation.invoke(sdsvm, "getStorageVolumeOfDb", svName);
   Assert.assertEquals(testSVId, sv.getId());

   new MockUp<ErrorReportException>() {
       @Mock
       public void report(ErrorCode errorCode) {
           throw new RuntimeException("Expected error: " + errorCode);
       }
   };
   try {
       SharedDataStorageVolumeMgr emptyMgr = new SharedDataStorageVolumeMgr();
       Deencapsulation.invoke(emptyMgr, "getStorageVolumeOfDb", StorageVolumeMgr.DEFAULT);
       Assert.fail("Expected ErrorReportException");
   } catch (RuntimeException e) {
       Assert.assertTrue(e.getMessage().contains("ERR_NO_DEFAULT_STORAGE_VOLUME"));
   }
}

### 172.Missing Asserts
link: https://github.com/yahoo/elide/commit/a196f753bb0b9323de7037742c395d4c07524e3b
p_path: elide-async/src/main/java/com/yahoo/elide/async/resources/ExportApiEndpoint.java#get
t_path: elide-async/src/test/java/com/yahoo/elide/async/resources/ExportApiEndpointTest.java#testGet

```java:test_src

@Test
public void testGet() {
   String queryId = "1";
   int maxDownloadTimeSeconds = 1;
   int maxDownloadTimeMilliSeconds = (int) TimeUnit.SECONDS.toMillis(maxDownloadTimeSeconds);
   when(engine.getResultsByID(queryId)).thenReturn(Observable.just("result"));
   exportApiProperties = new ExportApiProperties(Executors.newFixedThreadPool(1), Duration.ofSeconds(maxDownloadTimeSeconds));
   endpoint = new ExportApiEndpoint(engine, exportApiProperties);
   endpoint.get(queryId, response, asyncResponse);
   verify(engine, timeout(maxDownloadTimeMilliSeconds)).getResultsByID(queryId);
   verify(asyncResponse, timeout(maxDownloadTimeMilliSeconds)).resume(responseCaptor.capture());
   final Response res = responseCaptor.getValue();
   assertEquals(res.getStatus(), 200);
}

```java:test_tgt

@Test
public void testGet() {
   String queryId = "1";
   int maxDownloadTimeSeconds = 1;
   int maxDownloadTimeMilliSeconds = (int) TimeUnit.SECONDS.toMillis(maxDownloadTimeSeconds);
   when(engine.getResultsByID(queryId)).thenReturn(outputStream -> {
       try {
           outputStream.write("result".getBytes(StandardCharsets.UTF_8));
       } catch (IOException e) {
           throw new UncheckedIOException(e);
       }
   });
   exportApiProperties = new ExportApiProperties(Executors.newFixedThreadPool(1), Duration.ofSeconds(maxDownloadTimeSeconds));
   endpoint = new ExportApiEndpoint(engine, exportApiProperties);
   endpoint.get(queryId, response, asyncResponse);
   verify(engine, timeout(maxDownloadTimeMilliSeconds)).getResultsByID(queryId);
   verify(asyncResponse, timeout(maxDownloadTimeMilliSeconds)).resume(responseCaptor.capture());
   final Response res = responseCaptor.getValue();
   assertEquals(res.getStatus(), 200);
}

```java:llm_gen

@Test
public void testGet() {
   String queryId = "1";
   int maxDownloadTimeSeconds = 1;
   int maxDownloadTimeMilliSeconds = (int) TimeUnit.SECONDS.toMillis(maxDownloadTimeSeconds);
   when(engine.getResultsByID(queryId)).thenReturn(outputStream -> outputStream.write("result".getBytes()));
   exportApiProperties = new ExportApiProperties(Executors.newFixedThreadPool(1), Duration.ofSeconds(maxDownloadTimeSeconds));
   endpoint = new ExportApiEndpoint(engine, exportApiProperties);
   endpoint.get(queryId, response, asyncResponse);
   verify(engine, timeout(maxDownloadTimeMilliSeconds)).getResultsByID(queryId);
   verify(asyncResponse, timeout(maxDownloadTimeMilliSeconds)).resume(responseCaptor.capture());
   final Response res = responseCaptor.getValue();
   assertEquals(res.getStatus(), 200);
}

### 173.Wrong Update Direction
link: https://github.com/stefan-niedermann/nextcloud-deck/commit/1224b34217c225a1093df54ef449f88e2b79baa3
p_path: app/src/main/java/it/niedermann/nextcloud/deck/remote/api/ResponseCallback.java#from
t_path: app/src/test/java/it/niedermann/nextcloud/deck/remote/api/ResponseCallbackTest.java#testFrom

```java:test_src

@Test
public void testFrom() {
   final var originalCallback = new IResponseCallback<EmptyResponse>() {
       @Override
       public void onResponse(EmptyResponse response) {
       }
   };
   final var originalCallbackSpy = spy(originalCallback);
   final var callback = ResponseCallback.from(mock(Account.class), originalCallbackSpy);
   callback.onResponse(null);
   verify(originalCallbackSpy, times(1)).onResponse(null);
   callback.onError(null);
   verify(originalCallbackSpy, times(1)).onError(null);
}

```java:test_tgt

@Test
public void testFrom() {
   final var originalCallback = new IResponseCallback<EmptyResponse>() {
       @Override
       public void onResponse(EmptyResponse response, Headers headers) {
       }
   };
   final var originalCallbackSpy = spy(originalCallback);
   final var callback = ResponseCallback.from(mock(Account.class), originalCallbackSpy);
   callback.onResponse(null, IResponseCallback.EMPTY_HEADERS);
   verify(originalCallbackSpy, times(1)).onResponse(null, IResponseCallback.EMPTY_HEADERS);
   callback.onError(null);
   verify(originalCallbackSpy, times(1)).onError(null);
}

```java:llm_gen

@Test
public void testFrom() {
   final var originalCallback = new IResponseCallback<EmptyResponse>() {
       @Override
       public void onResponse(EmptyResponse response, Headers headers) {
       }
   };
   final var originalCallbackSpy = spy(originalCallback);
   final var callback = ResponseCallback.from(mock(Account.class), originalCallbackSpy);
   callback.onResponse(null, null);
   verify(originalCallbackSpy, times(1)).onResponse(null, null);
   callback.onError(null);
   verify(originalCallbackSpy, times(1)).onError(null);
}


### 174.Correct
link: https://github.com/huaweicloud/Sermant/commit/8f220ca2e85ea00cb6915f80ea2edba4b6d3f582
p_path: sermant-plugins/sermant-router/router-config-service/src/main/java/com/huaweicloud/sermant/router/config/handler/GlobalConfigHandler.java#shouldHandle
t_path: sermant-plugins/sermant-router/router-config-service/src/test/java/com/huaweicloud/sermant/router/config/handler/GlobalConfigHandlerTest.java#testShouldHandle

```java:test_src

/**
* 测试shouldHandle方法
*/
@Test
public void testShouldHandle() {
   Assert.assertTrue(handler.shouldHandle("servicecomb.globalRouteRule", RouterConstant.FLOW_MATCH_KIND));
}

```java:test_tgt

@Test
public void testShouldHandle() {
   Assert.assertTrue(handler.shouldHandle("servicecomb.globalRouteRule"));
}

```java:llm_gen

@Test
public void testShouldHandle() {
   Assert.assertTrue(handler.shouldHandle("servicecomb.globalRouteRule"));
}


### 175.Correct
link: https://github.com/google/tink/commit/b0c03e2304a0a0cc20f6ba8de4a6b85f8d1683be
p_path: java_src/src/main/java/com/google/crypto/tink/daead/DeterministicAeadKeyTemplates.java#createAesSivKeyTemplate
t_path: java_src/src/test/java/com/google/crypto/tink/daead/DeterministicAeadKeyTemplatesTest.java#testCreateAesSivKeyTemplate

```java:test_src

@Test
public void testCreateAesSivKeyTemplate() throws Exception {
   int keySize = 42;
   KeyTemplate template = DeterministicAeadKeyTemplates.createAesSivKeyTemplate(keySize);
   assertEquals(new AesSivKeyManager().getKeyType(), template.getTypeUrl());
   assertEquals(OutputPrefixType.TINK, template.getOutputPrefixType());
   AesSivKeyFormat format = AesSivKeyFormat.parseFrom(template.getValue(), ExtensionRegistryLite.getEmptyRegistry());
   assertEquals(keySize, format.getKeySize());
}

```java:test_tgt

@Test
public void testCreateAesSivKeyTemplate() throws Exception {
   int keySize = 42;
   KeyTemplate template = DeterministicAeadKeyTemplates.createAesSivKeyTemplate(keySize);
   assertEquals(AesSivKeyManager.getKeyType(), template.getTypeUrl());
   assertEquals(OutputPrefixType.TINK, template.getOutputPrefixType());
   AesSivKeyFormat format = AesSivKeyFormat.parseFrom(template.getValue(), ExtensionRegistryLite.getEmptyRegistry());
   assertEquals(keySize, format.getKeySize());
}

```java:llm_gen

@Test
public void testCreateAesSivKeyTemplate() throws Exception {
   int keySize = 42;
   KeyTemplate template = DeterministicAeadKeyTemplates.createAesSivKeyTemplate(keySize);
   assertEquals(AesSivKeyManager.getKeyType(), template.getTypeUrl());
   assertEquals(OutputPrefixType.TINK, template.getOutputPrefixType());
   AesSivKeyFormat format = AesSivKeyFormat.parseFrom(template.getValue(), ExtensionRegistryLite.getEmptyRegistry());
   assertEquals(keySize, format.getKeySize());
}

### 176.External File Modification
link: https://github.com/GoogleCloudPlatform/DataflowTemplates/commit/2e024643d1fa35e35b9ca64c690b81dfc5836ea9
p_path: v2/spanner-common/src/main/java/com/google/cloud/teleport/v2/spanner/migrations/avro/GenericRecordTypeConvertor.java#handleLogicalFieldType
t_path: v2/spanner-common/src/test/java/com/google/cloud/teleport/v2/spanner/migrations/avro/GenericRecordTypeConvertorTest.java#testHandleLogicalFieldType

```java:test_src

@Test
public void testHandleLogicalFieldType() {
   Schema avroSchema = SchemaUtils.parseAvroSchema(AvroTestingHelper.LOGICAL_TYPES_SCHEMA_JSON);
   GenericRecord genericRecord = new GenericData.Record(avroSchema);
   genericRecord.put("date_col", 738991);
   genericRecord.put("decimal_col", ByteBuffer.wrap(new BigDecimal("12.34").unscaledValue().toByteArray()));
   genericRecord.put("time_micros_col", 48035000000L);
   genericRecord.put("time_millis_col", 48035000);
   genericRecord.put("timestamp_micros_col", 1602599400056483L);
   genericRecord.put("timestamp_millis_col", 1602599400056L);
   String result = GenericRecordTypeConvertor.handleLogicalFieldType("date_col", genericRecord);
   assertEquals("Test date_col conversion: ", "3993-04-16", result);
   result = GenericRecordTypeConvertor.handleLogicalFieldType("decimal_col", genericRecord);
   assertEquals("Test decimal_col conversion: ", "12.34", result);
   result = GenericRecordTypeConvertor.handleLogicalFieldType("time_micros_col", genericRecord);
   assertEquals("Test time_micros_col conversion: ", "13:20:35", result);
   result = GenericRecordTypeConvertor.handleLogicalFieldType("time_millis_col", genericRecord);
   assertEquals("Test time_millis_col conversion: ", "13:20:35", result);
   result = GenericRecordTypeConvertor.handleLogicalFieldType("timestamp_micros_col", genericRecord);
   assertEquals("Test timestamp_micros_col conversion: ", "2020-10-13T14:30:00.056483Z", result);
   result = GenericRecordTypeConvertor.handleLogicalFieldType("timestamp_millis_col", genericRecord);
   assertEquals("Test timestamp_millis_col conversion: ", "2020-10-13T14:30:00.056Z", result);
}

```java:test_tgt

@Test
public void testHandleLogicalFieldType() throws IOException {
   Schema avroSchema = SchemaUtils.parseAvroSchema(Files.readString(Paths.get("src/test/resources/avro/logical-types-schema.avsc")));
   GenericRecord genericRecord = new GenericData.Record(avroSchema);
   genericRecord.put("date_col", 738991);
   genericRecord.put("decimal_col", ByteBuffer.wrap(new BigDecimal("12.34").unscaledValue().toByteArray()));
   genericRecord.put("time_micros_col", 48035000000L);
   genericRecord.put("time_millis_col", 48035000);
   genericRecord.put("timestamp_micros_col", 1602599400056483L);
   genericRecord.put("timestamp_millis_col", 1602599400056L);
   String col = "date_col";
   String result = GenericRecordTypeConvertor.handleLogicalFieldType(col, genericRecord.get(col), genericRecord.getSchema().getField(col).schema());
   assertEquals("Test date_col conversion: ", "3993-04-16", result);
   col = "decimal_col";
   result = GenericRecordTypeConvertor.handleLogicalFieldType(col, genericRecord.get(col), genericRecord.getSchema().getField(col).schema());
   assertEquals("Test decimal_col conversion: ", "12.34", result);
   col = "time_micros_col";
   result = GenericRecordTypeConvertor.handleLogicalFieldType(col, genericRecord.get(col), genericRecord.getSchema().getField(col).schema());
   assertEquals("Test time_micros_col conversion: ", "13:20:35", result);
   col = "time_millis_col";
   result = GenericRecordTypeConvertor.handleLogicalFieldType(col, genericRecord.get(col), genericRecord.getSchema().getField(col).schema());
   assertEquals("Test time_millis_col conversion: ", "13:20:35", result);
   col = "timestamp_micros_col";
   result = GenericRecordTypeConvertor.handleLogicalFieldType(col, genericRecord.get(col), genericRecord.getSchema().getField(col).schema());
   assertEquals("Test timestamp_micros_col conversion: ", "2020-10-13T14:30:00.056483Z", result);
   col = "timestamp_millis_col";
   result = GenericRecordTypeConvertor.handleLogicalFieldType(col, genericRecord.get(col), genericRecord.getSchema().getField(col).schema());
   assertEquals("Test timestamp_millis_col conversion: ", "2020-10-13T14:30:00.056Z", result);
}

```java:llm_gen

@Test
public void testHandleLogicalFieldType() {
   Schema avroSchema = SchemaUtils.parseAvroSchema(AvroTestingHelper.LOGICAL_TYPES_SCHEMA_JSON);
   Schema dateSchema = avroSchema.getField("date_col").schema();
   Schema decimalSchema = avroSchema.getField("decimal_col").schema();
   Schema timeMicrosSchema = avroSchema.getField("time_micros_col").schema();
   Schema timeMillisSchema = avroSchema.getField("time_millis_col").schema();
   Schema timestampMicrosSchema = avroSchema.getField("timestamp_micros_col").schema();
   Schema timestampMillisSchema = avroSchema.getField("timestamp_millis_col").schema();

   String result = GenericRecordTypeConvertor.handleLogicalFieldType("date_col", 738991, dateSchema);
   assertEquals("Test date_col conversion: ", "3993-04-16", result);
   result = GenericRecordTypeConvertor.handleLogicalFieldType("decimal_col", ByteBuffer.wrap(new BigDecimal("12.34").unscaledValue().toByteArray()), decimalSchema);
   assertEquals("Test decimal_col conversion: ", "12.34", result);
   result = GenericRecordTypeConvertor.handleLogicalFieldType("time_micros_col", 48035000000L, timeMicrosSchema);
   assertEquals("Test time_micros_col conversion: ", "13:20:35", result);
   result = GenericRecordTypeConvertor.handleLogicalFieldType("time_millis_col", 48035000, timeMillisSchema);
   assertEquals("Test time_millis_col conversion: ", "13:20:35", result);
   result = GenericRecordTypeConvertor.handleLogicalFieldType("timestamp_micros_col", 1602599400056483L, timestampMicrosSchema);
   assertEquals("Test timestamp_micros_col conversion: ", "2020-10-13T14:30:00.056483Z", result);
   result = GenericRecordTypeConvertor.handleLogicalFieldType("timestamp_millis_col", 1602599400056L, timestampMillisSchema);
   assertEquals("Test timestamp_millis_col conversion: ", "2020-10-13T14:30:00.056Z", result);
}

### 177.External Function Modification
link: https://github.com/schemaspy/schemaspy/commit/8d6743368d0c6f6a8826ae879dc8761241eb6444
p_path: src/main/java/org/schemaspy/util/markup/Asciidoc.java#toHtml
t_path: src/test/java/org/schemaspy/util/markup/AsciidocTest.java#toHtmlTest

```java:test_src

@Test
void toHtmlTest() {
   String sourceAsciiDoc = ":seq1: {counter:seq1}\n" + "== Section {seq1}\n" + "\n" + "The sequence in this section is {seq1}.\n" + "\n" + ":seq1: {counter:seq1}\n" + "== Section {seq1}\n" + "\n" + "The sequence in this section is {seq1}.";
   String expectedHtml = "<div class=\"sect1\">\n" + "<h2 id=\"_section_1\">Section 1</h2>\n" + "<div class=\"sectionbody\">\n" + "<div class=\"paragraph\">\n" + "<p>The sequence in this section is 1.</p>\n" + "</div>\n" + "</div>\n" + "</div>\n" + "<div class=\"sect1\">\n" + "<h2 id=\"_section_2\">Section 2</h2>\n" + "<div class=\"sectionbody\">\n" + "<div class=\"paragraph\">\n" + "<p>The sequence in this section is 2.</p>\n" + "</div>\n" + "</div>\n" + "</div>";
   String actualHtml = new Asciidoc(new PageRegistry()).toHtml(sourceAsciiDoc, ".");
   assertThat(actualHtml).isEqualTo(expectedHtml);
}

```java:test_tgt

@Test
void toHtmlTest() {
   String sourceAsciiDoc = ":seq1: {counter:seq1}\n" + "== Section {seq1}\n" + "\n" + "The sequence in this section is {seq1}.\n" + "\n" + ":seq1: {counter:seq1}\n" + "== Section {seq1}\n" + "\n" + "The sequence in this section is {seq1}.";
   String expectedHtml = "<div class=\"sect1\">\n" + "<h2 id=\"_section_1\">Section 1</h2>\n" + "<div class=\"sectionbody\">\n" + "<div class=\"paragraph\">\n" + "<p>The sequence in this section is 1.</p>\n" + "</div>\n" + "</div>\n" + "</div>\n" + "<div class=\"sect1\">\n" + "<h2 id=\"_section_2\">Section 2</h2>\n" + "<div class=\"sectionbody\">\n" + "<div class=\"paragraph\">\n" + "<p>The sequence in this section is 2.</p>\n" + "</div>\n" + "</div>\n" + "</div>";
   String actualHtml = new Asciidoc(new PageRegistry(), sourceAsciiDoc, ".").toHtml();
   assertThat(actualHtml).isEqualTo(expectedHtml);
}

```java:llm_gen

@Test
void toHtmlTest() {
   String sourceAsciiDoc = ":seq1: {counter:seq1}\n" + "== Section {seq1}\n" + "\n" + "The sequence in this section is {seq1}.\n" + "\n" + ":seq1: {counter:seq1}\n" + "== Section {seq1}\n" + "\n" + "The sequence in this section is {seq1}.";
   String expectedHtml = "<div class=\"sect1\">\n" + "<h2 id=\"_section_1\">Section 1</h2>\n" + "<div class=\"sectionbody\">\n" + "<div class=\"paragraph\">\n" + "<p>The sequence in this section is 1.</p>\n" + "</div>\n" + "</div>\n" + "</div>\n" + "<div class=\"sect1\">\n" + "<h2 id=\"_section_2\">Section 2</h2>\n" + "<div class=\"sectionbody\">\n" + "<div class=\"paragraph\">\n" + "<p>The sequence in this section is 2.</p>\n" + "</div>\n" + "</div>\n" + "</div>";
   String actualHtml = new Asciidoc(new PageRegistry()).toHtml();
   assertThat(actualHtml).isEqualTo(expectedHtml);
}

### 178.External Function Modification
link: https://github.com/BentoBoxWorld/BentoBox/commit/196e90bf4e4f0fbd8803dc523cfe4ecd826c58d6
p_path: src/main/java/world/bentobox/bentobox/managers/RanksManager.java#removeRank
t_path: src/test/java/world/bentobox/bentobox/managers/RanksManagerTest.java#testRemoveRank

```java:test_src

@Test
public void testRemoveRank() {
   assertTrue(ranksManager.addRank("test.rank.reference2", 650));
   assertTrue(ranksManager.removeRank("test.rank.reference2"));
   assertFalse(ranksManager.removeRank("test.rank.reference2"));
}

```java:test_tgt

@Test
public void testRemoveRank() {
   assertTrue(RanksManager.getInstance().addRank("test.rank.reference2", 650));
   assertTrue(RanksManager.getInstance().removeRank("test.rank.reference2"));
   assertFalse(RanksManager.getInstance().removeRank("test.rank.reference2"));
}

```java:llm_gen

@Test
public void testRemoveRank() {
   assertTrue(ranksManager.addRank("test.rank.reference2", 650));
   assertTrue(ranksManager.removeRank("test.rank.reference2"));
   assertFalse(ranksManager.removeRank("test.rank.reference2"));
   assertTrue(ranksManager.removeRank("OWNER_RANK_REF"));
   assertTrue(ranksManager.removeRank("SUB_OWNER_RANK_REF"));
   assertTrue(ranksManager.removeRank("TRUSTED_RANK_REF"));
   assertTrue(ranksManager.removeRank("COOP_RANK_REF"));
   assertTrue(ranksManager.removeRank("MEMBER_RANK_REF"));
   assertTrue(ranksManager.removeRank("VISITOR_RANK_REF"));
   assertTrue(ranksManager.removeRank("BANNED_RANK_REF"));
   assertTrue(ranksManager.removeRank("ADMIN_RANK_REF"));
   assertTrue(ranksManager.removeRank("MOD_RANK_REF"));
}

### 179.Test Preparation Error
link: https://github.com/huanghongxun/HMCL/commit/95afaa51122907835e1790eb265b184a79f895c7
p_path: HMCLCore/src/main/java/org/jackhuang/hmcl/util/versioning/VersionRange.java#contains
t_path: HMCLCore/src/test/java/org/jackhuang/hmcl/util/versioning/VersionRangeTest.java#testContains

```java:test_src

@Test
public void testContains() {
   assertTrue(between("10", "20").contains("10"));
   assertTrue(between("10", "20").contains("15"));
   assertTrue(between("10", "20").contains("20"));
   assertFalse(between("10", "20").contains("5"));
   assertFalse(between("10", "20").contains("25"));
   assertTrue(between("10", "10").contains("10"));
   assertFalse(between("10", "10").contains("5"));
   assertFalse(between("10", "10").contains("15"));
   assertTrue(atLeast("10").contains("10"));
   assertTrue(atLeast("10").contains("20"));
   assertFalse(atLeast("10").contains("5"));
   assertTrue(atMost("10").contains("10"));
   assertTrue(atMost("10").contains("5"));
   assertFalse(atMost("10").contains("20"));
   assertFalse(empty().contains("0"));
   assertFalse(empty().contains("10"));
   assertTrue(all().contains("0"));
   assertTrue(all().contains("10"));
   assertFalse(all().contains((String) null));
   assertFalse(empty().contains((String) null));
   assertFalse(between("0", "10").contains((String) null));
   assertFalse(atLeast("10").contains((String) null));
   assertFalse(atMost("10").contains((String) null));
   assertFalse(all().contains((VersionNumber) null));
   assertFalse(empty().contains((VersionNumber) null));
   assertFalse(between("0", "10").contains((VersionNumber) null));
   assertFalse(atLeast("10").contains((VersionNumber) null));
   assertFalse(atMost("10").contains((VersionNumber) null));
}

```java:test_tgt

@Test
public void testContains() {
   VersionRange<VersionNumber> empty = VersionRange.empty();
   VersionRange<VersionNumber> all = all();
   assertTrue(VersionNumber.between("10", "20").contains(VersionNumber.asVersion("10")));
   assertTrue(VersionNumber.between("10", "20").contains(VersionNumber.asVersion("15")));
   assertTrue(VersionNumber.between("10", "20").contains(VersionNumber.asVersion("20")));
   assertFalse(VersionNumber.between("10", "20").contains(VersionNumber.asVersion("5")));
   assertFalse(VersionNumber.between("10", "20").contains(VersionNumber.asVersion("25")));
   assertTrue(VersionNumber.between("10", "10").contains(VersionNumber.asVersion("10")));
   assertFalse(VersionNumber.between("10", "10").contains(VersionNumber.asVersion("5")));
   assertFalse(VersionNumber.between("10", "10").contains(VersionNumber.asVersion("15")));
   assertTrue(VersionNumber.atLeast("10").contains(VersionNumber.asVersion("10")));
   assertTrue(VersionNumber.atLeast("10").contains(VersionNumber.asVersion("20")));
   assertFalse(VersionNumber.atLeast("10").contains(VersionNumber.asVersion("5")));
   assertTrue(VersionNumber.atMost("10").contains(VersionNumber.asVersion("10")));
   assertTrue(VersionNumber.atMost("10").contains(VersionNumber.asVersion("5")));
   assertFalse(VersionNumber.atMost("10").contains(VersionNumber.asVersion("20")));
   assertFalse(empty.contains(VersionNumber.asVersion("0")));
   assertFalse(empty.contains(VersionNumber.asVersion("10")));
   assertTrue(all.contains(VersionNumber.asVersion("0")));
   assertTrue(all.contains(VersionNumber.asVersion("10")));
   assertFalse(all.contains(null));
   assertFalse(empty.contains(null));
   assertFalse(VersionNumber.between("0", "10").contains(null));
   assertFalse(VersionNumber.atLeast("10").contains(null));
   assertFalse(VersionNumber.atMost("10").contains(null));
   assertFalse(all.contains(null));
   assertFalse(empty.contains(null));
   assertFalse(VersionNumber.between("0", "10").contains(null));
   assertFalse(VersionNumber.atLeast("10").contains(null));
   assertFalse(VersionNumber.atMost("10").contains(null));
}

```java:llm_gen

@Test
public void testContains() {
   assertTrue(between("10", "20").contains("10"));
   assertTrue(between("10", "20").contains("15"));
   assertTrue(between("10", "20").contains("20"));
   assertFalse(between("10", "20").contains("5"));
   assertFalse(between("10", "20").contains("25"));
   assertTrue(between("10", "10").contains("10"));
   assertFalse(between("10", "10").contains("5"));
   assertFalse(between("10", "10").contains("15"));
   assertTrue(atLeast("10").contains("10"));
   assertTrue(atLeast("10").contains("20"));
   assertFalse(atLeast("10").contains("5"));
   assertTrue(atMost("10").contains("10"));
   assertTrue(atMost("10").contains("5"));
   assertFalse(atMost("10").contains("20"));
   assertFalse(empty().contains("0"));
   assertFalse(empty().contains("10"));
   assertTrue(all().contains("0"));
   assertTrue(all().contains("10"));
   assertFalse(all().contains((String) null));
   assertFalse(empty().contains((String) null));
   assertFalse(between("0", "10").contains((String) null));
   assertFalse(atLeast("10").contains((String) null));
   assertFalse(atMost("10").contains((String) null));
   assertFalse(all().contains((VersionNumber) null));
   assertFalse(empty().contains((VersionNumber) null));
   assertFalse(between("0", "10").contains((VersionNumber) null));
   assertFalse(atLeast("10").contains((VersionNumber) null));
   assertFalse(atMost("10").contains((VersionNumber) null));
   assertFalse(between(null, "10").contains("5"));
   assertFalse(between("10", null).contains("15"));
   assertTrue(between(null, null).contains("10"));
}

### 180.Wrong Update Direction
link: https://github.com/oracle/opengrok/commit/d0c4c473ae9b7f6f09ee396aebe911a0d87af0f4
p_path: suggester/src/main/java/org/opengrok/suggest/Suggester.java#remove
t_path: suggester/src/test/java/org/opengrok/suggest/SuggesterTest.java#testRemove

```java:test_src

@Test
void testRemove() throws IOException {
   SuggesterTestData t = initSuggester();
   t.s.remove(Collections.singleton("test"));
   assertFalse(t.suggesterDir.resolve("test").toFile().exists());
   FileUtils.deleteDirectory(t.suggesterDir.toFile());
   FileUtils.deleteDirectory(t.indexDir.toFile());
}

```java:test_tgt

@Test
void testRemove() throws Exception {
   SuggesterTestData t = initSuggester();
   t.s.remove(Collections.singleton("test"));
   assertFalse(t.suggesterDir.resolve("test").toFile().exists());
   FileUtils.deleteDirectory(t.suggesterDir.toFile());
   FileUtils.deleteDirectory(t.indexDir.toFile());
}

```java:llm_gen

@Test
void testRemove() throws IOException {
   SuggesterTestData t = initSuggester();
   t.s.remove(Collections.singleton("test"));
   assertFalse(t.suggesterDir.resolve("test").toFile().exists());
   FileUtils.deleteDirectory(t.suggesterDir.toFile());
   FileUtils.deleteDirectory(t.indexDir.toFile());
}

### 181.Test Preparation Error
link: https://github.com/apache/flink/commit/4aa4507507b60ee4a2b7cc3624a9f36e4d3592ce
p_path: flink-runtime/src/main/java/org/apache/flink/runtime/io/network/partition/UnionResultSubpartitionView.java#releaseAllResources
t_path: flink-runtime/src/test/java/org/apache/flink/runtime/io/network/partition/UnionResultSubpartitionViewTest.java#testReleaseAllResources

```java:test_src

@Test
void testReleaseAllResources() throws IOException {
   assertThat(view.isReleased()).isFalse();
   assertThat(view0.isReleased()).isFalse();
   assertThat(view1.isReleased()).isFalse();
   view.releaseAllResources();
   assertThat(view.isReleased()).isTrue();
   assertThat(view0.isReleased()).isTrue();
   assertThat(view1.isReleased()).isTrue();
}

```java:test_tgt

@Test
void testReleaseAllResources() throws IOException {
   assertThat(view.isReleased()).isFalse();
   assertThat(view0.isReleased()).isFalse();
   assertThat(view1.isReleased()).isFalse();
   assertThat(buffers0).allMatch(x -> !x.isRecycled());
   assertThat(buffers1).allMatch(x -> !x.isRecycled());
   view0.notifyDataAvailable();
   view.releaseAllResources();
   assertThat(view.isReleased()).isTrue();
   assertThat(view0.isReleased()).isTrue();
   assertThat(view1.isReleased()).isTrue();
   assertThat(buffers0).allMatch(Buffer::isRecycled);
   assertThat(buffers1).allMatch(Buffer::isRecycled);
}

```java:llm_gen

@Test
void testReleaseAllResources() throws IOException {
   assertThat(view.isReleased()).isFalse();
   assertThat(view0.isReleased()).isFalse();
   assertThat(view1.isReleased()).isFalse();
   assertThat(allViews).isNotEmpty();
   assertThat(cachedBuffers).isNotEmpty();
   view.releaseAllResources();
   assertThat(view.isReleased()).isTrue();
   assertThat(view0.isReleased()).isTrue();
   assertThat(view1.isReleased()).isTrue();
   assertThat(allViews).isEmpty();
   assertThat(cachedBuffers).isEmpty();
}

### 182.Test Preparation Error
link: https://github.com/StarRocks/starrocks/commit/952bc956276f35b51e239eaceda8659a2eded4b1
p_path: fe/fe-core/src/main/java/com/starrocks/planner/SchemaScanNode.java#computeFeNodes
t_path: fe/fe-core/src/test/java/com/starrocks/planner/SchemaScanNodeTest.java#testComputeFeNodes

```java:test_src

@Test
public void testComputeFeNodes(@Mocked GlobalStateMgr globalStateMgr) {
   List<Frontend> frontends = new ArrayList<>();
   frontends.add(new Frontend());
   Frontend frontend = new Frontend();
   frontend.setAlive(true);
   frontends.add(frontend);
   new Expectations() {
       {
           GlobalStateMgr.getCurrentState();
           minTimes = 0;
           result = globalStateMgr;
           globalStateMgr.getFrontends(null);
           minTimes = 0;
           result = frontends;
       }
   };
   TupleDescriptor desc = new TupleDescriptor(new TupleId(0));
   SystemTable table = new SystemTable(0, "fe_metrics", null, null, null);
   desc.setTable(table);
   SchemaScanNode scanNode = new SchemaScanNode(new PlanNodeId(0), desc);
   scanNode.computeFeNodes();
   Assert.assertNotNull(scanNode.getFrontends());
}

```java:test_tgt

@Test
public void testComputeFeNodes(@Mocked GlobalStateMgr globalStateMgr) {
   List<Frontend> frontends = new ArrayList<>();
   frontends.add(new Frontend());
   Frontend frontend = new Frontend();
   frontend.setAlive(true);
   frontends.add(frontend);
   new Expectations() {
       {
           GlobalStateMgr.getCurrentState();
           minTimes = 0;
           result = globalStateMgr;
           globalStateMgr.getNodeMgr().getFrontends(null);
           minTimes = 0;
           result = frontends;
       }
   };
   TupleDescriptor desc = new TupleDescriptor(new TupleId(0));
   SystemTable table = new SystemTable(0, "fe_metrics", null, null, null);
   desc.setTable(table);
   SchemaScanNode scanNode = new SchemaScanNode(new PlanNodeId(0), desc);
   scanNode.computeFeNodes();
   Assert.assertNotNull(scanNode.getFrontends());
}

```java:llm_gen

@Test
public void testComputeFeNodes(@Mocked GlobalStateMgr globalStateMgr, @Mocked NodeMgr nodeMgr) {
   List<Frontend> frontends = new ArrayList<>();
   frontends.add(new Frontend());
   Frontend frontend = new Frontend();
   frontend.setAlive(true);
   frontends.add(frontend);
   new Expectations() {
       {
           GlobalStateMgr.getCurrentState();
           minTimes = 0;
           result = globalStateMgr;
           globalStateMgr.getNodeMgr();
           minTimes = 0;
           result = nodeMgr;
           nodeMgr.getFrontends(null);
           minTimes = 0;
           result = frontends;
       }
   };
   TupleDescriptor desc = new TupleDescriptor(new TupleId(0));
   SystemTable table = new SystemTable(0, "fe_metrics", null, null, null);
   desc.setTable(table);
   SchemaScanNode scanNode = new SchemaScanNode(new PlanNodeId(0), desc);
   scanNode.computeFeNodes();
   Assert.assertNotNull(scanNode.getFrontends());
}


### 183.Test Preparation Error
link: https://github.com/apache/kafka/commit/520aa8665c8bad19c55d74e6b8ac14a4e17de789
p_path: group-coordinator/src/main/java/org/apache/kafka/coordinator/group/consumer/TargetAssignmentBuilder.java#createAssignmentMemberSpec
t_path: group-coordinator/src/test/java/org/apache/kafka/coordinator/group/consumer/TargetAssignmentBuilderTest.java#testCreateAssignmentMemberSpec

```java:test_src

@Test
public void testCreateAssignmentMemberSpec() {
   Uuid fooTopicId = Uuid.randomUuid();
   Uuid barTopicId = Uuid.randomUuid();
   ConsumerGroupMember member = new ConsumerGroupMember.Builder("member-id").setSubscribedTopicNames(Arrays.asList("foo", "bar", "zar")).setRackId("rackId").setInstanceId("instanceId").build();
   Map<String, TopicMetadata> subscriptionMetadata = new HashMap<String, TopicMetadata>() {
       {
           put("foo", new TopicMetadata(fooTopicId, "foo", 5, Collections.emptyMap()));
           put("bar", new TopicMetadata(barTopicId, "bar", 5, Collections.emptyMap()));
       }
   };
   Assignment assignment = new Assignment(mkAssignment(mkTopicAssignment(fooTopicId, 1, 2, 3), mkTopicAssignment(barTopicId, 1, 2, 3)));
   AssignmentMemberSpec assignmentMemberSpec = createAssignmentMemberSpec(member, assignment, subscriptionMetadata);
   assertEquals(new AssignmentMemberSpec(Optional.of("instanceId"), Optional.of("rackId"), new HashSet<>(Arrays.asList(fooTopicId, barTopicId)), assignment.partitions()), assignmentMemberSpec);
}

```java:test_tgt

@Test
public void testCreateAssignmentMemberSpec() {
   Uuid fooTopicId = Uuid.randomUuid();
   Uuid barTopicId = Uuid.randomUuid();
   TopicsImage topicsImage = new MetadataImageBuilder().addTopic(fooTopicId, "foo", 5).addTopic(barTopicId, "bar", 5).build().topics();
   ConsumerGroupMember member = new ConsumerGroupMember.Builder("member-id").setSubscribedTopicNames(Arrays.asList("foo", "bar", "zar")).setRackId("rackId").setInstanceId("instanceId").build();
   Assignment assignment = new Assignment(mkAssignment(mkTopicAssignment(fooTopicId, 1, 2, 3), mkTopicAssignment(barTopicId, 1, 2, 3)));
   AssignmentMemberSpec assignmentMemberSpec = createAssignmentMemberSpec(member, assignment, topicsImage);
   assertEquals(new AssignmentMemberSpec(Optional.of("instanceId"), Optional.of("rackId"), new TopicIds(mkSet("bar", "foo", "zar"), topicsImage), assignment.partitions()), assignmentMemberSpec);
}

```java:llm_gen

@Test
public void testCreateAssignmentMemberSpec() {
   Uuid fooTopicId = Uuid.randomUuid();
   Uuid barTopicId = Uuid.randomUuid();
   ConsumerGroupMember member = new ConsumerGroupMember.Builder("member-id").setSubscribedTopicNames(Arrays.asList("foo", "bar", "zar")).setRackId("rackId").setInstanceId("instanceId").build();
   TopicsImage topicsImage = new TopicsImage(new HashMap<String, Uuid>() {
       {
           put("foo", fooTopicId);
           put("bar", barTopicId);
       }
   }, Collections.emptyMap());
   Assignment assignment = new Assignment(mkAssignment(mkTopicAssignment(fooTopicId, 1, 2, 3), mkTopicAssignment(barTopicId, 1, 2, 3)));
   AssignmentMemberSpec assignmentMemberSpec = createAssignmentMemberSpec(member, assignment, topicsImage);
   assertEquals(new AssignmentMemberSpec(Optional.of("instanceId"), Optional.of("rackId"), new TopicIds(new HashSet<>(Arrays.asList("foo", "bar", "zar")), topicsImage), assignment.partitions()), assignmentMemberSpec);
}


### 184.Missing Asserts
link: https://github.com/StarRocks/starrocks/commit/dee7bbd4ba5dc910b2ca112c8e98303ab379b091
p_path: fe/fe-core/src/main/java/com/starrocks/http/rest/MetricsAction.java#parseRequestParams
t_path: fe/fe-core/src/test/java/com/starrocks/http/MetricsActionTest.java#testParseRequestParams

```java:test_src

@Test
public void testParseRequestParams() {
   ActionController controller = new ActionController();
   MockMetricsAction action = new MockMetricsAction(controller);
   {
       BaseRequest request = buildBaseRequest("/metrics", true);
       new Expectations(request) {
           {
               request.getAuthorizationHeader();
               result = new Exception("Don't expect check auth header");
               minTimes = 0;
               maxTimes = 0;
           }
       };
       MetricsAction.RequestParams params = action.callParseRequestParams(request);
       Assert.assertNotNull(params);
       Assert.assertFalse(params.isCollectMVMetrics());
       Assert.assertTrue(params.isMinifyMVMetrics());
       Assert.assertFalse(params.isCollectTableMetrics());
       Assert.assertTrue(params.isMinifyTableMetrics());
   }
   {
       BaseRequest request = buildBaseRequest("/metrics?with_table_metrics=all", false);
       new Expectations(request) {
           {
               request.getAuthorizationHeader();
               minTimes = 1;
           }
       };
       MetricsAction.RequestParams params = action.callParseRequestParams(request);
       Assert.assertNotNull(params);
       Assert.assertFalse(params.isCollectMVMetrics());
       Assert.assertTrue(params.isMinifyMVMetrics());
       Assert.assertFalse(params.isCollectTableMetrics());
       Assert.assertTrue(params.isMinifyTableMetrics());
   }
   {
       BaseRequest request = buildBaseRequest("/metrics?with_table_metrics=all", true);
       new Expectations(request) {
           {
               request.getHostString();
               result = "127.0.0.1";
           }
       };
       MetricsAction.RequestParams params = action.callParseRequestParams(request);
       Assert.assertNotNull(params);
       Assert.assertFalse(params.isCollectMVMetrics());
       Assert.assertTrue(params.isMinifyMVMetrics());
       Assert.assertTrue(params.isCollectTableMetrics());
       Assert.assertFalse(params.isMinifyTableMetrics());
   }
   {
       BaseRequest request = buildBaseRequest("/metrics?with_table_metrics=all&with_materialized_view_metrics=all", true);
       new Expectations(request) {
           {
               request.getHostString();
               result = "127.0.0.1";
           }
       };
       MetricsAction.RequestParams params = action.callParseRequestParams(request);
       Assert.assertNotNull(params);
       Assert.assertTrue(params.isCollectMVMetrics());
       Assert.assertFalse(params.isMinifyMVMetrics());
       Assert.assertTrue(params.isCollectTableMetrics());
       Assert.assertFalse(params.isMinifyTableMetrics());
   }
}

```java:test_tgt

@Test
public void testParseRequestParams() {
   ActionController controller = new ActionController();
   MockMetricsAction action = new MockMetricsAction(controller);
   {
       BaseRequest request = buildBaseRequest("/metrics", true);
       new Expectations(request) {
           {
               request.getAuthorizationHeader();
               result = new Exception("Don't expect check auth header");
               minTimes = 0;
               maxTimes = 0;
           }
       };
       MetricsAction.RequestParams params = action.callParseRequestParams(request);
       Assert.assertNotNull(params);
       Assert.assertFalse(params.isCollectMVMetrics());
       Assert.assertFalse(params.isMinifyMVMetrics());
       Assert.assertFalse(params.isCollectTableMetrics());
       Assert.assertFalse(params.isMinifyTableMetrics());
   }
   {
       BaseRequest request = buildBaseRequest("/metrics?with_table_metrics=all", false);
       new Expectations(request) {
           {
               request.getAuthorizationHeader();
               minTimes = 1;
           }
       };
       MetricsAction.RequestParams params = action.callParseRequestParams(request);
       Assert.assertNotNull(params);
       Assert.assertFalse(params.isCollectMVMetrics());
       Assert.assertFalse(params.isMinifyMVMetrics());
       Assert.assertFalse(params.isCollectTableMetrics());
       Assert.assertFalse(params.isMinifyTableMetrics());
   }
   {
       BaseRequest request = buildBaseRequest("/metrics?with_table_metrics=all", true);
       new Expectations(request) {
           {
               request.getHostString();
               result = "127.0.0.1";
           }
       };
       MetricsAction.RequestParams params = action.callParseRequestParams(request);
       Assert.assertNotNull(params);
       Assert.assertFalse(params.isCollectMVMetrics());
       Assert.assertFalse(params.isMinifyMVMetrics());
       Assert.assertTrue(params.isCollectTableMetrics());
       Assert.assertFalse(params.isMinifyTableMetrics());
   }
   {
       BaseRequest request = buildBaseRequest("/metrics?with_table_metrics=all&with_materialized_view_metrics=all", true);
       new Expectations(request) {
           {
               request.getHostString();
               result = "127.0.0.1";
           }
       };
       MetricsAction.RequestParams params = action.callParseRequestParams(request);
       Assert.assertNotNull(params);
       Assert.assertTrue(params.isCollectMVMetrics());
       Assert.assertFalse(params.isMinifyMVMetrics());
       Assert.assertTrue(params.isCollectTableMetrics());
       Assert.assertFalse(params.isMinifyTableMetrics());
   }
   {
       BaseRequest request = buildBaseRequest("/metrics?with_materialized_view_metrics=all", false);
       new Expectations(request) {
           {
               request.getAuthorizationHeader();
               minTimes = 1;
           }
       };
       MetricsAction.RequestParams params = action.callParseRequestParams(request);
       Assert.assertNotNull(params);
       Assert.assertFalse(params.isCollectMVMetrics());
       Assert.assertFalse(params.isMinifyMVMetrics());
       Assert.assertFalse(params.isCollectTableMetrics());
       Assert.assertFalse(params.isMinifyTableMetrics());
   }
   {
       BaseRequest request = buildBaseRequest("/metrics?with_materialized_view_metrics=all", true);
       new Expectations(request) {
           {
               request.getHostString();
               result = "127.0.0.1";
           }
       };
       MetricsAction.RequestParams params = action.callParseRequestParams(request);
       Assert.assertNotNull(params);
       Assert.assertTrue(params.isCollectMVMetrics());
       Assert.assertFalse(params.isMinifyMVMetrics());
       Assert.assertFalse(params.isCollectTableMetrics());
       Assert.assertFalse(params.isMinifyTableMetrics());
   }
   {
       BaseRequest request = buildBaseRequest("/metrics?with_materialized_view_metrics=minified", true);
       new Expectations(request) {
           {
               request.getHostString();
               result = "127.0.0.1";
           }
       };
       MetricsAction.RequestParams params = action.callParseRequestParams(request);
       Assert.assertNotNull(params);
       Assert.assertTrue(params.isCollectMVMetrics());
       Assert.assertTrue(params.isMinifyMVMetrics());
       Assert.assertFalse(params.isCollectTableMetrics());
       Assert.assertFalse(params.isMinifyTableMetrics());
   }
   {
       BaseRequest request = buildBaseRequest("/metrics?with_table_metrics=minified&with_materialized_view_metrics=minified", true);
       new Expectations(request) {
           {
               request.getHostString();
               result = "127.0.0.1";
           }
       };
       MetricsAction.RequestParams params = action.callParseRequestParams(request);
       Assert.assertNotNull(params);
       Assert.assertTrue(params.isCollectMVMetrics());
       Assert.assertTrue(params.isMinifyMVMetrics());
       Assert.assertTrue(params.isCollectTableMetrics());
       Assert.assertTrue(params.isMinifyTableMetrics());
   }
}

```java:llm_gen

@Test
public void testParseRequestParams() {
   ActionController controller = new ActionController();
   MockMetricsAction action = new MockMetricsAction(controller);
   {
       BaseRequest request = buildBaseRequest("/metrics", true);
       new Expectations(request) {
           {
               request.getAuthorizationHeader();
               result = new Exception("Don't expect check auth header");
               minTimes = 0;
               maxTimes = 0;
           }
       };
       MetricsAction.RequestParams params = action.callParseRequestParams(request);
       Assert.assertNotNull(params);
       Assert.assertFalse(params.isCollectMVMetrics());
       Assert.assertTrue(params.isCollectMVMetricsMinifiedMode());
       Assert.assertFalse(params.isCollectTableMetrics());
       Assert.assertTrue(params.isCollectTableMetricsMinifiedMode());
   }
   {
       BaseRequest request = buildBaseRequest("/metrics?with_table_metrics=all", false);
       new Expectations(request) {
           {
               request.getAuthorizationHeader();
               minTimes = 1;
           }
       };
       MetricsAction.RequestParams params = action.callParseRequestParams(request);
       Assert.assertNotNull(params);
       Assert.assertFalse(params.isCollectMVMetrics());
       Assert.assertTrue(params.isCollectMVMetricsMinifiedMode());
       Assert.assertFalse(params.isCollectTableMetrics());
       Assert.assertTrue(params.isCollectTableMetricsMinifiedMode());
   }
   {
       BaseRequest request = buildBaseRequest("/metrics?with_table_metrics=all", true);
       new Expectations(request) {
           {
               request.getHostString();
               result = "127.0.0.1";
           }
       };
       MetricsAction.RequestParams params = action.callParseRequestParams(request);
       Assert.assertNotNull(params);
       Assert.assertFalse(params.isCollectMVMetrics());
       Assert.assertTrue(params.isCollectMVMetricsMinifiedMode());
       Assert.assertTrue(params.isCollectTableMetrics());
       Assert.assertFalse(params.isCollectTableMetricsMinifiedMode());
   }
   {
       BaseRequest request = buildBaseRequest("/metrics?with_table_metrics=all&with_materialized_view_metrics=all", true);
       new Expectations(request) {
           {
               request.getHostString();
               result = "127.0.0.1";
           }
       };
       MetricsAction.RequestParams params = action.callParseRequestParams(request);
       Assert.assertNotNull(params);
       Assert.assertTrue(params.isCollectMVMetrics());
       Assert.assertFalse(params.isCollectMVMetricsMinifiedMode());
       Assert.assertTrue(params.isCollectTableMetrics());
       Assert.assertFalse(params.isCollectTableMetricsMinifiedMode());
   }
}

### 185.Wrong Update Direction
link: https://github.com/alibaba/nacos/commit/5169f06654a57db4f01cde83406bbc1ba07d4a29
p_path: common/src/main/java/com/alibaba/nacos/common/remote/client/grpc/DefaultGrpcClientConfig.java#fromProperties
t_path: common/src/test/java/com/alibaba/nacos/common/remote/client/grpc/DefaultGrpcClientConfigTest.java#testFromProperties

```java:test_src

@Test
public void testFromProperties() {
   Properties properties = new Properties();
   properties.setProperty(GrpcConstants.GRPC_NAME, "test");
   properties.setProperty(GrpcConstants.GRPC_RETRY_TIMES, "3");
   properties.setProperty(GrpcConstants.GRPC_TIMEOUT_MILLS, "3000");
   properties.setProperty(GrpcConstants.GRPC_CONNECT_KEEP_ALIVE_TIME, "5000");
   properties.setProperty(GrpcConstants.GRPC_THREADPOOL_KEEPALIVETIME, "10000");
   properties.setProperty(GrpcConstants.GRPC_THREADPOOL_CORE_SIZE, "2");
   properties.setProperty(GrpcConstants.GRPC_THREADPOOL_MAX_SIZE, "8");
   properties.setProperty(GrpcConstants.GRPC_SERVER_CHECK_TIMEOUT, "3000");
   properties.setProperty(GrpcConstants.GRPC_QUEUESIZE, "10000");
   properties.setProperty(GrpcConstants.GRPC_MAX_INBOUND_MESSAGE_SIZE, "10485760");
   properties.setProperty(GrpcConstants.GRPC_CHANNEL_KEEP_ALIVE_TIME, "60000");
   properties.setProperty(GrpcConstants.GRPC_CHANNEL_KEEP_ALIVE_TIMEOUT, "20000");
   properties.setProperty(GrpcConstants.GRPC_HEALTHCHECK_RETRY_TIMES, "3");
   properties.setProperty(GrpcConstants.GRPC_HEALTHCHECK_TIMEOUT, "3000");
   properties.setProperty(GrpcConstants.GRPC_CHANNEL_CAPABILITY_NEGOTIATION_TIMEOUT, "5000");
   DefaultGrpcClientConfig config = (DefaultGrpcClientConfig) DefaultGrpcClientConfig.newBuilder().fromProperties(properties).build();
   assertEquals("test", config.name());
   assertEquals(3, config.retryTimes());
   assertEquals(3000, config.timeOutMills());
   assertEquals(5000, config.connectionKeepAlive());
   assertEquals(10000, config.threadPoolKeepAlive());
   assertEquals(2, config.threadPoolCoreSize());
   assertEquals(8, config.threadPoolMaxSize());
   assertEquals(3000, config.serverCheckTimeOut());
   assertEquals(10000, config.threadPoolQueueSize());
   assertEquals(10485760, config.maxInboundMessageSize());
   assertEquals(60000, config.channelKeepAlive());
   assertEquals(20000, config.channelKeepAliveTimeout());
   assertEquals(3, config.healthCheckRetryTimes());
   assertEquals(3000, config.healthCheckTimeOut());
   assertEquals(5000, config.capabilityNegotiationTimeout());
   assertEquals(1, config.labels().size());
   assertNotNull(config.tlsConfig());
}

```java:test_tgt

@Test
public void testFromProperties() {
   Properties properties = new Properties();
   properties.setProperty(GrpcConstants.GRPC_NAME, "test");
   properties.setProperty(GrpcConstants.GRPC_RETRY_TIMES, "3");
   properties.setProperty(GrpcConstants.GRPC_TIMEOUT_MILLS, "3000");
   properties.setProperty(GrpcConstants.GRPC_CONNECT_KEEP_ALIVE_TIME, "5000");
   properties.setProperty(GrpcConstants.GRPC_THREADPOOL_KEEPALIVETIME, "10000");
   properties.setProperty(GrpcConstants.GRPC_THREADPOOL_CORE_SIZE, "2");
   properties.setProperty(GrpcConstants.GRPC_THREADPOOL_MAX_SIZE, "8");
   properties.setProperty(GrpcConstants.GRPC_SERVER_CHECK_TIMEOUT, "3000");
   properties.setProperty(GrpcConstants.GRPC_QUEUESIZE, "10000");
   properties.setProperty(GrpcConstants.GRPC_MAX_INBOUND_MESSAGE_SIZE, "10485760");
   properties.setProperty(GrpcConstants.GRPC_CHANNEL_KEEP_ALIVE_TIME, "60000");
   properties.setProperty(GrpcConstants.GRPC_CHANNEL_KEEP_ALIVE_TIMEOUT, "20000");
   properties.setProperty(GrpcConstants.GRPC_HEALTHCHECK_RETRY_TIMES, "3");
   properties.setProperty(GrpcConstants.GRPC_HEALTHCHECK_TIMEOUT, "3000");
   properties.setProperty(GrpcConstants.GRPC_CHANNEL_CAPABILITY_NEGOTIATION_TIMEOUT, "5000");
   DefaultGrpcClientConfig config = (DefaultGrpcClientConfig) DefaultGrpcClientConfig.newBuilder().fromProperties(properties, null).build();
   assertEquals("test", config.name());
   assertEquals(3, config.retryTimes());
   assertEquals(3000, config.timeOutMills());
   assertEquals(5000, config.connectionKeepAlive());
   assertEquals(10000, config.threadPoolKeepAlive());
   assertEquals(2, config.threadPoolCoreSize());
   assertEquals(8, config.threadPoolMaxSize());
   assertEquals(3000, config.serverCheckTimeOut());
   assertEquals(10000, config.threadPoolQueueSize());
   assertEquals(10485760, config.maxInboundMessageSize());
   assertEquals(60000, config.channelKeepAlive());
   assertEquals(20000, config.channelKeepAliveTimeout());
   assertEquals(3, config.healthCheckRetryTimes());
   assertEquals(3000, config.healthCheckTimeOut());
   assertEquals(5000, config.capabilityNegotiationTimeout());
   assertEquals(1, config.labels().size());
   assertNotNull(config.tlsConfig());
}

```java:llm_gen

@Test
public void testFromProperties() {
   Properties properties = new Properties();
   properties.setProperty(GrpcConstants.GRPC_NAME, "test");
   properties.setProperty(GrpcConstants.GRPC_RETRY_TIMES, "3");
   properties.setProperty(GrpcConstants.GRPC_TIMEOUT_MILLS, "3000");
   properties.setProperty(GrpcConstants.GRPC_CONNECT_KEEP_ALIVE_TIME, "5000");
   properties.setProperty(GrpcConstants.GRPC_THREADPOOL_KEEPALIVETIME, "10000");
   properties.setProperty(GrpcConstants.GRPC_THREADPOOL_CORE_SIZE, "2");
   properties.setProperty(GrpcConstants.GRPC_THREADPOOL_MAX_SIZE, "8");
   properties.setProperty(GrpcConstants.GRPC_SERVER_CHECK_TIMEOUT, "3000");
   properties.setProperty(GrpcConstants.GRPC_QUEUESIZE, "10000");
   properties.setProperty(GrpcConstants.GRPC_MAX_INBOUND_MESSAGE_SIZE, "10485760");
   properties.setProperty(GrpcConstants.GRPC_CHANNEL_KEEP_ALIVE_TIME, "60000");
   properties.setProperty(GrpcConstants.GRPC_CHANNEL_KEEP_ALIVE_TIMEOUT, "20000");
   properties.setProperty(GrpcConstants.GRPC_HEALTHCHECK_RETRY_TIMES, "3");
   properties.setProperty(GrpcConstants.GRPC_HEALTHCHECK_TIMEOUT, "3000");
   properties.setProperty(GrpcConstants.GRPC_CHANNEL_CAPABILITY_NEGOTIATION_TIMEOUT, "5000");
   RpcClientTlsConfig tlsConfig = RpcClientTlsConfig.properties(properties);
   DefaultGrpcClientConfig config = (DefaultGrpcClientConfig) DefaultGrpcClientConfig.newBuilder().fromProperties(properties, tlsConfig).build();
   assertEquals("test", config.name());
   assertEquals(3, config.retryTimes());
   assertEquals(3000, config.timeOutMills());
   assertEquals(5000, config.connectionKeepAlive());
   assertEquals(10000, config.threadPoolKeepAlive());
   assertEquals(2, config.threadPoolCoreSize());
   assertEquals(8, config.threadPoolMaxSize());
   assertEquals(3000, config.serverCheckTimeOut());
   assertEquals(10000, config.threadPoolQueueSize());
   assertEquals(10485760, config.maxInboundMessageSize());
   assertEquals(60000, config.channelKeepAlive());
   assertEquals(20000, config.channelKeepAliveTimeout());
   assertEquals(3, config.healthCheckRetryTimes());
   assertEquals(3000, config.healthCheckTimeOut());
   assertEquals(5000, config.capabilityNegotiationTimeout());
   assertEquals(1, config.labels().size());
   assertEquals(tlsConfig, config.tlsConfig());
}

### 186.Missing Asserts
link: https://github.com/apache/dolphinscheduler/commit/8efaa9fa1f1a5ab70dad0137df13da6480be59e9
p_path: dolphinscheduler-task-plugin/dolphinscheduler-task-api/src/main/java/org/apache/dolphinscheduler/plugin/task/api/utils/JdbcUrlParser.java#getJdbcInfo
t_path: dolphinscheduler-task-plugin/dolphinscheduler-task-api/src/test/java/org/apache/dolphinscheduler/plugin/task/api/utils/JdbcUrlParserTest.java#testGetJdbcInfo

```java:test_src

@Test
public void testGetJdbcInfo() {
   JdbcInfo jdbcInfo = JdbcUrlParser.getJdbcInfo("jdbc:mysql://localhost:3306/dolphinscheduler?" + "useUnicode=true&characterEncoding=UTF-8");
   if (jdbcInfo != null) {
       String jdbcInfoStr = jdbcInfo.toString();
       String expected = "JdbcInfo{host='localhost', port='3306', " + "driverName='mysql', database='dolphinscheduler', " + "params='useUnicode=true&characterEncoding=UTF-8', " + "address='jdbc:mysql://localhost:3306'}";
       Assertions.assertEquals(expected, jdbcInfoStr);
   }
}

```java:test_tgt

@Test
public void testGetJdbcInfo() {
   JdbcInfo jdbcInfo = JdbcUrlParser.getJdbcInfo("jdbc:mysql://localhost:3306/dolphinscheduler?" + "useUnicode=true&characterEncoding=UTF-8");
   if (jdbcInfo != null) {
       String jdbcInfoStr = jdbcInfo.toString();
       String expected = "JdbcInfo(host=localhost, port=3306, driverName=mysql, database=dolphinscheduler, " + "params={useUnicode=true, characterEncoding=UTF-8}, address=jdbc:mysql://localhost:3306, jdbcUrl=jdbc:mysql://localhost:3306/dolphinscheduler)";
       Assertions.assertEquals(expected, jdbcInfoStr);
   }
   // bad jdbc url case
   jdbcInfo = JdbcUrlParser.getJdbcInfo("jdbc:mysql://localhost:3306/dolphinscheduler?" + "useUnicode=true&&characterEncoding=UTF-8");
   if (jdbcInfo != null) {
       String jdbcInfoStr = jdbcInfo.toString();
       String expected = "JdbcInfo(host=localhost, port=3306, driverName=mysql, database=dolphinscheduler, " + "params={useUnicode=true, characterEncoding=UTF-8}, address=jdbc:mysql://localhost:3306, jdbcUrl=jdbc:mysql://localhost:3306/dolphinscheduler)";
       Assertions.assertEquals(expected, jdbcInfoStr);
   }
}

```java:llm_gen

@Test
public void testGetJdbcInfo() {
   JdbcInfo jdbcInfo = JdbcUrlParser.getJdbcInfo("jdbc:mysql://localhost:3306/dolphinscheduler?" + "useUnicode=true&characterEncoding=UTF-8");
   if (jdbcInfo != null) {
       String jdbcInfoStr = jdbcInfo.toString();
       String expected = "JdbcInfo{host='localhost', port='3306', " + "driverName='mysql', database='dolphinscheduler', " + "params={useUnicode=true, characterEncoding=UTF-8}, " + "address='jdbc:mysql://localhost:3306', jdbcUrl='jdbc:mysql://localhost:3306/dolphinscheduler'}";
       Assertions.assertEquals(expected, jdbcInfoStr);
   }
}


### 187.Wrong Update Direction
link: https://github.com/confluentinc/ksql/commit/08eb59f516a8a19c348516fa8f7a995c1d1820ea
p_path: ksqldb-engine/src/main/java/io/confluent/ksql/services/DefaultConnectClient.java#create
t_path: ksqldb-engine/src/test/java/io/confluent/ksql/services/DefaultConnectClientTest.java#testCreate

```java:test_src

@Test
public void testCreate() throws JsonProcessingException {
   WireMock.stubFor(WireMock.post(WireMock.urlEqualTo("/connectors")).withHeader(AUTHORIZATION.toString(), new EqualToPattern(AUTH_HEADER)).willReturn(WireMock.aResponse().withStatus(HttpStatus.SC_CREATED).withBody(MAPPER.writeValueAsString(SAMPLE_INFO))));
   final ConnectResponse<ConnectorInfo> response = client.create("foo", ImmutableMap.of());
   assertThat(response.datum(), OptionalMatchers.of(is(SAMPLE_INFO)));
   assertThat("Expected no error!", !response.error().isPresent());
}

```java:test_tgt

@Test
public void testCreate() throws JsonProcessingException {
   WireMock.stubFor(WireMock.post(WireMock.urlEqualTo(pathPrefix + "/connectors")).withHeader(AUTHORIZATION.toString(), new EqualToPattern(AUTH_HEADER)).withHeader(CUSTOM_HEADER_NAME, new EqualToPattern(CUSTOM_HEADER_VALUE)).willReturn(WireMock.aResponse().withStatus(HttpStatus.SC_CREATED).withBody(MAPPER.writeValueAsString(SAMPLE_INFO))));
   final ConnectResponse<ConnectorInfo> response = client.create("foo", ImmutableMap.of());
   assertThat(response.datum(), OptionalMatchers.of(is(SAMPLE_INFO)));
   assertThat("Expected no error!", !response.error().isPresent());
}

```java:llm_gen

@Test
public void testCreate() throws JsonProcessingException {
   WireMock.stubFor(WireMock.post(WireMock.urlEqualTo("/connectors"))
       .withHeader(AUTHORIZATION.toString(), new EqualToPattern(AUTH_HEADER))
       .willReturn(WireMock.aResponse()
           .withStatus(HttpStatus.SC_CREATED)
           .withBody(MAPPER.writeValueAsString(SAMPLE_INFO))));
   final ConnectResponse<ConnectorInfo> response = client.create("foo", ImmutableMap.of("config", "value"));
   assertThat(response.datum(), OptionalMatchers.of(is(SAMPLE_INFO)));
   assertThat("Expected no error!", !response.error().isPresent());
}

### 188.External Class Modification
link: https://github.com/apache/opennlp/commit/5c3d7e1b919c055a6fd07720e2ce0407a4bb9c2b
p_path: opennlp-tools/src/main/java/opennlp/tools/ml/BeamSearch.java#bestSequence
t_path: opennlp-tools/src/test/java/opennlp/tools/ml/BeamSearchTest.java#testBestSequence

```java:test_src

@Test
void testBestSequence() {
   String[] sequence = { "1", "2", "3", "2", "1" };
   BeamSearchContextGenerator<String> cg = new IdentityFeatureGenerator(sequence);
   String[] outcomes = new String[] { "1", "2", "3" };
   MaxentModel model = new IdentityModel(outcomes);
   BeamSearch<String> bs = new BeamSearch<>(2, model);
   Sequence seq = bs.bestSequence(sequence, null, cg, (int i, String[] inputSequence, String[] outcomesSequence, String outcome) -> true);
   Assertions.assertNotNull(seq);
   Assertions.assertEquals(sequence.length, seq.getOutcomes().size());
   Assertions.assertEquals("1", seq.getOutcomes().get(0));
   Assertions.assertEquals("2", seq.getOutcomes().get(1));
   Assertions.assertEquals("3", seq.getOutcomes().get(2));
   Assertions.assertEquals("2", seq.getOutcomes().get(3));
   Assertions.assertEquals("1", seq.getOutcomes().get(4));
}

```java:test_tgt

@Test
void testBestSequence() {
   String[] sequence = { "1", "2", "3", "2", "1" };
   BeamSearchContextGenerator<String> cg = new IdentityFeatureGenerator(sequence);
   String[] outcomes = new String[] { "1", "2", "3" };
   MaxentModel model = new IdentityModel(outcomes);
   BeamSearch bs = new BeamSearch(2, model);
   Sequence seq = bs.bestSequence(sequence, null, cg, (int i, String[] inputSequence, String[] outcomesSequence, String outcome) -> true);
   Assertions.assertNotNull(seq);
   Assertions.assertEquals(sequence.length, seq.getOutcomes().size());
   Assertions.assertEquals("1", seq.getOutcomes().get(0));
   Assertions.assertEquals("2", seq.getOutcomes().get(1));
   Assertions.assertEquals("3", seq.getOutcomes().get(2));
   Assertions.assertEquals("2", seq.getOutcomes().get(3));
   Assertions.assertEquals("1", seq.getOutcomes().get(4));
}

```java:llm_gen

@Test
void testBestSequence() {
   String[] sequence = { "1", "2", "3", "2", "1" };
   BeamSearchContextGenerator<String> cg = new IdentityFeatureGenerator(sequence);
   String[] outcomes = new String[] { "1", "2", "3" };
   MaxentModel model = new IdentityModel(outcomes);
   BeamSearch<String> bs = new BeamSearch<>(2, model);
   Sequence seq = bs.bestSequence(sequence, null, cg, (i, inputSequence, outcomesSequence, outcome) -> true);
   Assertions.assertNotNull(seq);
   Assertions.assertEquals(sequence.length, seq.getOutcomes().size());
   Assertions.assertEquals("1", seq.getOutcomes().get(0));
   Assertions.assertEquals("2", seq.getOutcomes().get(1));
   Assertions.assertEquals("3", seq.getOutcomes().get(2));
   Assertions.assertEquals("2", seq.getOutcomes().get(3));
   Assertions.assertEquals("1", seq.getOutcomes().get(4));
}

### 189.Missing Asserts
link: https://github.com/thingsboard/thingsboard/commit/96112e94d8b92533471320a899e5a25fd769e01d
p_path: application/src/main/java/org/thingsboard/server/controller/WidgetTypeController.java#getBundleWidgetTypes
t_path: application/src/test/java/org/thingsboard/server/controller/WidgetTypeControllerTest.java#testGetBundleWidgetTypes

```java:test_src

@Test
public void testGetBundleWidgetTypes() throws Exception {
   WidgetsBundle widgetsBundle = new WidgetsBundle();
   widgetsBundle.setTitle("My widgets bundle");
   widgetsBundle = doPost("/api/widgetsBundle", widgetsBundle, WidgetsBundle.class);
   List<WidgetType> widgetTypes = new ArrayList<>();
   for (int i = 0; i < 89; i++) {
       WidgetTypeDetails widgetType = new WidgetTypeDetails();
       widgetType.setName("Widget Type " + i);
       widgetType.setDescriptor(JacksonUtil.fromString("{ \"someKey\": \"someValue\" }", JsonNode.class));
       widgetTypes.add(new WidgetType(doPost("/api/widgetType", widgetType, WidgetTypeDetails.class)));
   }
   List<String> widgetTypeIds = widgetTypes.stream().map(type -> type.getId().getId().toString()).collect(Collectors.toList());
   doPost("/api/widgetsBundle/" + widgetsBundle.getId().getId().toString() + "/widgetTypes", widgetTypeIds);
   List<WidgetType> loadedWidgetTypes = doGetTyped("/api/widgetTypes?widgetsBundleId={widgetsBundleId}", new TypeReference<>() {
   }, widgetsBundle.getId().getId().toString());
   Collections.sort(widgetTypes, idComparator);
   Collections.sort(loadedWidgetTypes, idComparator);
   Assert.assertEquals(widgetTypes, loadedWidgetTypes);
}

```java:test_tgt

@Test
public void testGetBundleWidgetTypes() throws Exception {
   WidgetsBundle widgetsBundle = new WidgetsBundle();
   widgetsBundle.setTitle("My widgets bundle");
   widgetsBundle = doPost("/api/widgetsBundle", widgetsBundle, WidgetsBundle.class);
   List<WidgetType> widgetTypes = new ArrayList<>();
   for (int i = 0; i < 89; i++) {
       WidgetTypeDetails widgetType = new WidgetTypeDetails();
       widgetType.setName("Widget Type " + i);
       widgetType.setDescriptor(JacksonUtil.fromString("{ \"someKey\": \"someValue\" }", JsonNode.class));
       widgetTypes.add(new WidgetType(doPost("/api/widgetType", widgetType, WidgetTypeDetails.class)));
   }
   List<String> widgetTypeIds = widgetTypes.stream().map(type -> type.getId().getId().toString()).collect(Collectors.toList());
   doPost("/api/widgetsBundle/" + widgetsBundle.getId().getId().toString() + "/widgetTypes", widgetTypeIds);
   List<WidgetType> loadedWidgetTypes = doGetTyped("/api/widgetTypes?widgetsBundleId={widgetsBundleId}", new TypeReference<>() {
   }, widgetsBundle.getId().getId().toString());
   Collections.sort(widgetTypes, idComparator);
   Collections.sort(loadedWidgetTypes, idComparator);
   Assert.assertEquals(widgetTypes, loadedWidgetTypes);
   loginCustomerUser();
   List<WidgetType> loadedWidgetTypesCustomer = doGetTyped("/api/widgetTypes?widgetsBundleId={widgetsBundleId}", new TypeReference<>() {
   }, widgetsBundle.getId().getId().toString());
   Collections.sort(loadedWidgetTypesCustomer, idComparator);
   Assert.assertEquals(widgetTypes, loadedWidgetTypesCustomer);
   List<WidgetTypeDetails> customerLoadedWidgetTypesDetails = doGetTyped("/api/widgetTypesDetails?widgetsBundleId={widgetsBundleId}", new TypeReference<>() {
   }, widgetsBundle.getId().getId().toString());
   List<WidgetType> widgetTypesFromDetailsListCustomer = customerLoadedWidgetTypesDetails.stream().map(WidgetType::new).collect(Collectors.toList());
   Collections.sort(widgetTypesFromDetailsListCustomer, idComparator);
   Assert.assertEquals(widgetTypesFromDetailsListCustomer, loadedWidgetTypes);
   loginSysAdmin();
   List<WidgetType> sysAdminLoadedWidgetTypes = doGetTyped("/api/widgetTypes?widgetsBundleId={widgetsBundleId}", new TypeReference<>() {
   }, widgetsBundle.getId().getId().toString());
   Collections.sort(sysAdminLoadedWidgetTypes, idComparator);
   Assert.assertEquals(widgetTypes, sysAdminLoadedWidgetTypes);
   List<WidgetTypeDetails> sysAdminLoadedWidgetTypesDetails = doGetTyped("/api/widgetTypesDetails?widgetsBundleId={widgetsBundleId}", new TypeReference<>() {
   }, widgetsBundle.getId().getId().toString());
   List<WidgetType> widgetTypesFromDetailsListSysAdmin = sysAdminLoadedWidgetTypesDetails.stream().map(WidgetType::new).collect(Collectors.toList());
   Collections.sort(widgetTypesFromDetailsListSysAdmin, idComparator);
   Assert.assertEquals(widgetTypesFromDetailsListSysAdmin, loadedWidgetTypes);
}

```java:llm_gen

@Test
public void testGetBundleWidgetTypes() throws Exception {
   loginCustomerUser();
   WidgetsBundle widgetsBundle = new WidgetsBundle();
   widgetsBundle.setTitle("My widgets bundle");
   widgetsBundle = doPost("/api/widgetsBundle", widgetsBundle, WidgetsBundle.class);
   List<WidgetType> widgetTypes = new ArrayList<>();
   for (int i = 0; i < 89; i++) {
       WidgetTypeDetails widgetType = new WidgetTypeDetails();
       widgetType.setName("Widget Type " + i);
       widgetType.setDescriptor(JacksonUtil.fromString("{ \"someKey\": \"someValue\" }", JsonNode.class));
       widgetTypes.add(new WidgetType(doPost("/api/widgetType", widgetType, WidgetTypeDetails.class)));
   }
   List<String> widgetTypeIds = widgetTypes.stream().map(type -> type.getId().getId().toString()).collect(Collectors.toList());
   doPost("/api/widgetsBundle/" + widgetsBundle.getId().getId().toString() + "/widgetTypes", widgetTypeIds);
   List<WidgetType> loadedWidgetTypes = doGetTyped("/api/widgetTypes?widgetsBundleId={widgetsBundleId}", new TypeReference<>() {
   }, widgetsBundle.getId().getId().toString());
   Collections.sort(widgetTypes, idComparator);
   Collections.sort(loadedWidgetTypes, idComparator);
   Assert.assertEquals(widgetTypes, loadedWidgetTypes);
}

### 190.Test Preparation Error
link: https://github.com/alibaba/nacos/commit/849393c4a1eeaeee20dbbd7101cf60b36f91cf08
p_path: config/src/main/java/com/alibaba/nacos/config/server/service/repository/embedded/EmbeddedHistoryConfigInfoPersistServiceImpl.java#findDeletedConfig
t_path: config/src/test/java/com/alibaba/nacos/config/server/service/repository/embedded/EmbeddedHistoryConfigInfoPersistServiceImplTest.java#testFindDeletedConfig

```java:test_src

@Test
public void testFindDeletedConfig() {
   Map<String, Object> mockObj1 = new HashMap<>();
   mockObj1.put("nid", new BigInteger("1234"));
   mockObj1.put("data_id", "data_id1");
   mockObj1.put("group_id", "group_id1");
   mockObj1.put("tenant_id", "tenant_id1");
   LocalDateTime now = LocalDateTime.of(LocalDate.now(), LocalTime.now());
   mockObj1.put("gmt_modified", now);
   List<Map<String, Object>> list = new ArrayList<>();
   list.add(mockObj1);
   Map<String, Object> mockObj2 = new HashMap<>();
   mockObj2.put("nid", new BigInteger("12345"));
   mockObj2.put("data_id", "data_id2");
   mockObj2.put("group_id", "group_id2");
   mockObj2.put("tenant_id", "tenant_id2");
   LocalDateTime now2 = LocalDateTime.of(LocalDate.now(), LocalTime.now());
   mockObj2.put("gmt_modified", now2);
   list.add(mockObj2);
   int pageSize = 1233;
   long startId = 23456;
   Timestamp timestamp = new Timestamp(System.currentTimeMillis());
   Mockito.when(databaseOperate.queryMany(anyString(), eq(new Object[] { timestamp, startId, pageSize }))).thenReturn(list);
   List<ConfigInfoWrapper> deletedConfig = embeddedHistoryConfigInfoPersistService.findDeletedConfig(timestamp, startId, pageSize);
   Assert.assertEquals("data_id1", deletedConfig.get(0).getDataId());
   Assert.assertEquals("group_id1", deletedConfig.get(0).getGroup());
   Assert.assertEquals("tenant_id1", deletedConfig.get(0).getTenant());
   Assert.assertEquals(now.toInstant(ZoneOffset.ofHours(8)).toEpochMilli(), deletedConfig.get(0).getLastModified());
   Assert.assertEquals("data_id2", deletedConfig.get(1).getDataId());
   Assert.assertEquals("group_id2", deletedConfig.get(1).getGroup());
   Assert.assertEquals("tenant_id2", deletedConfig.get(1).getTenant());
   Assert.assertEquals(now2.toInstant(ZoneOffset.ofHours(8)).toEpochMilli(), deletedConfig.get(1).getLastModified());
}

```java:test_tgt

@Test
public void testFindDeletedConfig() {
   ConfigInfoStateWrapper mockObj1 = new ConfigInfoStateWrapper();
   mockObj1.setDataId("data_id1");
   mockObj1.setGroup("group_id1");
   mockObj1.setTenant("tenant_id1");
   mockObj1.setMd5("md51");
   mockObj1.setLastModified(System.currentTimeMillis());
   List<ConfigInfoStateWrapper> list = new ArrayList<>();
   list.add(mockObj1);
   ConfigInfoStateWrapper mockObj2 = new ConfigInfoStateWrapper();
   mockObj2.setDataId("data_id2");
   mockObj2.setGroup("group_id2");
   mockObj2.setTenant("tenant_id2");
   mockObj2.setMd5("md52");
   list.add(mockObj2);
   int pageSize = 1233;
   long startId = 23456;
   Timestamp timestamp = new Timestamp(System.currentTimeMillis());
   Mockito.when(databaseOperate.queryMany(anyString(), eq(new Object[] { timestamp, startId, pageSize }), eq(CONFIG_INFO_STATE_WRAPPER_ROW_MAPPER))).thenReturn(list);
   List<ConfigInfoStateWrapper> deletedConfig = embeddedHistoryConfigInfoPersistService.findDeletedConfig(timestamp, startId, pageSize);
   Assert.assertEquals("data_id1", deletedConfig.get(0).getDataId());
   Assert.assertEquals("group_id1", deletedConfig.get(0).getGroup());
   Assert.assertEquals("tenant_id1", deletedConfig.get(0).getTenant());
   Assert.assertEquals(mockObj1.getLastModified(), deletedConfig.get(0).getLastModified());
   Assert.assertEquals("data_id2", deletedConfig.get(1).getDataId());
   Assert.assertEquals("group_id2", deletedConfig.get(1).getGroup());
   Assert.assertEquals("tenant_id2", deletedConfig.get(1).getTenant());
   Assert.assertEquals(mockObj2.getLastModified(), deletedConfig.get(1).getLastModified());
}

```java:llm_gen

@Test
public void testFindDeletedConfig() {
   ConfigInfoStateWrapper mockObj1 = new ConfigInfoStateWrapper();
   mockObj1.setId("1234");
   mockObj1.setDataId("data_id1");
   mockObj1.setGroup("group_id1");
   mockObj1.setTenant("tenant_id1");
   LocalDateTime now = LocalDateTime.of(LocalDate.now(), LocalTime.now());
   mockObj1.setLastModified(now.toInstant(ZoneOffset.ofHours(8)).toEpochMilli());
   List<ConfigInfoStateWrapper> list = new ArrayList<>();
   list.add(mockObj1);
   ConfigInfoStateWrapper mockObj2 = new ConfigInfoStateWrapper();
   mockObj2.setId("12345");
   mockObj2.setDataId("data_id2");
   mockObj2.setGroup("group_id2");
   mockObj2.setTenant("tenant_id2");
   LocalDateTime now2 = LocalDateTime.of(LocalDate.now(), LocalTime.now());
   mockObj2.setLastModified(now2.toInstant(ZoneOffset.ofHours(8)).toEpochMilli());
   list.add(mockObj2);
   int pageSize = 1233;
   long startId = 23456;
   Timestamp timestamp = new Timestamp(System.currentTimeMillis());
   Mockito.when(databaseOperate.queryMany(anyString(), eq(new Object[] { timestamp, startId, pageSize }), eq(CONFIG_INFO_STATE_WRAPPER_ROW_MAPPER)).thenReturn(list);
   List<ConfigInfoStateWrapper> deletedConfig = embeddedHistoryConfigInfoPersistService.findDeletedConfig(timestamp, startId, pageSize);
   Assert.assertEquals("data_id1", deletedConfig.get(0).getDataId());
   Assert.assertEquals("group_id1", deletedConfig.get(0).getGroup());
   Assert.assertEquals("tenant_id1", deletedConfig.get(0).getTenant());
   Assert.assertEquals(now.toInstant(ZoneOffset.ofHours(8)).toEpochMilli(), deletedConfig.get(0).getLastModified());
   Assert.assertEquals("data_id2", deletedConfig.get(1).getDataId());
   Assert.assertEquals("group_id2", deletedConfig.get(1).getGroup());
   Assert.assertEquals("tenant_id2", deletedConfig.get(1).getTenant());
   Assert.assertEquals(now2.toInstant(ZoneOffset.ofHours(8)).toEpochMilli(), deletedConfig.get(1).getLastModified());
}

### 191.Assert Error
link: https://github.com/runelite/runelite/commit/43588dd7e28519ee68cc294e3b78968e5be0e318
p_path: runelite-client/src/main/java/net/runelite/client/ui/overlay/components/TextComponent.java#render
t_path: runelite-client/src/test/java/net/runelite/client/ui/overlay/components/TextComponentTest.java#testRender

```java:test_src

@Test
public void testRender() {
   TextComponent textComponent = new TextComponent();
   textComponent.setText("test");
   textComponent.setColor(Color.RED);
   textComponent.render(graphics);
   verify(graphics, times(2)).drawString(eq("test"), anyInt(), anyInt());
   verify(graphics, atLeastOnce()).setColor(Color.RED);
}

```java:test_tgt

@Test
public void testRender() {
   TextComponent textComponent = new TextComponent();
   textComponent.setText("test");
   textComponent.setColor(Color.RED);
   textComponent.render(graphics);
   verify(graphics, times(2)).drawString(eq("test"), anyInt(), anyInt());
   verify(graphics).setColor(Color.RED);
}

```java:llm_gen

@Test
public void testRender() {
   TextComponent textComponent = new TextComponent();
   textComponent.setText("test");
   textComponent.setColor(Color.RED);
   textComponent.render(graphics);
   verify(graphics, times(1)).drawString(eq("test"), anyInt(), anyInt());
   verify(graphics, atLeastOnce()).setColor(Color.RED);
}

### 192.External Class Modification
link: https://github.com/dhis2/dhis2-core/commit/1956e6a2f4fb44f2733ecff9db1b1d60a90cae16
p_path: dhis-2/dhis-services/dhis-service-analytics/src/main/java/org/hisp/dhis/analytics/table/model/AnalyticsTableColumn.java#isSkipIndex
t_path: dhis-2/dhis-services/dhis-service-analytics/src/test/java/org/hisp/dhis/analytics/table/model/AnalyticsTableColumnTest.java#testIsSkipIndex

```java:test_src

@Test
void testIsSkipIndex() {
   AnalyticsTableColumn colA = new AnalyticsTableColumn("value", DOUBLE, "value", IndexType.NONE);
   AnalyticsTableColumn colB = new AnalyticsTableColumn("ou", CHARACTER_11, "ou", IndexType.BTREE);
   assertTrue(colA.isSkipIndex());
   assertFalse(colB.isSkipIndex());
}

```java:test_tgt

@Test
void testIsSkipIndex() {
   AnalyticsTableColumn colA = new AnalyticsTableColumn("value", DOUBLE, "value", Skip.SKIP);
   AnalyticsTableColumn colB = new AnalyticsTableColumn("ou", CHARACTER_11, "ou", Skip.INCLUDE);
   assertTrue(colA.isSkipIndex());
   assertFalse(colB.isSkipIndex());
}

```java:llm_gen

@Test
void testIsSkipIndex() {
   AnalyticsTableColumn colA = new AnalyticsTableColumn("value", DOUBLE, "value", Skip.SKIP);
   AnalyticsTableColumn colB = new AnalyticsTableColumn("ou", CHARACTER_11, "ou", Skip.NO_SKIP);
   assertTrue(colA.isSkipIndex());
   assertFalse(colB.isSkipIndex());
}

### 193.Test Preparation Error
link: https://github.com/apache/hudi/commit/b99bf709e1927ccbc05a24b9b5609da4b140f5c0
p_path: hudi-io/src/main/java/org/apache/hudi/storage/StoragePathInfo.java#equals
t_path: hudi-io/src/test/java/org/apache/hudi/io/storage/TestStoragePathInfo.java#testEquals

```java:test_src

@Test
public void testEquals() {
   HoodieFileStatus fileStatus1 = new HoodieFileStatus(new HoodieLocation(PATH1), LENGTH, false, MODIFICATION_TIME);
   HoodieFileStatus fileStatus2 = new HoodieFileStatus(new HoodieLocation(PATH1), LENGTH + 2, false, MODIFICATION_TIME + 2L);
   assertEquals(fileStatus1, fileStatus2);
}

```java:test_tgt

@Test
public void testEquals() {
   StoragePathInfo pathInfo1 = new StoragePathInfo(new StoragePath(PATH1), LENGTH, false, MODIFICATION_TIME);
   StoragePathInfo pathInfo2 = new StoragePathInfo(new StoragePath(PATH1), LENGTH + 2, false, MODIFICATION_TIME + 2L);
   assertEquals(pathInfo1, pathInfo2);
}

```java:llm_gen

@Test
public void testEquals() {
   StoragePathInfo pathInfo1 = new StoragePathInfo(new Path(PATH1), LENGTH, false, MODIFICATION_TIME);
   StoragePathInfo pathInfo2 = new StoragePathInfo(new Path(PATH1), LENGTH + 2, false, MODIFICATION_TIME + 2L);
   assertEquals(pathInfo1, pathInfo2);
}

### 194.Test Preparation Error
link: https://github.com/dhis2/dhis2-core/commit/fd1cd58d008caf6ec4ba04b4ab3c9c3f7095cee0
p_path: dhis-2/dhis-web-api/src/main/java/org/hisp/dhis/webapi/controller/organisationunit/OrganisationUnitController.java#getDescendants
t_path: dhis-2/dhis-test-web-api/src/test/java/org/hisp/dhis/webapi/controller/OrganisationUnitControllerTest.java#testGetDescendants

```java:test_src

@Test
void testGetDescendants() {
   assertListOfOrganisationUnits(GET("/organisationUnits/{id}/descendants", ou1).content(), "L1", "L21", "L22", "L31", "L32");
   assertListOfOrganisationUnits(GET("/organisationUnits/{id}/descendants", ou21).content(), "L21", "L31");
}

```java:test_tgt

@Test
void testGetDescendants() {
   assertListOfOrganisationUnits(GET("/organisationUnits/{id}/descendants", ou1).content(), "L1", "L21", "L22", "L31", "L32");
   assertListOfOrganisationUnits(GET("/organisationUnits/{id}/descendants", ou21).content(), "L21", "L31");
   assertListOfOrganisationUnits(GET("/organisationUnits/{id}/descendants?filter=displayName:ilike:L2", ou1).content(), "L21", "L22");
}

```java:llm_gen

@Test
void testGetDescendants() {
   assertListOfOrganisationUnits(GET("/organisationUnits/{id}/descendants", ou1).content(), "L1", "L21", "L22", "L31", "L32");
   assertListOfOrganisationUnits(GET("/organisationUnits/{id}/descendants", ou21).content(), "L21", "L31");
   assertListOfOrganisationUnits(organisationUnitService.getOrganisationUnitWithChildren(parent.getUid()));
}

### 195.External Class Modification
link: https://github.com/apache/kafka/commit/bf88013a2812cab65bc70667e451e0a15d26b73c
p_path: group-coordinator/src/main/java/org/apache/kafka/coordinator/group/OffsetMetadataManager.java#cleanupExpiredOffsets
t_path: group-coordinator/src/test/java/org/apache/kafka/coordinator/group/OffsetMetadataManagerTest.java#testCleanupExpiredOffsets

```java:test_src

@Test
public void testCleanupExpiredOffsets() {
   GroupMetadataManager groupMetadataManager = mock(GroupMetadataManager.class);
   Group group = mock(Group.class);
   OffsetMetadataManagerTestContext context = new OffsetMetadataManagerTestContext.Builder().withGroupMetadataManager(groupMetadataManager).withOffsetsRetentionMs(1000).build();
   long commitTimestamp = context.time.milliseconds();
   context.commitOffset("group-id", "firstTopic", 0, 100L, 0, commitTimestamp);
   context.commitOffset("group-id", "secondTopic", 0, 100L, 0, commitTimestamp);
   context.commitOffset("group-id", "secondTopic", 1, 100L, 0, commitTimestamp + 500);
   context.time.sleep(1000);
   List<Record> expectedRecords = Collections.singletonList(RecordHelpers.newOffsetCommitTombstoneRecord("group-id", "secondTopic", 0));
   when(groupMetadataManager.group("group-id")).thenReturn(group);
   when(group.offsetExpirationCondition()).thenReturn(Optional.of(new OffsetExpirationConditionImpl(offsetAndMetadata -> offsetAndMetadata.commitTimestampMs)));
   when(group.isSubscribedToTopic("firstTopic")).thenReturn(true);
   when(group.isSubscribedToTopic("secondTopic")).thenReturn(false);
   List<Record> records = new ArrayList<>();
   assertFalse(context.cleanupExpiredOffsets("group-id", records));
   assertEquals(expectedRecords, records);
   context.time.sleep(500);
   expectedRecords = Collections.singletonList(RecordHelpers.newOffsetCommitTombstoneRecord("group-id", "secondTopic", 1));
   records = new ArrayList<>();
   assertFalse(context.cleanupExpiredOffsets("group-id", records));
   assertEquals(expectedRecords, records);
   when(group.isSubscribedToTopic("firstTopic")).thenReturn(false);
   context.commitOffset("group-id", "firstTopic", 1, 100L, 0, commitTimestamp + 500);
   context.commitOffset("group-id", "secondTopic", 0, 101L, 0, commitTimestamp + 500);
   expectedRecords = Arrays.asList(RecordHelpers.newOffsetCommitTombstoneRecord("group-id", "firstTopic", 0), RecordHelpers.newOffsetCommitTombstoneRecord("group-id", "firstTopic", 1), RecordHelpers.newOffsetCommitTombstoneRecord("group-id", "secondTopic", 0));
   records = new ArrayList<>();
   assertTrue(context.cleanupExpiredOffsets("group-id", records));
   assertEquals(expectedRecords, records);
}

```java:test_tgt

@Test
public void testCleanupExpiredOffsets() {
   GroupMetadataManager groupMetadataManager = mock(GroupMetadataManager.class);
   Group group = mock(Group.class);
   OffsetMetadataManagerTestContext context = new OffsetMetadataManagerTestContext.Builder().withGroupMetadataManager(groupMetadataManager).withOffsetsRetentionMs(1000).build();
   long commitTimestamp = context.time.milliseconds();
   context.commitOffset("group-id", "firstTopic", 0, 100L, 0, commitTimestamp);
   context.commitOffset("group-id", "secondTopic", 0, 100L, 0, commitTimestamp);
   context.commitOffset("group-id", "secondTopic", 1, 100L, 0, commitTimestamp + 500);
   context.time.sleep(1000);
   List<CoordinatorRecord> expectedRecords = Collections.singletonList(CoordinatorRecordHelpers.newOffsetCommitTombstoneRecord("group-id", "secondTopic", 0));
   when(groupMetadataManager.group("group-id")).thenReturn(group);
   when(group.offsetExpirationCondition()).thenReturn(Optional.of(new OffsetExpirationConditionImpl(offsetAndMetadata -> offsetAndMetadata.commitTimestampMs)));
   when(group.isSubscribedToTopic("firstTopic")).thenReturn(true);
   when(group.isSubscribedToTopic("secondTopic")).thenReturn(false);
   List<CoordinatorRecord> records = new ArrayList<>();
   assertFalse(context.cleanupExpiredOffsets("group-id", records));
   assertEquals(expectedRecords, records);
   context.time.sleep(500);
   expectedRecords = Collections.singletonList(CoordinatorRecordHelpers.newOffsetCommitTombstoneRecord("group-id", "secondTopic", 1));
   records = new ArrayList<>();
   assertFalse(context.cleanupExpiredOffsets("group-id", records));
   assertEquals(expectedRecords, records);
   when(group.isSubscribedToTopic("firstTopic")).thenReturn(false);
   context.commitOffset("group-id", "firstTopic", 1, 100L, 0, commitTimestamp + 500);
   context.commitOffset("group-id", "secondTopic", 0, 101L, 0, commitTimestamp + 500);
   expectedRecords = Arrays.asList(CoordinatorRecordHelpers.newOffsetCommitTombstoneRecord("group-id", "firstTopic", 0), CoordinatorRecordHelpers.newOffsetCommitTombstoneRecord("group-id", "firstTopic", 1), CoordinatorRecordHelpers.newOffsetCommitTombstoneRecord("group-id", "secondTopic", 0));
   records = new ArrayList<>();
   assertTrue(context.cleanupExpiredOffsets("group-id", records));
   assertEquals(expectedRecords, records);
}

```java:llm_gen

@Test
public void testCleanupExpiredOffsets() {
   GroupMetadataManager groupMetadataManager = mock(GroupMetadataManager.class);
   Group group = mock(Group.class);
   OffsetMetadataManagerTestContext context = new OffsetMetadataManagerTestContext.Builder().withGroupMetadataManager(groupMetadataManager).withOffsetsRetentionMs(1000).build();
   long commitTimestamp = context.time.milliseconds();
   context.commitOffset("group-id", "firstTopic", 0, 100L, 0, commitTimestamp);
   context.commitOffset("group-id", "secondTopic", 0, 100L, 0, commitTimestamp);
   context.commitOffset("group-id", "secondTopic", 1, 100L, 0, commitTimestamp + 500);
   context.time.sleep(1000);
   List<CoordinatorRecord> expectedRecords = Collections.singletonList(RecordHelpers.newOffsetCommitTombstoneRecord("group-id", "secondTopic", 0));
   when(groupMetadataManager.group("group-id")).thenReturn(group);
   when(group.offsetExpirationCondition()).thenReturn(Optional.of(new OffsetExpirationConditionImpl(offsetAndMetadata -> offsetAndMetadata.commitTimestampMs)));
   when(group.isSubscribedToTopic("firstTopic")).thenReturn(true);
   when(group.isSubscribedToTopic("secondTopic")).thenReturn(false);
   List<CoordinatorRecord> records = new ArrayList<>();
   assertFalse(context.cleanupExpiredOffsets("group-id", records));
   assertEquals(expectedRecords, records);
   context.time.sleep(500);
   expectedRecords = Collections.singletonList(RecordHelpers.newOffsetCommitTombstoneRecord("group-id", "secondTopic", 1));
   records = new ArrayList<>();
   assertFalse(context.cleanupExpiredOffsets("group-id", records));
   assertEquals(expectedRecords, records);
   when(group.isSubscribedToTopic("firstTopic")).thenReturn(false);
   context.commitOffset("group-id", "firstTopic", 1, 100L, 0, commitTimestamp + 500);
   context.commitOffset("group-id", "secondTopic", 0, 101L, 0, commitTimestamp + 500);
   expectedRecords = Arrays.asList(RecordHelpers.newOffsetCommitTombstoneRecord("group-id", "firstTopic", 0), RecordHelpers.newOffsetCommitTombstoneRecord("group-id", "firstTopic", 1), RecordHelpers.newOffsetCommitTombstoneRecord("group-id", "secondTopic", 0));
   records = new ArrayList<>();
   assertTrue(context.cleanupExpiredOffsets("group-id", records));
   assertEquals(expectedRecords, records);
}

### 196.External Function Modification
link: https://github.com/apache/incubator-pinot/commit/4ad36c3482740386264478717343316b53cabeba
p_path: pinot-core/src/main/java/org/apache/pinot/core/data/manager/BaseTableDataManager.java#downloadFromPeersWithoutStreaming
t_path: pinot-core/src/test/java/org/apache/pinot/core/data/manager/BaseTableDataManagerTest.java#testDownloadFromPeersWithoutStreaming

```java:test_src

@Test
public void testDownloadFromPeersWithoutStreaming() throws Exception {
   URI uri = mockRemoteCopy();
   TableDataManagerConfig config = createDefaultTableDataManagerConfig();
   when(config.getTablePeerDownloadScheme()).thenReturn("http");
   HelixManager mockedHelix = mock(HelixManager.class);
   BaseTableDataManager tmgr = createTableManager(config, mockedHelix);
   File tempRootDir = tmgr.getTmpSegmentDataDir("test-download-peer-without-streaming");
   File destFile = new File(tempRootDir, "seg01" + TarGzCompressionUtils.TAR_GZ_FILE_EXTENSION);
   try (MockedStatic<PeerServerSegmentFinder> mockPeerSegFinder = mockStatic(PeerServerSegmentFinder.class)) {
       mockPeerSegFinder.when(() -> PeerServerSegmentFinder.getPeerServerURIs("seg01", "http", mockedHelix, TABLE_NAME_WITH_TYPE)).thenReturn(Collections.singletonList(uri));
       tmgr.downloadFromPeersWithoutStreaming("seg01", mock(SegmentZKMetadata.class), destFile);
   }
   assertEquals(FileUtils.readFileToString(destFile), "this is from somewhere remote");
}

```java:test_tgt

@Test
public void testDownloadFromPeersWithoutStreaming() throws Exception {
   URI uri = mockRemoteCopy();
   InstanceDataManagerConfig config = createDefaultInstanceDataManagerConfig();
   when(config.getSegmentPeerDownloadScheme()).thenReturn("http");
   HelixManager helixManager = mock(HelixManager.class);
   BaseTableDataManager tmgr = createTableManager(config, helixManager);
   File tempRootDir = tmgr.getTmpSegmentDataDir("test-download-peer-without-streaming");
   File destFile = new File(tempRootDir, "seg01" + TarGzCompressionUtils.TAR_GZ_FILE_EXTENSION);
   try (MockedStatic<PeerServerSegmentFinder> mockPeerSegFinder = mockStatic(PeerServerSegmentFinder.class)) {
       mockPeerSegFinder.when(() -> PeerServerSegmentFinder.getPeerServerURIs("seg01", "http", helixManager, TABLE_NAME_WITH_TYPE)).thenReturn(Collections.singletonList(uri));
       tmgr.downloadFromPeersWithoutStreaming("seg01", mock(SegmentZKMetadata.class), destFile);
   }
   assertEquals(FileUtils.readFileToString(destFile), "this is from somewhere remote");
}

```java:llm_gen

@Test
public void testDownloadFromPeersWithoutStreaming() throws Exception {
   URI uri = mockRemoteCopy();
   TableDataManagerConfig config = createDefaultTableDataManagerConfig();
   BaseTableDataManager tmgr = createTableManager(config, mock(HelixManager.class));
   tmgr._peerDownloadScheme = "http";
   HelixManager mockedHelix = mock(HelixManager.class);
   File tempRootDir = tmgr.getTmpSegmentDataDir("test-download-peer-without-streaming");
   File destFile = new File(tempRootDir, "seg01" + TarGzCompressionUtils.TAR_GZ_FILE_EXTENSION);
   try (MockedStatic<PeerServerSegmentFinder> mockPeerSegFinder = mockStatic(PeerServerSegmentFinder.class)) {
       mockPeerSegFinder.when(() -> PeerServerSegmentFinder.getPeerServerURIs("seg01", "http", mockedHelix, TABLE_NAME_WITH_TYPE)).thenReturn(Collections.singletonList(uri));
       tmgr.downloadFromPeersWithoutStreaming("seg01", mock(SegmentZKMetadata.class), destFile);
   }
   assertEquals(FileUtils.readFileToString(destFile), "this is from somewhere remote");
}

### 197.Additional Asserts
link: https://github.com/BentoBoxWorld/BentoBox/commit/196e90bf4e4f0fbd8803dc523cfe4ecd826c58d6
p_path: src/main/java/world/bentobox/bentobox/managers/RanksManager.java#addRank
t_path: src/test/java/world/bentobox/bentobox/managers/RanksManagerTest.java#testAddRank

```java:test_src

@Test
public void testAddRank() {
   assertTrue(ranksManager.addRank("test.rank.reference", 750));
}

```java:test_tgt

@Test
public void testAddRank() {
   assertTrue(RanksManager.getInstance().addRank("test.rank.reference", 750));
}

```java:llm_gen

@Test
public void testAddRank() {
   assertTrue(ranksManager.addRank("test.rank.reference", 750));
   assertFalse(ranksManager.addRank(OWNER_RANK_REF, 1000));
   assertFalse(ranksManager.addRank(SUB_OWNER_RANK_REF, 900));
   assertFalse(ranksManager.addRank(TRUSTED_RANK_REF, 800));
   assertFalse(ranksManager.addRank(COOP_RANK_REF, 700));
   assertFalse(ranksManager.addRank(MEMBER_RANK_REF, 600));
   assertFalse(ranksManager.addRank(VISITOR_RANK_REF, 500));
   assertFalse(ranksManager.addRank(BANNED_RANK_REF, 400));
   assertFalse(ranksManager.addRank(ADMIN_RANK_REF, 300));
   assertFalse(ranksManager.addRank(MOD_RANK_REF, 200));
}

### 198.External Class Modification
link: https://github.com/halo-dev/halo/commit/0e17d53ede66c57b12f2dec4c92874c7e69ed9ef
p_path: application/src/main/java/run/halo/app/notification/DefaultNotificationCenter.java#getNotifiersBySubscriber
t_path: application/src/test/java/run/halo/app/notification/DefaultNotificationCenterTest.java#testGetNotifiersBySubscriber

````java:test_src

@Test
public void testGetNotifiersBySubscriber() {
    UserNotificationPreference preference = new UserNotificationPreference();
    when(userNotificationPreferenceService.getByUser(any())).thenReturn(Mono.just(preference));
    var reason = new Reason();
    reason.setMetadata(new Metadata());
    reason.getMetadata().setName("reason-a");
    reason.setSpec(new Reason.Spec());
    reason.getSpec().setReasonType("new-reply-on-comment");
    var subscriber = new Subscription.Subscriber();
    subscriber.setName("anonymousUser#A");
    notificationCenter.getNotifiersBySubscriber(subscriber, reason).collectList().as(StepVerifier::create).consumeNextWith(notifiers -> {
        assertThat(notifiers).hasSize(1);
        assertThat(notifiers.get(0)).isEqualTo("default-email-notifier");
    }).verifyComplete();
    verify(userNotificationPreferenceService).getByUser(eq(subscriber.getName()));
}

```java:test_tgt

@Test
public void testGetNotifiersBySubscriber() {
    UserNotificationPreference preference = new UserNotificationPreference();
    when(userNotificationPreferenceService.getByUser(any())).thenReturn(Mono.just(preference));
    var reason = new Reason();
    reason.setMetadata(new Metadata());
    reason.getMetadata().setName("reason-a");
    reason.setSpec(new Reason.Spec());
    reason.getSpec().setReasonType("new-reply-on-comment");
    var subscriber = new Subscriber(UserIdentity.anonymousWithEmail("A"), "fake-name");
    notificationCenter.getNotifiersBySubscriber(subscriber, reason).collectList().as(StepVerifier::create).consumeNextWith(notifiers -> {
        assertThat(notifiers).hasSize(1);
        assertThat(notifiers.get(0)).isEqualTo("default-email-notifier");
    }).verifyComplete();
    verify(userNotificationPreferenceService).getByUser(eq(subscriber.name()));
}

```java:llm_gen

@Test
public void testGetNotifiersBySubscriber() {
    UserNotificationPreference preference = new UserNotificationPreference();
    when(userNotificationPreferenceService.getByUser(any())).thenReturn(Mono.just(preference));
    var reason = new Reason();
    reason.setMetadata(new Metadata());
    reason.getMetadata().setName("reason-a");
    reason.setSpec(new Reason.Spec());
    reason.getSpec().setReasonType("new-reply-on-comment");
    var subscriber = new Subscription.Subscriber();
    subscriber.name = "anonymousUser#A";
    notificationCenter.getNotifiersBySubscriber(subscriber, reason).collectList().as(StepVerifier::create).consumeNextWith(notifiers -> {
        assertThat(notifiers).hasSize(1);
        assertThat(notifiers.get(0)).isEqualTo("default-email-notifier");
    }).verifyComplete();
    verify(userNotificationPreferenceService).getByUser(eq(subscriber.name));
}

### 199.Assert Error
link: https://github.com/neo4j-contrib/neo4j-apoc-procedures/commit/fac7fb29cea7d2bab73224db556bf47344966609
p_path: full/src/main/java/apoc/es/ElasticSearch.java#stats
t_path: full/src/test/java/apoc/es/ElasticSearchTest.java#testStats

```java:test_src

@Test
public void testStats() throws Exception {
    TestUtil.testCall(db, "CALL apoc.es.stats($host)", defaultParams, r -> {
        assertNotNull(r.get("value"));
        Object numOfDocs = extractValueFromResponse(r, "$._all.total.docs.count");
        assertNotEquals(0, numOfDocs);
    });
}

```java:test_tgt

@Test
public void testStats() throws Exception {
    TestUtil.testCall(db, "CALL apoc.es.stats($host)", defaultParams, commonEsStatsConsumer());
}

```java:llm_gen

@Test
public void testStats() throws Exception {
    TestUtil.testCall(db, "CALL apoc.es.stats($host, {})", defaultParams, r -> {
        assertNotNull(r.get("value"));
        Object numOfDocs = extractValueFromResponse(r, "$._all.total.docs.count");
        assertNotEquals(0, numOfDocs);
    });
}
````

### 200.External Function Modification
link: https://github.com/haifengl/smile/commit/ddce803064790ed644bcbc122afc3ba83a962405
p_path: deep/src/main/java/smile/llm/tokenizer/Tokenizer.java#sentencePiece
t_path: deep/src/test/java/smile/llm/tokenizer/TokenizerTest.java#testSentencePiece

````java:test_src

@Test
public void testSentencePiece() throws IOException {
    var tokenizer = Tokenizer.sentencePiece("deep/src/universal/models/tokenizer_v2.model");
    int[] tokens = { 1, 910, 338, 263, 1243, 10541, 29889, 2 };
    assertArrayEquals(tokens, tokenizer.encode("This is a test sentence.", true, true));
    assertEquals("This is a test sentence.", tokenizer.decode(tokens));
}

```java:test_tgt

@Test
public void testSentencePiece() throws IOException {
    var tokenizer = Tokenizer.sentencePiece("deep/src/universal/models/tokenizer_v2.model");
    System.out.println(Arrays.toString(tokenizer.tokenize("This is a test sentence.")));
    int[] tokens1 = { 1, 910, 338, 263, 1243, 10541, 29889, 2 };
    assertEquals("This is a test sentence.", tokenizer.decode(tokens1));
    assertArrayEquals(tokens1, tokenizer.encode("This is a test sentence.", true, true));
    int[] tokens2 = { 910, 338, 263, 1243, 10541, 29889, 2 };
    assertEquals("This is a test sentence.", tokenizer.decode(tokens2));
    assertArrayEquals(tokens2, tokenizer.encode("This is a test sentence.", false, true));
    int[] tokens3 = { 1, 910, 338, 263, 1243, 10541, 29889 };
    assertEquals("This is a test sentence.", tokenizer.decode(tokens3));
    assertArrayEquals(tokens3, tokenizer.encode("This is a test sentence.", true, false));
    int[] tokens4 = { 910, 338, 263, 1243, 10541, 29889 };
    assertEquals("This is a test sentence.", tokenizer.decode(tokens4));
    assertArrayEquals(tokens4, tokenizer.encode("This is a test sentence.", false, false));
}

```java:llm_gen

@Test
public void testSentencePiece() throws IOException {
    var tokenizer = SentencePiece.sentencePiece("deep/src/universal/models/tokenizer_v2.model");
    int[] tokens = { 1, 910, 338, 263, 1243, 10541, 29889, 2 };
    assertArrayEquals(tokens, tokenizer.encode("This is a test sentence.", true, true));
    assertEquals("This is a test sentence.", tokenizer.decode(tokens));
}
````
